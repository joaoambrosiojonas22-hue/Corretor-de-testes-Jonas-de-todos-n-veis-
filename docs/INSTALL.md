# 🚀 Guia de Instalação e Uso

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Configuração](#configuração)
4. [Como Usar](#como-usar)
5. [Exemplos Práticos](#exemplos-práticos)
6. [Troubleshooting](#troubleshooting)

---

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter:

- **Python 3.8+** instalado ([Download Python](https://www.python.org/downloads/))
- **Git** instalado ([Download Git](https://git-scm.com/))
- **pip** (gerenciador de pacotes Python) - geralmente já vem com Python

Para verificar se está tudo instalado:

```bash
python --version
git --version
pip --version
```

---

## 💻 Instalação

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/joaoambrosiojonas22-hue/Corretor-de-testes-Jonas-de-todos-n-veis-.git
cd Corretor-de-testes-Jonas-de-todos-n-veis-
```

### Passo 2: Criar Ambiente Virtual

Um ambiente virtual isola as dependências do projeto:

**No Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

Você saberá que está ativado quando ver `(venv)` no terminal.

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias:
- `pytest` - para testes
- `pandas` - para análise de dados
- `matplotlib` - para gráficos
- `reportlab` - para gerar PDFs

### Passo 4: Verificar Instalação

```bash
python -c "from corretor import CorretorTestes; print('✓ Instalação bem-sucedida!')"
```

---

## ⚙️ Configuração

### Estrutura de Diretórios

O projeto cria automaticamente os seguintes diretórios:

```
data/              # Testes em JSON
output/            # Resultados e relatórios
logs/              # Arquivos de log
```

Se quiser criar manualmente:

```bash
mkdir -p data output logs
```

### Adicionar Seus Próprios Testes

Crie um arquivo `data/testes_customizado.json`:

```json
[
  {
    "id": 1,
    "nivel": "basico",
    "tipo": "multipla_escolha",
    "pergunta": "Sua pergunta aqui?",
    "opcoes": ["Opção A", "Opção B", "Opção C"],
    "resposta_correta": 0,
    "explicacao": "Explicação da resposta",
    "dificuldade": 1
  }
]
```

E atualize `data/gabarito.json`:

```json
{
  "1": 0
}
```

---

## 🎯 Como Usar

### Uso Básico

```python
from corretor import CorretorTestes

# 1. Criar instância
corretor = CorretorTestes()

# 2. Carregar testes
testes = corretor.carregar_testes(nivel="basico")
gabarito = corretor.carregar_gabarito()

# 3. Corrigir uma resposta
resultado = corretor.corrigir_resposta(
    id_teste=1,
    resposta_aluno="B",
    nivel="basico",
    id_aluno="aluno_001"
)

# 4. Ver resultado
print(f"Acertou: {resultado['acertou']}")
print(f"Feedback: {resultado['feedback']}")
print(f"Pontos: {resultado['pontos']}")
```

### Tipos de Questões Suportadas

#### 1️⃣ Múltipla Escolha

```python
resultado = corretor.corrigir_resposta(
    id_teste=1,
    resposta_aluno=1,  # Índice da opção (0, 1, 2, ...)
    nivel="basico"
)
```

#### 2️⃣ Verdadeiro/Falso

```python
resultado = corretor.corrigir_resposta(
    id_teste=2,
    resposta_aluno=True,  # ou False
    nivel="basico"
)
```

#### 3️⃣ Dissertativa

```python
resultado = corretor.corrigir_resposta(
    id_teste=3,
    resposta_aluno="Sua resposta aqui",
    nivel="basico"
)
```

#### 4️⃣ Numérica

```python
resultado = corretor.corrigir_resposta(
    id_teste=4,
    resposta_aluno=42,  # ou 42.5 para decimais
    nivel="basico"
)
```

### Gerar Relatórios

```python
from corretor import GeradorRelatorio

gerador = GeradorRelatorio()

# Relatório individual
relatorio = gerador.gerar_relatorio_aluno(
    id_aluno="aluno_001",
    resultados=corretor.alunos["aluno_001"]["resultados"],
    nome_aluno="João Silva"
)

# Salvar como JSON
gerador.salvar_relatorio(relatorio, "output/relatorio.json")

# Ver em formato texto
texto = gerador.gerar_relatorio_texto(relatorio)
print(texto)
```

### Obter Desempenho

```python
# Desempenho de um aluno
desempenho = corretor.obter_desempenho_aluno("aluno_001")
print(f"Taxa de acerto: {desempenho['taxa_acerto']:.1f}%")
print(f"Total de pontos: {desempenho['total_pontos']}")

# Estatísticas gerais
stats = corretor.obter_estatisticas_gerais()
print(f"Total de testes: {stats['total_testes']}")
print(f"Taxa geral: {stats['taxa_acerto']:.1f}%")
```

---

## 📚 Exemplos Práticos

### Exemplo 1: Corrigir Teste de um Aluno

Execute o exemplo básico:

```bash
python exemplos/exemplo_uso.py
```

**Saída esperada:**
```
============================================================
EXEMPLO BÁSICO - Corretor de Testes Jonas
============================================================

📚 Carregando testes...
✓ 4 testes carregados!

📝 TESTE 1: Múltipla Escolha
------------------------------------------------------------
Pergunta: O que é Python?
Opções: ['Uma serpente', 'Uma linguagem de programação', 'Um filme', 'Um animal']
Sua resposta: 1 (Uma linguagem de programação)

✓ CORRETO
Feedback: ✓ Parabéns! Resposta correta...
Pontos: 10
```

### Exemplo 2: Processar Múltiplos Alunos com Relatórios

```bash
python exemplos/exemplo_completo.py
```

Este exemplo:
- ✅ Processa 3 alunos diferentes
- 📊 Gera relatórios individuais
- 📈 Gera relatório da turma
- 💾 Salva tudo em JSON

Os arquivos gerados ficarão em `output/`:
- `relatorio_aluno_001.json`
- `relatorio_aluno_002.json`
- `relatorio_aluno_003.json`
- `relatorio_turma.json`
- `historico.json`
- `alunos.json`

### Exemplo 3: Criar Seu Próprio Script

Crie um arquivo `meu_teste.py`:

```python
from corretor import CorretorTestes, GeradorRelatorio

# Inicializar
corretor = CorretorTestes()
gerador = GeradorRelatorio()

# Carregar dados
corretor.carregar_testes()
corretor.carregar_gabarito()

# Simular respostas
respostas = [
    (1, 1, "basico"),
    (2, False, "basico"),
    (3, "Uma variável armazena valores", "basico"),
]

# Processar
for id_teste, resposta, nivel in respostas:
    resultado = corretor.corrigir_resposta(
        id_teste=id_teste,
        resposta_aluno=resposta,
        nivel=nivel,
        id_aluno="meu_aluno"
    )
    print(f"Teste {id_teste}: {'✓' if resultado['acertou'] else '✗'}")

# Gerar relatório
desempenho = corretor.obter_desempenho_aluno("meu_aluno")
print(f"\nTaxa de acerto: {desempenho['taxa_acerto']:.1f}%")
```

Execute com:
```bash
python meu_teste.py
```

---

## 🔧 Troubleshooting

### ❌ Erro: "ModuleNotFoundError: No module named 'corretor'"

**Solução:**
```bash
# Certifique-se de estar no diretório do projeto
cd Corretor-de-testes-Jonas-de-todos-n-veis-

# Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências novamente
pip install -r requirements.txt
```

### ❌ Erro: "FileNotFoundError: data/testes_basico.json"

**Solução:**
Certifique-se de que está executando o código do diretório raiz do projeto:

```bash
cd Corretor-de-testes-Jonas-de-todos-n-veis-
python exemplos/exemplo_uso.py
```

### ❌ Erro: "Python 3.8+ required"

**Solução:**
```bash
# Verificar versão
python --version

# Se necessário, instale uma versão mais recente
# https://www.python.org/downloads/
```

### ❌ Diretórios "output" ou "data" não aparecem

**Solução:**
O projeto cria automaticamente. Se não aparecer:

```bash
mkdir -p data output logs
```

### ❌ Ambiente virtual não ativa

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**
```bash
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📞 Suporte Adicional

Se encontrar problemas:

1. **Consulte a documentação:** `/docs/API.md`
2. **Veja exemplos:** `/exemplos/`
3. **Abra uma issue:** [GitHub Issues](https://github.com/joaoambrosiojonas22-hue/Corretor-de-testes-Jonas-de-todos-n-veis-/issues)

---

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Exemplo básico executado (`python exemplos/exemplo_uso.py`)
- [ ] Testes passando (`pytest tests/`)

Se todos os itens estão marcados, **você está pronto para usar! 🎉**

---

**Última atualização:** Julho 2024
**Versão:** 1.0.0
