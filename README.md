# Análise de Evasão e Desempenho Acadêmico - Engenharia de Produção

## Descrição

Análise de dados desenvolvida para TCC sobre evasão e desempenho acadêmico no curso de Engenharia de Produção. Utiliza dados de estudantes (2012-2025) com técnicas de análise exploratória, clusterização e modelagem preditiva.

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── preparar_bases.py                  # Processamento e limpeza dos dados brutos
├── analise_exploratoria.ipynb         # Análise descritiva e perfil dos estudantes
├── analise_desempenho_evasao.ipynb    # Análise de desempenho e motivos de evasão
├── analise_clustering.ipynb           # Clusterização K-Means com PCA
├── modelagem_preditiva.ipynb          # Regressão Logística e Random Forest
├── figures/                           # Figuras geradas (PNG, 300 DPI)
└── tables/                            # Tabelas geradas (Excel)
```

## Dados

Dados provenientes do sistema acadêmico, **anonimizados** para preservar a privacidade dos estudantes.

**Bases:** Estudantes ativos, inativos e base concatenada.

**Variáveis principais:** IRA, porcentagem concluída, ano de ingresso, status, tempo de evasão, indicadores socioeconômicos (PPI, renda, escola pública, PCD).

## Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd analise_desempenho_curso

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## Uso

### 1. Processar Dados

```bash
python preparar_bases.py
```

### 2. Executar Análises

Abra e execute os notebooks Jupyter na ordem:

1. **analise_exploratoria.ipynb**: Perfil demográfico, distribuição de gênero, tipos de ingresso, indicadores socioeconômicos
2. **analise_desempenho_evasao.ipynb**: IRA por coorte, correlações, motivos e tempo de evasão
3. **analise_clustering.ipynb**: K-Means (k=4), PCA, perfis de clusters
4. **modelagem_preditiva.ipynb**: Regressão Logística e Random Forest para predição de evasão


## Tecnologias

- Python 3.8+
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook

## Considerações Éticas

Dados anonimizados, sem informações pessoais identificáveis. Uso autorizado pela instituição para fins acadêmicos.

## Autor

Victor Hugo da Costa Fernandes - TCC Engenharia de Produção
