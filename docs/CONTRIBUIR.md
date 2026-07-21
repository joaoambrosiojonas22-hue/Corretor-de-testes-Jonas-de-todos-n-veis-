# 🤝 Guia de Contribuição

## Bem-vindo! 👋

Obrigado por considerar contribuir para o **Corretor de Testes Jonas**! Este documento fornece orientações para contribuir com o projeto.

---

## 📋 Índice

1. [Código de Conduta](#código-de-conduta)
2. [Como Contribuir](#como-contribuir)
3. [Processo de Pull Request](#processo-de-pull-request)
4. [Padrões de Código](#padrões-de-código)
5. [Commits](#commits)
6. [Testes](#testes)

---

## 📜 Código de Conduta

Este projeto adota um Código de Conduta para garantir um ambiente acolhedor para todos:

- ✅ Ser respeitoso com todas as pessoas
- ✅ Aceitar críticas construtivas
- ✅ Focar no que é melhor para a comunidade
- ✅ Mostrar empatia com outros membros

❌ Comportamentos inaceitáveis incluem:
- Linguagem ofensiva ou discriminatória
- Assédio de qualquer forma
- Publicação de informações privadas
- Ataques pessoais

---

## 🎯 Como Contribuir

### Reportar Bugs 🐛

**Antes de abrir uma issue:**
- Verifique se o bug já foi reportado
- Tente reproduzir o problema
- Prepare um exemplo mínimo

**Ao reportar, inclua:**
```
Título: [BUG] Descrição breve

Descrição:
- O que você esperava que acontecesse
- O que realmente aconteceu
- Versão do Python
- Sistema operacional

Passo a Passo para Reproduzir:
1. ...
2. ...
3. ...

Código de Exemplo:
```python
# Seu código aqui
```
```

### Sugerir Melhorias 💡

**Ao sugerir, forneça:**
- Descrição clara da melhoria
- Por que seria útil
- Exemplos de implementação
- Casos de uso

### Implementar Funcionalidades ✨

Para novos recursos:
1. Abra uma issue primeiro para discutir
2. Espere aprovação
3. Implemente seguindo os padrões do projeto
4. Adicione testes
5. Atualize documentação

---

## 🔄 Processo de Pull Request

### Passo 1: Fork o Repositório

```bash
git clone https://github.com/SEU_USUARIO/Corretor-de-testes-Jonas-de-todos-n-veis-.git
cd Corretor-de-testes-Jonas-de-todos-n-veis-
```

### Passo 2: Crie uma Branch

```bash
git checkout -b feature/sua-feature
# ou
git checkout -b fix/seu-bugfix
```

Nomeia a branch com prefixo:
- `feature/` - Nova funcionalidade
- `fix/` - Correção de bug
- `docs/` - Documentação
- `test/` - Testes
- `refactor/` - Refatoração

### Passo 3: Faça suas Mudanças

```bash
# Faça suas alterações
# Commit regularmente
git add .
git commit -m "descrição das mudanças"
```

### Passo 4: Teste suas Mudanças

```bash
# Execute os testes
pytest tests/

# Verifique cobertura
pytest tests/ --cov=corretor
```

### Passo 5: Push e Crie PR

```bash
git push origin feature/sua-feature
```

Vá para o GitHub e crie um Pull Request.

### Passo 6: Responda aos Comentários

- ✅ Responda todas as revisões
- ✅ Faça ajustes solicitados
- ✅ Mantenha a conversa respeitosa

---

## 🎨 Padrões de Código

### PEP 8

Siga [PEP 8](https://www.python.org/dev/peps/pep-0008/) rigorosamente:

```python
# ✅ Correto
def calcular_pontos(acertou: bool, dificuldade: int = 1) -> int:
    """Calcula pontos baseado em acerto e dificuldade."""
    if acertou:
        return 10 * dificuldade
    return 0

# ❌ Incorreto
def calcularPontos(acertou,dificuldade=1):
    if acertou: return 10*dificuldade
    else: return 0
```

### Docstrings

Use docstrings estilo Google:

```python
def validar_resposta(
    tipo_questao: str,
    resposta_aluno: Any,
    resposta_correta: Any
) -> Dict[str, Any]:
    """
    Valida uma resposta com base no tipo de questão.
    
    Args:
        tipo_questao (str): Tipo de questão
        resposta_aluno (Any): Resposta do aluno
        resposta_correta (Any): Resposta correta
        
    Returns:
        Dict[str, Any]: Resultado da validação com chaves:
            - 'acertou' (bool): Se acertou
            - 'confianca' (float): Nível de confiança
    """
    # Implementação
    pass
```

### Nomes de Variáveis

```python
# ✅ Bom
total_acertos = 0
taxa_acerto_percentual = 0.85
id_aluno = "aluno_001"

# ❌ Ruim
ta = 0
tap = 0.85
id = "aluno_001"
a = 0
```

### Imports

```python
# ✅ Organizado
import json
from typing import Dict, List, Any
from datetime import datetime

from corretor.validador import Validador
from corretor.utilitarios import normalizar_resposta

# ❌ Desordenado
from corretor.utilitarios import normalizar_resposta
import json
from corretor.validador import Validador
from typing import Dict, List, Any
from datetime import datetime
```

---

## 📝 Commits

### Mensagens de Commit

Use o formato:

```
<tipo>: <descrição breve>

<descrição detalhada>

Fixes #<issue_number>
```

**Tipos:**
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Manutenção

**Exemplos:**

```
feat: implementar validação de respostas dissertativas

Agora o sistema usa algoritmo de similaridade para
validar respostas dissertativas. Implementa matriz de
similaridade usando Jaccard distance.

Fixes #15
```

```
fix: corrigir cálculo de pontos com tempo

O desconto de tempo não estava sendo aplicado corretamente.
Agora calcula 1 ponto por minuto gastos.

Fixes #23
```

---

## 🧪 Testes

### Estrutura de Testes

```python
import pytest
from corretor.validador import Validador

class TestValidador:
    """Testes da classe Validador."""
    
    @pytest.fixture
    def validador(self):
        """Fixture para criar instância."""
        return Validador()
    
    def test_validar_multipla_escolha_correta(self, validador):
        """Testa validação com resposta correta."""
        acertou, confianca = validador.validar_multipla_escolha("B", "B")
        assert acertou is True
        assert confianca == 1.0
    
    def test_validar_multipla_escolha_incorreta(self, validador):
        """Testa validação com resposta incorreta."""
        acertou, confianca = validador.validar_multipla_escolha("A", "B")
        assert acertou is False
```

### Executar Testes

```bash
# Executar todos
pytest

# Com verbosidade
pytest -v

# Com cobertura
pytest --cov=corretor

# Teste específico
pytest tests/test_validador.py::TestValidador::test_validar_multipla_escolha_correta
```

### Requisitos para PR

- ✅ Todos os testes passando
- ✅ Cobertura mínima de 80%
- ✅ Sem erros de linting
- ✅ Documentação atualizada

---

## 📚 Documentação

### Atualizar README

Se sua mudança afeta funcionalidade:
```markdown
1. Atualize a seção relevante
2. Adicione exemplo prático
3. Atualize índice se necessário
```

### Adicionar Exemplos

Crie exemplos em `/exemplos/`:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo: Descrição do que o exemplo faz
"""

from corretor import CorretorTestes

def exemplo():
    """Descreva o exemplo."""
    # Seu código aqui
    pass

if __name__ == "__main__":
    exemplo()
```

---

## ✅ Checklist para PR

Antes de enviar:

- [ ] Código segue PEP 8
- [ ] Docstrings adicionadas/atualizadas
- [ ] Testes adicionados/passam
- [ ] Cobertura >= 80%
- [ ] README atualizado
- [ ] Exemplos funcionam
- [ ] Sem erros de linting
- [ ] Mensagens de commit descritivas
- [ ] Nenhum arquivo não intencional adicionado

---

## 🎓 Recursos Úteis

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Git Workflow](https://git-scm.com/book/en/v2)

---

## ❓ Dúvidas?

- 💬 Abra uma issue para discutir
- 📧 Entre em contato
- 📖 Consulte a documentação

---

**Obrigado por contribuir! Você é incrível! 🌟**
