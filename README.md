# Análise de Evasão e Desempenho Acadêmico - Engenharia de Produção

## Descrição

Este repositório contém os scripts de análise de dados desenvolvidos para o TCC sobre evasão e desempenho acadêmico no curso de Engenharia de Produção. O estudo analisa dados de estudantes ativos e inativos no período de 2012 a 2025, utilizando técnicas de análise exploratória, clusterização e modelagem preditiva.

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── preparar_bases.py              # Processamento e limpeza dos dados brutos
├── analise_exploratoria.py        # Análise descritiva e perfil dos estudantes
├── analise_desempenho_evasao.py   # Análise de desempenho e motivos de evasão
├── analise_clustering.py          # Clusterização K-Means com PCA
├── modelagem_preditiva.py         # Regressão Logística e Random Forest
├── data/                          # Dados processados (não incluídos no repositório)
├── figures/                       # Figuras geradas pelas análises
└── tables/                        # Tabelas geradas pelas análises
```

## Dados

Os dados utilizados são provenientes do sistema acadêmico da instituição e foram **anonimizados** para preservar a privacidade dos estudantes. Todas as informações sensíveis (nomes, matrículas, emails, endereços, etc.) foram removidas.

### Bases de Dados

- **Estudantes Ativos**: Dados de estudantes matriculados
- **Estudantes Inativos**: Dados de estudantes que evadiram ou concluíram
- **Base Concatenada**: União das duas bases anteriores

### Variáveis Principais

- **IRA**: Índice de Rendimento Acadêmico
- **Porcentagem_Concluido_SIGA**: Percentual de conclusão do curso
- **Ano_Ingresso**: Ano de ingresso no curso
- **Status**: Situação atual do estudante
- **Tempo_Evasao**: Anos até a evasão (apenas para inativos)
- Indicadores socioeconômicos (PPI, renda, escola pública, PCD)

## Instalação

### Requisitos

- Python 3.8 ou superior
- pip

### Configuração do Ambiente

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd <pasta-do-repositorio>

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## Uso

### 1. Processamento dos Dados

```bash
python preparar_bases.py
```

Este script processa os dados brutos, realiza limpeza, cria variáveis derivadas e gera as bases processadas.

### 2. Análise Exploratória

```bash
python analise_exploratoria.py
```

Gera análises descritivas incluindo:
- Distribuição geográfica dos estudantes
- Perfil de gênero por coorte
- Fluxo de ingressos e desligamentos
- Indicadores socioeconômicos

### 3. Análise de Desempenho e Evasão

```bash
python analise_desempenho_evasao.py
```

Analisa:
- Desempenho acadêmico (IRA) por coorte
- Correlações entre métricas de desempenho
- Motivos de evasão
- Tempo até a evasão

### 4. Clusterização

```bash
python analise_clustering.py
```

Realiza clusterização K-Means com:
- Seleção automática de features
- Visualização PCA
- Perfil médio dos clusters
- Análise de silhouette

### 5. Modelagem Preditiva

```bash
python modelagem_preditiva.py
```

Implementa modelos de predição de evasão:
- Regressão Logística
- Random Forest
- Métricas de avaliação (Acurácia, AUC-ROC)
- Importância de variáveis

## Principais Resultados

### Taxa de Evasão

- Aproximadamente 45-50% dos estudantes evadem ao longo do curso
- Maior concentração de evasão nos primeiros 3 anos

### Fatores Preditivos

- **IRA** é o principal preditor de evasão
- **Porcentagem de conclusão** também apresenta forte correlação
- Indicadores socioeconômicos mostram influência significativa

### Clusters Identificados

A análise identificou 4 perfis principais de estudantes:
1. Alto desempenho e alto progresso
2. Desempenho médio com progresso moderado
3. Baixo desempenho em risco
4. Estudantes em início de curso

### Performance dos Modelos

- **Regressão Logística**: ~75-80% de acurácia
- **Random Forest**: ~80-85% de acurácia
- **AUC-ROC**: 0.75-0.85

## Estrutura dos Scripts

### preparar_bases.py
- Leitura dos dados brutos
- Remoção de informações sensíveis
- Padronização de nomes de colunas
- Cálculo de métricas derivadas
- Geração das bases processadas

### analise_exploratoria.py
- Perfil demográfico
- Distribuição de gênero
- Tipos de ingresso
- Indicadores socioeconômicos

### analise_desempenho_evasao.py
- Boxplots de IRA por coorte
- Análise por sexo
- Matriz de correlação
- Distribuição de motivos de evasão

### analise_clustering.py
- Seleção de features com base em missing e correlação
- K-Means com k=4
- PCA para visualização
- Análise de perfis por cluster

### modelagem_preditiva.py
- Preparação de dados (train/test split)
- Normalização de features
- Treinamento de modelos
- Avaliação com múltiplas métricas
- Análise de importância de variáveis

## Outputs

### Figuras
Todas as figuras são salvas em alta resolução (300 DPI) na pasta `figures/`:
- Distribuições geográficas
- Fluxos temporais
- Boxplots de desempenho
- Scatter plots
- Matrizes de correlação
- Visualizações de clusters
- Curvas ROC
- Matrizes de confusão

### Tabelas
Tabelas em formato Excel são salvas na pasta `tables/`:
- Resumos estatísticos
- Médias por cluster
- Loadings do PCA
- Coeficientes dos modelos
- Feature importances

## Tecnologias Utilizadas

- **Python 3.8+**
- **Pandas**: Manipulação de dados
- **NumPy**: Operações numéricas
- **Matplotlib/Seaborn**: Visualizações
- **Scikit-learn**: Machine Learning
- **Jupyter**: Desenvolvimento interativo (opcional)

## Considerações Éticas

- Todos os dados foram anonimizados
- Informações pessoais identificáveis foram removidas
- IDs numéricos aleatórios substituem identificadores reais
- O uso dos dados foi autorizado pela instituição para fins acadêmicos

## Limitações

- Análise restrita a um único curso
- Período de análise: 2012-2025
- Dados socioeconômicos disponíveis apenas para estudantes SISU

## Contribuições

Este é um projeto acadêmico desenvolvido como TCC. Sugestões e melhorias são bem-vindas através de issues ou pull requests.

## Licença

Este projeto está sob licença acadêmica. O uso dos dados está restrito a fins de pesquisa.

## Autor

Victor Hugo da Costa Fernandes - TCC Engenharia de Produção

## Agradecimentos

- Orientadores do TCC
- Instituição pela disponibilização dos dados
- Comunidade Python e open source
