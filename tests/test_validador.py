"""
Testes para o módulo validador
"""

import pytest
from corretor.validador import Validador


class TestValidador:
    """Testes da classe Validador."""
    
    @pytest.fixture
    def validador(self):
        """Fixture para criar uma instância do Validador."""
        return Validador()
    
    def test_validar_multipla_escolha_correta(self, validador):
        """Testa validação de múltipla escolha com resposta correta."""
        acertou, confianca = validador.validar_multipla_escolha("B", "B")
        assert acertou is True
        assert confianca == 1.0
    
    def test_validar_multipla_escolha_incorreta(self, validador):
        """Testa validação de múltipla escolha com resposta incorreta."""
        acertou, confianca = validador.validar_multipla_escolha("A", "B")
        assert acertou is False
        assert confianca == 0.0
    
    def test_validar_verdadeiro_falso_correto(self, validador):
        """Testa validação verdadeiro/falso com resposta correta."""
        acertou, confianca = validador.validar_verdadeiro_falso(True, True)
        assert acertou is True
        assert confianca == 1.0
    
    def test_validar_numerica_correta(self, validador):
        """Testa validação numérica com resposta correta."""
        acertou, confianca = validador.validar_numerica(10, 10)
        assert acertou is True
        assert confianca == 1.0
    
    def test_validar_numerica_com_margem(self, validador):
        """Testa validação numérica com margem de erro."""
        acertou, confianca = validador.validar_numerica(10.05, 10, margem_erro=0.01)
        assert acertou is True
    
    def test_validar_dissertativa(self, validador):
        """Testa validação de dissertativa."""
        acertou, confianca = validador.validar_dissertativa(
            "Python é uma linguagem de programação",
            "Python é uma linguagem de programação"
        )
        assert acertou is True
        assert confianca >= 0.7
