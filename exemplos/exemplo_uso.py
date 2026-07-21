#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo básico de uso do Corretor de Testes Jonas
"""

from corretor import CorretorTestes


def exemplo_basico():
    """Exemplo básico de correção de um teste."""
    print("\n" + "="*60)
    print("EXEMPLO BÁSICO - Corretor de Testes Jonas")
    print("="*60 + "\n")
    
    # Criar instância do corretor
    corretor = CorretorTestes()
    
    # Carregar testes e gabarito
    print("📚 Carregando testes...")
    testes = corretor.carregar_testes(nivel="basico")
    gabarito = corretor.carregar_gabarito()
    print(f"✓ {len(testes)} testes carregados!\n")
    
    # Exemplo 1: Múltipla escolha
    print("\n📝 TESTE 1: Múltipla Escolha")
    print("-" * 60)
    teste1 = corretor.obter_teste(1)
    print(f"Pergunta: {teste1['pergunta']}")
    print(f"Opções: {teste1['opcoes']}")
    print(f"Sua resposta: 1 (Uma linguagem de programação)")
    
    resultado1 = corretor.corrigir_resposta(
        id_teste=1,
        resposta_aluno=1,
        nivel="basico",
        id_aluno="aluno_001"
    )
    print(f"\n{resultado1['feedback']}")
    print(f"Pontos: {resultado1['pontos']}")
    
    # Exemplo 2: Verdadeiro ou Falso
    print("\n\n📝 TESTE 2: Verdadeiro ou Falso")
    print("-" * 60)
    teste2 = corretor.obter_teste(2)
    print(f"Pergunta: {teste2['pergunta']}")
    print(f"Sua resposta: Verdadeiro")
    
    resultado2 = corretor.corrigir_resposta(
        id_teste=2,
        resposta_aluno=True,
        nivel="basico",
        id_aluno="aluno_001"
    )
    print(f"\n{resultado2['feedback']}")
    print(f"Pontos: {resultado2['pontos']}")
    
    # Exemplo 3: Numérica
    print("\n\n📝 TESTE 3: Questão Numérica")
    print("-" * 60)
    teste4 = corretor.obter_teste(4)
    print(f"Pergunta: {teste4['pergunta']}")
    print(f"Sua resposta: 8")
    
    resultado4 = corretor.corrigir_resposta(
        id_teste=4,
        resposta_aluno=8,
        nivel="basico",
        id_aluno="aluno_001"
    )
    print(f"\n{resultado4['feedback']}")
    print(f"Pontos: {resultado4['pontos']}")
    
    # Desempenho do aluno
    print("\n\n📊 DESEMPENHO DO ALUNO")
    print("="*60)
    desempenho = corretor.obter_desempenho_aluno("aluno_001")
    print(f"Total de Testes: {desempenho['total_testes']}")
    print(f"Total de Acertos: {desempenho['total_acertos']}")
    print(f"Taxa de Acerto: {desempenho['taxa_acerto']:.2f}%")
    print(f"Total de Pontos: {desempenho['total_pontos']}")
    print(f"Média de Pontos: {desempenho['media_pontos']:.2f}")
    
    # Estatísticas gerais
    print("\n\n📈 ESTATÍSTICAS GERAIS")
    print("="*60)
    stats = corretor.obter_estatisticas_gerais()
    for chave, valor in stats.items():
        print(f"{chave}: {valor}")
    
    # Salvar dados
    print("\n\n💾 SALVANDO DADOS...")
    print("="*60)
    corretor.salvar_historico()
    corretor.salvar_dados_alunos()
    print("\n✓ Dados salvos com sucesso!")


if __name__ == "__main__":
    exemplo_basico()
