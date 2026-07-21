"""
Validador de respostas para diferentes tipos de questões
"""

from typing import Dict, Any, Union, Tuple
from .utilitarios import normalizar_resposta, calcular_similaridade


class Validador:
    """Classe para validar diferentes tipos de respostas."""
    
    # Limiar de similaridade para questões dissertativas
    LIMIAR_SIMILARIDADE = 0.7
    
    def __init__(self):
        """Inicializa o validador."""
        self.historico_validacoes = []
    
    def validar_multipla_escolha(
        self,
        resposta_aluno: Union[str, int],
        resposta_correta: Union[str, int]
    ) -> Tuple[bool, float]:
        """
        Valida resposta de múltipla escolha.
        
        Args:
            resposta_aluno: Resposta do aluno (letra ou índice)
            resposta_correta: Resposta correta (letra ou índice)
            
        Returns:
            Tuple[bool, float]: (acertou, confiança)
        """
        # Normalizar para string
        resp_aluno = str(resposta_aluno).strip().upper()
        resp_correta = str(resposta_correta).strip().upper()
        
        acertou = resp_aluno == resp_correta
        confianca = 1.0 if acertou else 0.0
        
        self.historico_validacoes.append({
            'tipo': 'multipla_escolha',
            'acertou': acertou,
            'confianca': confianca
        })
        
        return acertou, confianca
    
    def validar_verdadeiro_falso(
        self,
        resposta_aluno: Union[str, bool],
        resposta_correta: Union[str, bool]
    ) -> Tuple[bool, float]:
        """
        Valida resposta Verdadeiro/Falso.
        
        Args:
            resposta_aluno: Resposta do aluno
            resposta_correta: Resposta correta
            
        Returns:
            Tuple[bool, float]: (acertou, confiança)
        """
        # Normalizar para boolean
        def para_bool(resposta):
            if isinstance(resposta, bool):
                return resposta
            resp_str = str(resposta).strip().lower()
            return resp_str in ['verdadeiro', 'true', 'v', '1', 's', 'sim']
        
        resp_aluno = para_bool(resposta_aluno)
        resp_correta = para_bool(resposta_correta)
        
        acertou = resp_aluno == resp_correta
        confianca = 1.0 if acertou else 0.0
        
        self.historico_validacoes.append({
            'tipo': 'verdadeiro_falso',
            'acertou': acertou,
            'confianca': confianca
        })
        
        return acertou, confianca
    
    def validar_dissertativa(
        self,
        resposta_aluno: str,
        resposta_correta: str,
        palavras_chave: list = None
    ) -> Tuple[bool, float]:
        """
        Valida resposta dissertativa usando similaridade.
        
        Args:
            resposta_aluno: Resposta do aluno
            resposta_correta: Resposta correta esperada
            palavras_chave: Lista de palavras-chave importantes
            
        Returns:
            Tuple[bool, float]: (acertou, confiança)
        """
        similaridade = calcular_similaridade(resposta_aluno, resposta_correta)
        
        # Se tem palavras-chave, verificar se estão presentes
        confianca = similaridade
        
        if palavras_chave:
            palavras_encontradas = 0
            resposta_lower = normalizar_resposta(resposta_aluno)
            
            for palavra in palavras_chave:
                if normalizar_resposta(palavra) in resposta_lower:
                    palavras_encontradas += 1
            
            taxa_palavras = palavras_encontradas / len(palavras_chave)
            confianca = (similaridade + taxa_palavras) / 2
        
        acertou = confianca >= self.LIMIAR_SIMILARIDADE
        
        self.historico_validacoes.append({
            'tipo': 'dissertativa',
            'acertou': acertou,
            'confianca': confianca
        })
        
        return acertou, confianca
    
    def validar_numerica(
        self,
        resposta_aluno: Union[int, float],
        resposta_correta: Union[int, float],
        margem_erro: float = 0.01
    ) -> Tuple[bool, float]:
        """
        Valida resposta numérica com margem de erro.
        
        Args:
            resposta_aluno: Resposta numérica do aluno
            resposta_correta: Resposta numérica correta
            margem_erro: Margem de erro aceitável (percentual)
            
        Returns:
            Tuple[bool, float]: (acertou, confiança)
        """
        try:
            aluno = float(resposta_aluno)
            correta = float(resposta_correta)
        except (ValueError, TypeError):
            return False, 0.0
        
        if correta == 0:
            acertou = aluno == correta
            confianca = 1.0 if acertou else 0.0
        else:
            erro_percentual = abs(aluno - correta) / abs(correta)
            acertou = erro_percentual <= margem_erro
            confianca = max(0.0, 1.0 - erro_percentual)
        
        self.historico_validacoes.append({
            'tipo': 'numerica',
            'acertou': acertou,
            'confianca': confianca
        })
        
        return acertou, confianca
    
    def validar_resposta(
        self,
        tipo_questao: str,
        resposta_aluno: Any,
        resposta_correta: Any,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Valida uma resposta com base no tipo de questão.
        
        Args:
            tipo_questao: Tipo de questão
            resposta_aluno: Resposta do aluno
            resposta_correta: Resposta correta
            **kwargs: Argumentos adicionais (palavras_chave, margem_erro, etc)
            
        Returns:
            Dict: Resultado da validação
        """
        tipo = tipo_questao.lower()
        
        if tipo == 'multipla_escolha':
            acertou, confianca = self.validar_multipla_escolha(
                resposta_aluno, resposta_correta
            )
        elif tipo == 'verdadeiro_falso':
            acertou, confianca = self.validar_verdadeiro_falso(
                resposta_aluno, resposta_correta
            )
        elif tipo == 'dissertativa':
            palavras_chave = kwargs.get('palavras_chave', None)
            acertou, confianca = self.validar_dissertativa(
                resposta_aluno, resposta_correta, palavras_chave
            )
        elif tipo == 'numerica':
            margem = kwargs.get('margem_erro', 0.01)
            acertou, confianca = self.validar_numerica(
                resposta_aluno, resposta_correta, margem
            )
        else:
            raise ValueError(f"Tipo de questão desconhecido: {tipo}")
        
        return {
            'tipo': tipo,
            'acertou': acertou,
            'confianca': confianca
        }
    
    def obter_historico(self) -> list:
        """
        Retorna o histórico de validações.
        
        Returns:
            list: Histórico de validações
        """
        return self.historico_validacoes
    
    def limpar_historico(self) -> None:
        """Limpa o histórico de validações."""
        self.historico_validacoes = []
