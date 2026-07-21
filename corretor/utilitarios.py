"""
Funções utilitárias para o Corretor de Testes
"""

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Union


def carregar_json(caminho: str) -> Union[Dict, List]:
    """
    Carrega dados de um arquivo JSON.
    
    Args:
        caminho (str): Caminho do arquivo JSON
        
    Returns:
        Union[Dict, List]: Dados carregados do JSON
        
    Raises:
        FileNotFoundError: Se o arquivo não existir
        json.JSONDecodeError: Se o JSON for inválido
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def salvar_json(dados: Union[Dict, List], caminho: str) -> None:
    """
    Salva dados em um arquivo JSON.
    
    Args:
        dados (Union[Dict, List]): Dados a serem salvos
        caminho (str): Caminho do arquivo de destino
    """
    diretorio = os.path.dirname(caminho)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)


def obter_timestamp() -> str:
    """
    Obtém o timestamp atual em formato ISO.
    
    Returns:
        str: Timestamp formatado
    """
    return datetime.now().isoformat()


def normalizar_resposta(resposta: str) -> str:
    """
    Normaliza uma resposta para comparação.
    Remove espaços extras e converte para minúsculas.
    
    Args:
        resposta (str): Resposta a normalizar
        
    Returns:
        str: Resposta normalizada
    """
    return resposta.strip().lower()


def calcular_similaridade(texto1: str, texto2: str) -> float:
    """
    Calcula similaridade entre dois textos (0-1).
    Usa comparação simples de palavras.
    
    Args:
        texto1 (str): Primeiro texto
        texto2 (str): Segundo texto
        
    Returns:
        float: Valor de similaridade entre 0 e 1
    """
    texto1 = normalizar_resposta(texto1)
    texto2 = normalizar_resposta(texto2)
    
    if texto1 == texto2:
        return 1.0
    
    palavras1 = set(texto1.split())
    palavras2 = set(texto2.split())
    
    if not palavras1 or not palavras2:
        return 0.0
    
    intersecao = len(palavras1 & palavras2)
    uniao = len(palavras1 | palavras2)
    
    return intersecao / uniao if uniao > 0 else 0.0


def validar_nivel(nivel: str) -> bool:
    """
    Valida se o nível é válido.
    
    Args:
        nivel (str): Nível a validar
        
    Returns:
        bool: True se válido, False caso contrário
    """
    niveis_validos = ["basico", "intermediario", "avancado"]
    return nivel.lower() in niveis_validos


def validar_tipo_questao(tipo: str) -> bool:
    """
    Valida se o tipo de questão é válido.
    
    Args:
        tipo (str): Tipo de questão
        
    Returns:
        bool: True se válido, False caso contrário
    """
    tipos_validos = ["multipla_escolha", "verdadeiro_falso", "dissertativa", "numerica"]
    return tipo.lower() in tipos_validos


def calcular_pontos(acertou: bool, dificuldade: int = 1, tempo_gasto: int = 0) -> int:
    """
    Calcula pontos baseado no acerto, dificuldade e tempo.
    
    Args:
        acertou (bool): Se acertou
        dificuldade (int): Nível de dificuldade (1-5)
        tempo_gasto (int): Tempo em segundos
        
    Returns:
        int: Pontos obtidos
    """
    if not acertou:
        return 0
    
    pontos_base = 10 * dificuldade
    desconto_tempo = max(0, tempo_gasto // 60)  # 1 ponto por minuto
    
    return max(0, pontos_base - desconto_tempo)


def formatar_resultado(resultado: Dict[str, Any]) -> str:
    """
    Formata um resultado para exibição legível.
    
    Args:
        resultado (Dict): Dicionário com resultado
        
    Returns:
        str: Resultado formatado
    """
    status = "✓ CORRETO" if resultado.get('acertou') else "✗ INCORRETO"
    pontos = resultado.get('pontos', 0)
    feedback = resultado.get('feedback', 'Sem feedback')
    
    return f"""
{status}
Pontos: {pontos}
Feedback: {feedback}
"""


def criar_diretorio_se_nao_existe(caminho: str) -> None:
    """
    Cria um diretório se ele não existir.
    
    Args:
        caminho (str): Caminho do diretório
    """
    if not os.path.exists(caminho):
        os.makedirs(caminho)
