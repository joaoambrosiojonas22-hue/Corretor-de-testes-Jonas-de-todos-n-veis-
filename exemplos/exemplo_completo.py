#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo completo com múltiplos alunos e geração de relatórios
"""

from corretor import CorretorTestes, GeradorRelatorio


def exemplo_completo():
    """Exemplo completo com múltiplos alunos."""
    print("\n" + "="*70)
    print("EXEMPLO COMPLETO - Múltiplos Alunos e Relatórios")
    print("="*70 + "\n")
    
    # Criar instâncias
    corretor = CorretorTestes()
    gerador = GeradorRelatorio()
    
    # Carregar dados
    print("📚 Carregando testes de todos os níveis...")
    testes = corretor.carregar_testes()
    gabarito = corretor.carregar_gabarito()
    print(f"✓ {len(testes)} testes carregados!\n")
    
    # Simular respostas de alunos
    alunos_respostas = {
        "aluno_001": [
            (1, 1, "basico"),      # Acertou
            (2, False, "basico"),  # Acertou
            (4, 8, "basico"),      # Acertou
            (5, 1, "intermediario"),  # Acertou
            (6, True, "intermediario"), # Acertou
        ],
        "aluno_002": [
            (1, 0, "basico"),      # Errou
            (2, True, "basico"),   # Errou
            (4, 9, "basico"),      # Errou
            (5, 2, "intermediario"),  # Errou
            (6, True, "intermediario"), # Acertou
        ],
        "aluno_003": [
            (1, 1, "basico"),      # Acertou
            (2, False, "basico"),  # Acertou
            (4, 8, "basico"),      # Acertou
            (5, 1, "intermediario"),  # Acertou
            (6, False, "intermediario"), # Errou
            (9, 1, "avancado"),    # Acertou
        ],
    }
    
    # Processar respostas
    print("\n📝 PROCESSANDO RESPOSTAS DOS ALUNOS")
    print("="*70 + "\n")
    
    for id_aluno, respostas in alunos_respostas.items():
        print(f"\n👤 Processando {id_aluno}...")
        for id_teste, resposta, nivel in respostas:
            resultado = corretor.corrigir_resposta(
                id_teste=id_teste,
                resposta_aluno=resposta,
                nivel=nivel,
                id_aluno=id_aluno
            )
            status = "✓" if resultado['acertou'] else "✗"
            print(f"  {status} Teste {id_teste}: {resultado['pontos']} pontos")
    
    # Gerar relatórios individuais
    print("\n\n📊 GERANDO RELATÓRIOS INDIVIDUAIS")
    print("="*70 + "\n")
    
    for id_aluno, dados_aluno in corretor.alunos.items():
        print(f"\n📄 Relatório de {id_aluno}:")
        print("-" * 70)
        
        relatorio = gerador.gerar_relatorio_aluno(
            id_aluno=id_aluno,
            resultados=dados_aluno['resultados'],
            nome_aluno=f"Aluno {id_aluno.split('_')[1]}"
        )
        
        texto = gerador.gerar_relatorio_texto(relatorio)
        print(texto)
        
        # Salvar relatório
        gerador.salvar_relatorio(
            relatorio,
            f"output/relatorio_{id_aluno}.json"
        )
    
    # Gerar relatório da turma
    print("\n\n📈 GERANDO RELATÓRIO DA TURMA")
    print("="*70 + "\n")
    
    relatorio_turma = gerador.gerar_relatorio_turma(corretor.alunos)
    
    texto_turma = gerador.gerar_relatorio_texto(relatorio_turma)
    print(texto_turma)
    
    # Mostrar detalhes da turma
    print("\nDesempenho por Aluno:")
    print("-" * 70)
    for aluno in relatorio_turma['desempenho_alunos']:
        print(f"  {aluno['id']}: {aluno['taxa_acerto']:.1f}% ({aluno['total_acertos']}/{aluno['total_testes']})")
    
    # Salvar relatório da turma
    gerador.salvar_relatorio(
        relatorio_turma,
        "output/relatorio_turma.json"
    )
    
    # Salvar dados finais
    print("\n\n💾 SALVANDO DADOS")
    print("="*70)
    corretor.salvar_historico()
    corretor.salvar_dados_alunos()
    print("\n✓ Todos os dados foram salvos com sucesso!")


if __name__ == "__main__":
    exemplo_completo()
