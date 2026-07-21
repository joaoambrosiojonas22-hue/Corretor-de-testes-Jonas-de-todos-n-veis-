"""
Classe principal do Corretor de Testes
Responsável pela orquestração da correção de testes
"""

from typing import Dict, List, Any, Optional
from .validador import Validador
from .utilitarios import (
    carregar_json, salvar_json, obter_timestamp, 
    calcular_pontos, normalizar_resposta, criar_diretorio_se_nao_existe
)


class CorretorTestes:
    """
    Classe principal para correção automática de testes.
    
    Exemplo:
        >>> corretor = CorretorTestes()
        >>> resultado = corretor.corrigir_resposta(1, "B", "basico")
        >>> print(resultado)
    """
    
    def __init__(self, caminho_dados: str = "data"):
        """
        Inicializa o Corretor de Testes.
        
        Args:
            caminho_dados (str): Caminho para diretório de dados
        """
        self.caminho_dados = caminho_dados
        self.validador = Validador()
        self.testes_carregados = {}
        self.gabarito = {}
        self.historico_correcoes = []
        self.alunos = {}
        
        # Criar diretórios necessários
        criar_diretorio_se_nao_existe(caminho_dados)
        criar_diretorio_se_nao_existe("output")
        criar_diretorio_se_nao_existe("logs")
    
    def carregar_testes(self, nivel: Optional[str] = None) -> Dict[int, Dict]:
        """
        Carrega testes do arquivo JSON.
        
        Args:
            nivel (str): Nível específico (basico, intermediario, avancado)
                        Se None, carrega todos os níveis
        
        Returns:
            Dict: Dicionário com testes carregados
        """
        if nivel is None:
            niveis = ["basico", "intermediario", "avancado"]
        else:
            niveis = [nivel.lower()]
        
        for nv in niveis:
            caminho = f"{self.caminho_dados}/testes_{nv}.json"
            try:
                testes = carregar_json(caminho)
                for teste in testes:
                    self.testes_carregados[teste.get('id')] = teste
            except FileNotFoundError:
                print(f"Aviso: Arquivo {caminho} não encontrado")
        
        return self.testes_carregados
    
    def carregar_gabarito(self) -> Dict[int, Any]:
        """
        Carrega o gabarito de respostas.
        
        Returns:
            Dict: Dicionário com gabarito
        """
        try:
            self.gabarito = carregar_json(f"{self.caminho_dados}/gabarito.json")
        except FileNotFoundError:
            print("Aviso: Arquivo gabarito.json não encontrado")
        
        return self.gabarito
    
    def obter_teste(self, id_teste: int) -> Optional[Dict]:
        """
        Obtém um teste específico.
        
        Args:
            id_teste (int): ID do teste
            
        Returns:
            Dict: Dados do teste ou None
        """
        return self.testes_carregados.get(id_teste)
    
    def corrigir_resposta(
        self,
        id_teste: int,
        resposta_aluno: Any,
        nivel: str,
        id_aluno: Optional[str] = None,
        tempo_gasto: int = 0
    ) -> Dict[str, Any]:
        """
        Corrige a resposta de um aluno em um teste específico.
        
        Args:
            id_teste (int): ID do teste
            resposta_aluno (Any): Resposta do aluno
            nivel (str): Nível do teste (basico, intermediario, avancado)
            id_aluno (str): ID do aluno
            tempo_gasto (int): Tempo gasto em segundos
            
        Returns:
            Dict: Resultado da correção
        """
        # Obter teste
        teste = self.obter_teste(id_teste)
        if not teste:
            return {
                'sucesso': False,
                'erro': f'Teste {id_teste} não encontrado'
            }
        
        # Obter resposta correta do gabarito
        resposta_correta = self.gabarito.get(id_teste)
        if not resposta_correta:
            return {
                'sucesso': False,
                'erro': f'Gabarito para teste {id_teste} não encontrado'
            }
        
        # Validar resposta
        tipo_questao = teste.get('tipo', 'multipla_escolha')
        resultado_validacao = self.validador.validar_resposta(
            tipo_questao=tipo_questao,
            resposta_aluno=resposta_aluno,
            resposta_correta=resposta_correta,
            palavras_chave=teste.get('palavras_chave'),
            margem_erro=teste.get('margem_erro', 0.01)
        )
        
        # Calcular pontos
        dificuldade = teste.get('dificuldade', 1)
        pontos = calcular_pontos(
            resultado_validacao['acertou'],
            dificuldade,
            tempo_gasto
        )
        
        # Gerar feedback
        feedback = self._gerar_feedback(
            teste,
            resultado_validacao['acertou'],
            resposta_correta
        )
        
        # Resultado final
        resultado = {
            'sucesso': True,
            'id_teste': id_teste,
            'tipo': tipo_questao,
            'nivel': nivel,
            'resposta_aluno': resposta_aluno,
            'resposta_correta': resposta_correta,
            'acertou': resultado_validacao['acertou'],
            'confianca': resultado_validacao['confianca'],
            'pontos': pontos,
            'tempo_gasto': tempo_gasto,
            'feedback': feedback,
            'timestamp': obter_timestamp()
        }
        
        # Salvar no histórico
        self.historico_correcoes.append(resultado)
        
        # Salvar dados do aluno se fornecido
        if id_aluno:
            self._salvar_resultado_aluno(id_aluno, resultado)
        
        return resultado
    
    def _gerar_feedback(
        self,
        teste: Dict,
        acertou: bool,
        resposta_correta: Any
    ) -> str:
        """
        Gera feedback para o aluno.
        
        Args:
            teste (Dict): Dados do teste
            acertou (bool): Se acertou
            resposta_correta (Any): Resposta correta
            
        Returns:
            str: Feedback gerado
        """
        if acertou:
            feedback = "✓ Parabéns! Resposta correta. "
        else:
            feedback = "✗ Resposta incorreta. "
            feedback += f"A resposta correta é: {resposta_correta}. "
        
        # Adicionar explicação se disponível
        explicacao = teste.get('explicacao', '')
        if explicacao:
            feedback += f"Explicação: {explicacao}"
        
        return feedback
    
    def _salvar_resultado_aluno(
        self,
        id_aluno: str,
        resultado: Dict
    ) -> None:
        """
        Salva o resultado para um aluno específico.
        
        Args:
            id_aluno (str): ID do aluno
            resultado (Dict): Resultado da correção
        """
        if id_aluno not in self.alunos:
            self.alunos[id_aluno] = {
                'id': id_aluno,
                'resultados': [],
                'total_pontos': 0,
                'total_acertos': 0,
                'total_testes': 0
            }
        
        aluno = self.alunos[id_aluno]
        aluno['resultados'].append(resultado)
        aluno['total_testes'] += 1
        aluno['total_pontos'] += resultado['pontos']
        
        if resultado['acertou']:
            aluno['total_acertos'] += 1
    
    def obter_desempenho_aluno(self, id_aluno: str) -> Optional[Dict]:
        """
        Obtém o desempenho de um aluno.
        
        Args:
            id_aluno (str): ID do aluno
            
        Returns:
            Dict: Dados de desempenho do aluno
        """
        if id_aluno not in self.alunos:
            return None
        
        aluno = self.alunos[id_aluno]
        total = aluno['total_testes']
        
        if total == 0:
            taxa_acerto = 0
        else:
            taxa_acerto = (aluno['total_acertos'] / total) * 100
        
        return {
            'id': id_aluno,
            'total_testes': total,
            'total_acertos': aluno['total_acertos'],
            'taxa_acerto': taxa_acerto,
            'total_pontos': aluno['total_pontos'],
            'media_pontos': aluno['total_pontos'] / total if total > 0 else 0
        }
    
    def salvar_historico(self, caminho: str = "output/historico.json") -> None:
        """
        Salva o histórico de correções.
        
        Args:
            caminho (str): Caminho do arquivo de saída
        """
        salvar_json(self.historico_correcoes, caminho)
        print(f"Histórico salvo em: {caminho}")
    
    def salvar_dados_alunos(self, caminho: str = "output/alunos.json") -> None:
        """
        Salva os dados de todos os alunos.
        
        Args:
            caminho (str): Caminho do arquivo de saída
        """
        dados = {
            aluno_id: dados_aluno
            for aluno_id, dados_aluno in self.alunos.items()
        }
        salvar_json(dados, caminho)
        print(f"Dados de alunos salvos em: {caminho}")
    
    def obter_estatisticas_gerais(self) -> Dict[str, Any]:
        """
        Obtém estatísticas gerais de todas as correções.
        
        Returns:
            Dict: Estatísticas gerais
        """
        total_testes = len(self.historico_correcoes)
        
        if total_testes == 0:
            return {
                'total_testes': 0,
                'total_acertos': 0,
                'taxa_acerto': 0,
                'pontos_totais': 0
            }
        
        total_acertos = sum(1 for r in self.historico_correcoes if r['acertou'])
        pontos_totais = sum(r['pontos'] for r in self.historico_correcoes)
        
        return {
            'total_testes': total_testes,
            'total_acertos': total_acertos,
            'taxa_acerto': (total_acertos / total_testes) * 100,
            'pontos_totais': pontos_totais,
            'pontos_medio': pontos_totais / total_testes if total_testes > 0 else 0,
            'total_alunos': len(self.alunos)
        }
