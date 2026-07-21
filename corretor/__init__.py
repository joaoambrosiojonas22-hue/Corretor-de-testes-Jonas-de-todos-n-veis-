"""
Corretor de Testes Jonas - Ferramenta de correção automática de testes
"""

from .corretor import CorretorTestes
from .validador import Validador
from .gerador_relatorio import GeradorRelatorio
from .utilitarios import carregar_json, salvar_json

__version__ = "1.0.0"
__author__ = "Jonas Ambrosio"
__all__ = [
    "CorretorTestes",
    "Validador",
    "GeradorRelatorio",
    "carregar_json",
    "salvar_json",
]
