"""
Gerador de Relatórios para o Corretor de Testes
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from .utilitarios import salvar_json, obter_timestamp


class GeradorRelatorio:
    """Gera relatórios de desempenho e análises."""
    
    def __init__(self):
        """Inicializa o gerador de relatórios."""
        self.relatorios = []
    
    def gerar_relatorio_aluno(
        self,
        id_aluno: str,
        resultados: List[Dict[str, Any]],
        nome_aluno: str = ""
    ) -> Dict[str, Any]:
        """
        Gera relatório de desempenho de um aluno.
        
        Args:
            id_aluno: ID do aluno
            resultados: Lista de resultados de testes
            nome_aluno: Nome do aluno
            
        Returns:
            Dict: Relatório gerado
        """
        if not resultados:
            return {
                'id_aluno': id_aluno,
                'nome': nome_aluno,
                'mensagem': 'Nenhum resultado para gerar relatório'
            }
        
        total_testes = len(resultados)
        total_acertos = sum(1 for r in resultados if r.get('acertou'))
        total_pontos = sum(r.get('pontos', 0) for r in resultados)
        taxa_acerto = (total_acertos / total_testes * 100) if total_testes > 0 else 0
        
        # Análise por nível
        por_nivel = {}
        for resultado in resultados:
            nivel = resultado.get('nivel', 'desconhecido')
            if nivel not in por_nivel:
                por_nivel[nivel] = {'acertos': 0, 'total': 0}
            por_nivel[nivel]['total'] += 1
            if resultado.get('acertou'):
                por_nivel[nivel]['acertos'] += 1
        
        # Análise por tipo de questão
        por_tipo = {}
        for resultado in resultados:
            tipo = resultado.get('tipo', 'desconhecido')
            if tipo not in por_tipo:
                por_tipo[tipo] = {'acertos': 0, 'total': 0}
            por_tipo[tipo]['total'] += 1
            if resultado.get('acertou'):
                por_tipo[tipo]['acertos'] += 1
        
        relatorio = {
            'id_aluno': id_aluno,
            'nome': nome_aluno,
            'data_geracao': obter_timestamp(),
            'resumo': {
                'total_testes': total_testes,
                'total_acertos': total_acertos,
                'total_erros': total_testes - total_acertos,
                'taxa_acerto': round(taxa_acerto, 2),
                'total_pontos': total_pontos,
                'media_pontos': round(total_pontos / total_testes, 2) if total_testes > 0 else 0
            },
            'por_nivel': por_nivel,
            'por_tipo': por_tipo,
            'resultados': resultados
        }
        
        self.relatorios.append(relatorio)
        return relatorio
    
    def gerar_relatorio_turma(
        self,
        alunos: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Gera relatório consolidado de uma turma.
        
        Args:
            alunos: Dicionário com dados dos alunos
            
        Returns:
            Dict: Relatório da turma
        """
        total_alunos = len(alunos)
        total_testes_turma = 0
        total_acertos_turma = 0
        total_pontos_turma = 0
        
        desempenho_alunos = []
        
        for id_aluno, dados_aluno in alunos.items():
            total = dados_aluno.get('total_testes', 0)
            acertos = dados_aluno.get('total_acertos', 0)
            pontos = dados_aluno.get('total_pontos', 0)
            
            total_testes_turma += total
            total_acertos_turma += acertos
            total_pontos_turma += pontos
            
            taxa_aluno = (acertos / total * 100) if total > 0 else 0
            
            desempenho_alunos.append({
                'id': id_aluno,
                'total_testes': total,
                'total_acertos': acertos,
                'taxa_acerto': round(taxa_aluno, 2),
                'total_pontos': pontos
            })
        
        taxa_acerto_turma = (
            total_acertos_turma / total_testes_turma * 100
        ) if total_testes_turma > 0 else 0
        
        relatorio = {
            'tipo': 'turma',
            'data_geracao': obter_timestamp(),
            'resumo': {
                'total_alunos': total_alunos,
                'total_testes': total_testes_turma,
                'total_acertos': total_acertos_turma,
                'taxa_acerto_turma': round(taxa_acerto_turma, 2),
                'total_pontos_turma': total_pontos_turma,
                'media_pontos_turma': round(
                    total_pontos_turma / total_testes_turma, 2
                ) if total_testes_turma > 0 else 0
            },
            'desempenho_alunos': desempenho_alunos
        }
        
        return relatorio
    
    def salvar_relatorio(
        self,
        relatorio: Dict[str, Any],
        caminho: str
    ) -> None:
        """
        Salva relatório em arquivo JSON.
        
        Args:
            relatorio: Relatório a salvar
            caminho: Caminho do arquivo
        """
        salvar_json(relatorio, caminho)
        print(f"✓ Relatório salvo em: {caminho}")
    
    def gerar_relatorio_texto(
        self,
        relatorio: Dict[str, Any]
    ) -> str:
        """
        Gera relatório em formato texto.
        
        Args:
            relatorio: Relatório a converter
            
        Returns:
            str: Relatório em texto formatado
        """
        texto = ""
        texto += "\n" + "="*60 + "\n"
        
        if 'nome' in relatorio:
            # Relatório individual
            texto += f"RELATÓRIO DO ALUNO\n"
            texto += f"Nome: {relatorio.get('nome', 'N/A')}\n"
            texto += f"ID: {relatorio['id_aluno']}\n"
        else:
            # Relatório de turma
            texto += f"RELATÓRIO DA TURMA\n"
        
        texto += "="*60 + "\n\n"
        
        resumo = relatorio.get('resumo', {})
        texto += "RESUMO\n"
        texto += "-"*60 + "\n"
        
        for chave, valor in resumo.items():
            chave_formatada = chave.replace('_', ' ').title()
            texto += f"{chave_formatada}: {valor}\n"
        
        texto += "\n" + "="*60 + "\n"
        
        return texto
