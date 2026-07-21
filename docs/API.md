# 📖 Documentação da API

## Índice

1. [CorretorTestes](#corretortestes)
2. [Validador](#validador)
3. [GeradorRelatorio](#geradorrelatorio)
4. [Utilitários](#utilitários)

---

## CorretorTestes

Classe principal responsável pela orquestração da correção de testes.

### Inicialização

```python
from corretor import CorretorTestes

corretor = CorretorTestes(caminho_dados="data")
```

**Parâmetros:**
- `caminho_dados` (str): Caminho para o diretório de dados. Padrão: `"data"`

### Métodos

#### `carregar_testes(nivel=None)`

Carrega testes do arquivo JSON.

```python
testes = corretor.carregar_testes(nivel="basico")
```

**Parâmetros:**
- `nivel` (str, opcional): Nível específico (`"basico"`, `"intermediario"`, `"avancado"`). Se None, carrega todos.

**Retorna:**
- `Dict[int, Dict]`: Dicionário com testes carregados

**Exemplo:**
```python
# Carregar testes básicos
testes_basicos = corretor.carregar_testes(nivel="basico")

# Carregar todos os testes
todos_testes = corretor.carregar_testes()
```

---

#### `carregar_gabarito()`

Carrega o gabarito de respostas.

```python
gabarito = corretor.carregar_gabarito()
```

**Retorna:**
- `Dict[int, Any]`: Dicionário com gabarito

---

#### `obter_teste(id_teste)`

Obtém um teste específico.

```python
teste = corretor.obter_teste(1)
```

**Parâmetros:**
- `id_teste` (int): ID do teste

**Retorna:**
- `Dict` ou `None`: Dados do teste ou None se não encontrado

**Exemplo:**
```python
teste = corretor.obter_teste(1)
if teste:
    print(f"Pergunta: {teste['pergunta']}")
```

---

#### `corrigir_resposta(id_teste, resposta_aluno, nivel, id_aluno=None, tempo_gasto=0)`

Corrige a resposta de um aluno.

```python
resultado = corretor.corrigir_resposta(
    id_teste=1,
    resposta_aluno="B",
    nivel="basico",
    id_aluno="aluno_001",
    tempo_gasto=45
)
```

**Parâmetros:**
- `id_teste` (int): ID do teste
- `resposta_aluno` (Any): Resposta do aluno (tipo depende da questão)
- `nivel` (str): Nível do teste
- `id_aluno` (str, opcional): ID do aluno para rastreamento
- `tempo_gasto` (int): Tempo em segundos. Padrão: 0

**Retorna:**
- `Dict`: Resultado da correção com chaves:
  - `sucesso` (bool): Se a operação foi bem-sucedida
  - `id_teste` (int): ID do teste
  - `tipo` (str): Tipo da questão
  - `acertou` (bool): Se acertou
  - `confianca` (float): Nível de confiança (0-1)
  - `pontos` (int): Pontos obtidos
  - `feedback` (str): Feedback para o aluno
  - `timestamp` (str): Data/hora da correção

**Exemplo:**
```python
resultado = corretor.corrigir_resposta(
    id_teste=1,
    resposta_aluno=1,
    nivel="basico",
    id_aluno="aluno_001"
)

if resultado['acertou']:
    print(f"Parabéns! Você ganhou {resultado['pontos']} pontos")
else:
    print(resultado['feedback'])
```

---

#### `obter_desempenho_aluno(id_aluno)`

Obtém o desempenho de um aluno.

```python
desempenho = corretor.obter_desempenho_aluno("aluno_001")
```

**Parâmetros:**
- `id_aluno` (str): ID do aluno

**Retorna:**
- `Dict`: Dados de desempenho com chaves:
  - `id` (str): ID do aluno
  - `total_testes` (int): Total de testes realizados
  - `total_acertos` (int): Total de acertos
  - `taxa_acerto` (float): Percentual de acertos
  - `total_pontos` (int): Total de pontos
  - `media_pontos` (float): Média de pontos por teste

**Exemplo:**
```python
desempenho = corretor.obter_desempenho_aluno("aluno_001")
print(f"Taxa de acerto: {desempenho['taxa_acerto']:.1f}%")
print(f"Pontos: {desempenho['total_pontos']}")
```

---

#### `obter_estatisticas_gerais()`

Obtém estatísticas gerais de todas as correções.

```python
stats = corretor.obter_estatisticas_gerais()
```

**Retorna:**
- `Dict`: Estatísticas gerais com chaves:
  - `total_testes` (int): Total de testes corrigidos
  - `total_acertos` (int): Total de acertos
  - `taxa_acerto` (float): Taxa geral de acertos
  - `pontos_totais` (int): Total de pontos
  - `pontos_medio` (float): Média de pontos
  - `total_alunos` (int): Total de alunos

---

#### `salvar_historico(caminho="output/historico.json")`

Salva o histórico de correções.

```python
corretor.salvar_historico()
```

**Parâmetros:**
- `caminho` (str): Caminho do arquivo de saída

---

#### `salvar_dados_alunos(caminho="output/alunos.json")`

Salva os dados de todos os alunos.

```python
corretor.salvar_dados_alunos()
```

---

## Validador

Classe para validação de respostas de diferentes tipos.

### Inicialização

```python
from corretor import Validador

validador = Validador()
```

### Métodos

#### `validar_multipla_escolha(resposta_aluno, resposta_correta)`

Valida resposta de múltipla escolha.

```python
acertou, confianca = validador.validar_multipla_escolha("B", "B")
```

**Retorna:**
- `Tuple[bool, float]`: (acertou, confiança)

---

#### `validar_verdadeiro_falso(resposta_aluno, resposta_correta)`

Valida resposta Verdadeiro/Falso.

```python
acertou, confianca = validador.validar_verdadeiro_falso(True, False)
```

---

#### `validar_dissertativa(resposta_aluno, resposta_correta, palavras_chave=None)`

Valida resposta dissertativa usando similaridade.

```python
acertou, confianca = validador.validar_dissertativa(
    "Python é uma linguagem",
    "Python é uma linguagem de programação",
    palavras_chave=["linguagem", "programação"]
)
```

---

#### `validar_numerica(resposta_aluno, resposta_correta, margem_erro=0.01)`

Valida resposta numérica com margem de erro.

```python
acertou, confianca = validador.validar_numerica(10.05, 10, margem_erro=0.01)
```

---

#### `validar_resposta(tipo_questao, resposta_aluno, resposta_correta, **kwargs)`

Valida uma resposta com base no tipo.

```python
resultado = validador.validar_resposta(
    tipo_questao="multipla_escolha",
    resposta_aluno=1,
    resposta_correta=1
)
```

---

## GeradorRelatorio

Classe para gerar relatórios de desempenho.

### Inicialização

```python
from corretor import GeradorRelatorio

gerador = GeradorRelatorio()
```

### Métodos

#### `gerar_relatorio_aluno(id_aluno, resultados, nome_aluno="")`

Gera relatório individual de um aluno.

```python
relatorio = gerador.gerar_relatorio_aluno(
    id_aluno="aluno_001",
    resultados=[...],
    nome_aluno="João Silva"
)
```

**Retorna:**
- `Dict`: Relatório com análises detalhadas

---

#### `gerar_relatorio_turma(alunos)`

Gera relatório consolidado de uma turma.

```python
relatorio_turma = gerador.gerar_relatorio_turma(corretor.alunos)
```

---

#### `salvar_relatorio(relatorio, caminho)`

Salva relatório em JSON.

```python
gerador.salvar_relatorio(relatorio, "output/relatorio.json")
```

---

#### `gerar_relatorio_texto(relatorio)`

Gera relatório em formato texto.

```python
texto = gerador.gerar_relatorio_texto(relatorio)
print(texto)
```

---

## Utilitários

Funções auxiliares para manipulação de dados.

### `carregar_json(caminho)`

Carrega dados de arquivo JSON.

```python
from corretor.utilitarios import carregar_json

dados = carregar_json("data/testes.json")
```

---

### `salvar_json(dados, caminho)`

Salva dados em arquivo JSON.

```python
from corretor.utilitarios import salvar_json

salvar_json({"teste": "dados"}, "output/resultado.json")
```

---

### `normalizar_resposta(resposta)`

Normaliza uma resposta para comparação.

```python
from corretor.utilitarios import normalizar_resposta

resp = normalizar_resposta("  PYTHON  ")
# Resultado: "python"
```

---

### `calcular_similaridade(texto1, texto2)`

Calcula similaridade entre dois textos (0-1).

```python
from corretor.utilitarios import calcular_similaridade

similaridade = calcular_similaridade("Python é uma linguagem", "Python é linguagem")
# Resultado: ~0.8
```

---

### `validar_nivel(nivel)`

Valida se o nível é válido.

```python
from corretor.utilitarios import validar_nivel

if validar_nivel("basico"):
    print("Nível válido")
```

---

### `calcular_pontos(acertou, dificuldade, tempo_gasto)`

Calcula pontos baseado em acerto, dificuldade e tempo.

```python
from corretor.utilitarios import calcular_pontos

pontos = calcular_pontos(acertou=True, dificuldade=2, tempo_gasto=60)
```

---

## Tipos de Dados

### Estrutura de Teste

```python
{
    "id": 1,
    "nivel": "basico",  # basico, intermediario, avancado
    "tipo": "multipla_escolha",  # multipla_escolha, verdadeiro_falso, dissertativa, numerica
    "pergunta": "O que é Python?",
    "opcoes": ["Opção A", "Opção B"],  # Para múltipla escolha
    "resposta_correta": 1,
    "explicacao": "Explicação da resposta",
    "dificuldade": 1,  # 1-5
    "palavras_chave": ["palavra1", "palavra2"],  # Opcional, para dissertativa
    "margem_erro": 0.01  # Opcional, para numérica
}
```

### Estrutura de Resultado

```python
{
    "sucesso": True,
    "id_teste": 1,
    "tipo": "multipla_escolha",
    "nivel": "basico",
    "resposta_aluno": 1,
    "resposta_correta": 1,
    "acertou": True,
    "confianca": 1.0,
    "pontos": 10,
    "tempo_gasto": 45,
    "feedback": "Parabéns!",
    "timestamp": "2024-07-21T12:00:00"
}
```

---

## Códigos de Erro

| Código | Mensagem | Solução |
|--------|----------|----------|
| 404 | Teste não encontrado | Verifique o ID do teste |
| 404 | Gabarito não encontrado | Atualize `data/gabarito.json` |
| 400 | Tipo de questão desconhecido | Use: multipla_escolha, verdadeiro_falso, dissertativa, numerica |
| 400 | Nível inválido | Use: basico, intermediario, avancado |

---

## Boas Práticas

✅ **Faça:**
- Sempre carregar testes e gabarito antes de corrigir
- Usar `id_aluno` para rastreamento de desempenho
- Salvar dados regularmente
- Validar entrada de dados

❌ **Evite:**
- Modificar testes em tempo de execução
- Usar IDs de teste duplicados
- Ignorar mensagens de erro
- Trabalhar sem ambiente virtual

---

## Suporte

Para dúvidas:
- 📖 Consulte os exemplos em `/exemplos/`
- 🐛 Abra uma issue no GitHub
- 💬 Verifique a documentação completa em `/docs/`
