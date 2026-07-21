# ⚡ Quick Start

## Instalação Rápida (5 minutos)

### 1. Clone o Repositório
```bash
git clone https://github.com/joaoambrosiojonas22-hue/Corretor-de-testes-Jonas-de-todos-n-veis-.git
cd Corretor-de-testes-Jonas-de-todos-n-veis-
```

### 2. Configure o Ambiente
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Execute um Exemplo
```bash
python exemplos/exemplo_uso.py
```

---

## Uso Básico (10 linhas)

```python
from corretor import CorretorTestes

corretor = CorretorTestes()
corretor.carregar_testes()
corretor.carregar_gabarito()

resultado = corretor.corrigir_resposta(
    id_teste=1, resposta_aluno=1, nivel="basico"
)

print(f"Acertou: {resultado['acertou']}")
print(f"Feedback: {resultado['feedback']}")
```

---

## Tipos de Questões

### Múltipla Escolha
```python
resultado = corretor.corrigir_resposta(
    id_teste=1, resposta_aluno=1, nivel="basico"
)
```

### Verdadeiro/Falso
```python
resultado = corretor.corrigir_resposta(
    id_teste=2, resposta_aluno=True, nivel="basico"
)
```

### Dissertativa
```python
resultado = corretor.corrigir_resposta(
    id_teste=3, resposta_aluno="Sua resposta", nivel="basico"
)
```

### Numérica
```python
resultado = corretor.corrigir_resposta(
    id_teste=4, resposta_aluno=42, nivel="basico"
)
```

---

## Gerar Relatórios

```python
from corretor import GeradorRelatorio

gerador = GeradorRelatorio()

# Relatório individual
relatorio = gerador.gerar_relatorio_aluno(
    id_aluno="aluno_001",
    resultados=corretor.alunos["aluno_001"]["resultados"]
)
gerador.salvar_relatorio(relatorio, "relatorio.json")

# Relatório da turma
turma = gerador.gerar_relatorio_turma(corretor.alunos)
gerador.salvar_relatorio(turma, "turma.json")
```

---

## Próximos Passos

- 📖 Leia o [Guia Completo de Instalação](INSTALL.md)
- 📚 Consulte a [Documentação da API](API.md)
- 🎓 Veja os [Exemplos](../exemplos/)
- 🤝 Contribua! Leia [Como Contribuir](CONTRIBUIR.md)
