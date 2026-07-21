# 📚 Corretor de Testes Jonas - Todos os Níveis

> **Gere tempo, eficiência e prático** - Automatize a correção de testes com inteligência!

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)](https://github.com/joaoambrosiojonas22-hue/Corretor-de-testes-Jonas-de-todos-n-veis-)

---

## 🎯 Sobre o Projeto

O **Corretor de Testes Jonas** é uma ferramenta automatizada e inteligente para corrigir testes de diferentes níveis de dificuldade. Ela foi projetada para economizar tempo, aumentar eficiência e fornecer feedback prático e útil.

### ✨ Principais Funcionalidades

- ✅ **Correção Automática** - Analisa respostas e verifica se estão corretas
- 📊 **Relatórios Detalhados** - Gera estatísticas e análises de desempenho
- 🎓 **Múltiplos Níveis** - Suporta testes básico, intermediário e avançado
- 🔍 **Feedback Construtivo** - Fornece dicas e explicações para erros
- 💾 **Persistência de Dados** - Salva histórico de testes e resultados
- 🔗 **Rastreabilidade Completa** - Relaciona testes, respostas e feedback

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/joaoambrosiojonas22-hue/Corretor-de-testes-Jonas-de-todos-n-veis-.git
cd Corretor-de-testes-Jonas-de-todos-n-veis-
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Uso Básico

```python
from corretor import CorretorTestes

# Criar uma instância do corretor
corretor = CorretorTestes()

# Carregar testes
testes = corretor.carregar_testes('data/testes.json')

# Corrigir respostas do aluno
resultado = corretor.corrigir_resposta(
    id_teste=1,
    resposta_aluno="Python é uma linguagem de programação",
    nivel="basico"
)

# Visualizar resultado
print(resultado)
```

### Exemplo Completo

Veja `exemplos/exemplo_uso.py` para um exemplo prático completo.

---

## 📁 Estrutura do Projeto

```
Corretor-de-testes-Jonas-de-todos-n-veis-/
├── README.md                          # Documentação principal
├── requirements.txt                   # Dependências do projeto
├── LICENSE                            # Licença MIT
├── .gitignore                         # Arquivos ignorados pelo Git
│
├── corretor/                          # Módulo principal
│   ├── __init__.py                   # Inicialização do pacote
│   ├── corretor.py                   # Classe principal
│   ├── validador.py                  # Validação de respostas
│   ├── gerador_relatorio.py          # Geração de relatórios
│   └── utilitarios.py                # Funções auxiliares
│
├── data/                              # Dados e testes
│   ├── testes_basico.json            # Testes nível básico
│   ├── testes_intermediario.json     # Testes nível intermediário
│   ├── testes_avancado.json          # Testes nível avançado
│   └── gabarito.json                 # Gabarito de respostas
│
├── tests/                             # Testes unitários
│   ├── __init__.py
│   ├── test_corretor.py              # Testes da classe principal
│   ├── test_validador.py             # Testes do validador
│   └── test_gerador_relatorio.py    # Testes do gerador
│
├── exemplos/                          # Exemplos de uso
│   ├── exemplo_uso.py                # Exemplo básico
│   ├── exemplo_completo.py           # Exemplo avançado
│   └── exemplo_relatorio.py          # Exemplo com relatórios
│
└── docs/                              # Documentação adicional
    ├── INSTALL.md                    # Guia de instalação
    ├── API.md                        # Documentação da API
    └── CONTRIBUIR.md                 # Guia de contribuição
```

---

## 🔧 Estrutura de Dados

### Formato de Teste (JSON)

```json
{
  "id": 1,
  "nivel": "basico",
  "tipo": "multipla_escolha",
  "pergunta": "O que é Python?",
  "opcoes": [
    "Uma serpente",
    "Uma linguagem de programação",
    "Um filme"
  ],
  "resposta_correta": 1,
  "explicacao": "Python é uma linguagem de programação de alto nível",
  "dificuldade": 1
}
```

### Formato de Resultado

```json
{
  "id_teste": 1,
  "resposta_aluno": "B",
  "resposta_correta": "B",
  "acertou": true,
  "pontos": 10,
  "tempo_gasto": 45,
  "feedback": "Parabéns! Resposta correta."
}
```

---

## 📊 Recursos Principais

### 1. **Correção Automática**
- Suporta múltiplos tipos de questões
- Comparação inteligente de respostas
- Detecção de erros comuns

### 2. **Sistema de Níveis**
- 🟢 **Básico**: Conceitos fundamentais
- 🟡 **Intermediário**: Aplicação de conhecimento
- 🔴 **Avançado**: Análise e síntese

### 3. **Geração de Relatórios**
- Estatísticas por aluno
- Análise por nível
- Gráficos e visualizações
- Histórico completo

### 4. **Feedback Inteligente**
- Dicas para erros comuns
- Links para recursos de aprendizado
- Sugestões de melhoria

---

## 💻 Exemplos de Uso

### Corrigir um Teste

```python
from corretor import CorretorTestes

corretor = CorretorTestes()
resultado = corretor.corrigir_resposta(
    id_teste=1,
    resposta_aluno="B",
    nivel="basico"
)
print(f"Acertou: {resultado['acertou']}")
print(f"Pontos: {resultado['pontos']}")
```

### Gerar Relatório

```python
from corretor import CorretorTestes
from corretor import GeradorRelatorio

corretor = CorretorTestes()
gerador = GeradorRelatorio()

relatorio = gerador.gerar_relatorio_aluno(aluno_id=1)
gerador.salvar_relatorio(relatorio, 'output/relatorio.pdf')
```

---

## 🧪 Testes Unitários

Execute os testes com:

```bash
pytest tests/
```

Ou com cobertura:

```bash
pytest tests/ --cov=corretor
```

---

## 📝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

Veja [CONTRIBUIR.md](docs/CONTRIBUIR.md) para mais detalhes.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Jonas Ambrosio**
- GitHub: [@joaoambrosiojonas22-hue](https://github.com/joaoambrosiojonas22-hue)

---

## 🤝 Suporte

Se você tiver dúvidas ou encontrar problemas:

1. Verifique a [documentação](docs/)
2. Consulte os [exemplos](exemplos/)
3. Abra uma [issue](https://github.com/joaoambrosiojonas22-hue/Corretor-de-testes-Jonas-de-todos-n-veis-/issues)

---

## 🎉 Agradecimentos

Obrigado por usar o Corretor de Testes Jonas! Sua contribuição faz a diferença. 💙
