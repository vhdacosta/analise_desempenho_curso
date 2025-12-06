import pandas as pd
import numpy as np

RAW_ATIVOS = r'Estudantes_ativos_EP_CCET_2025.1.xlsx'
PROCESSED_ATIVOS = r'Estudantes_ativos_EP_2025.xlsx'

RAW_INATIVOS = r'Relação de Alunos Inativos EP.csv'
PROCESSED_INATIVOS = r'Estudantes_inativos_EP_2025.xlsx'

PROCESSED_CONCAT = r'Estudantes_EP_2025_concat.xlsx'

colunas_comuns_ativos = [
    'Id', 'Sexo', 'Cidade', 'Estado', 'Nacionalidade',
    'Início_Vínculo', 'Matriz_Curricular', 'Tipo_Ingresso',
    'Ano_Ingresso', 'Período_Ingresso', 'Perfil', 'Status',
    'IRA', 'Media_Aprovadas', 'Media_Total',
    'Ponderada_Aprovadas', 'Ponderada_Total',
    'Numero_Horas_Exigidas_Curso', 'Numero_Horas_Inscritas_Resultado',
    'Numero_Horas_Inscritas_Periodo_Atual',
    'Horas_Aprovadas',
    'Porcentagem_Concluido_SIGA', 'Porcentagem_Inscrito',
    'Porcentagem_Aprovado', 'Porcentagem_Reprovado',
    'ano_conclusao_ensino_medio',
]

colunas_comuns_inativos = colunas_comuns_ativos + [
    'Ano_Egresso', 'Periodo_Egresso', 'Tempo_Evasao',
]


ativos_columns = [
    'Id (aleatório)', 'Sexo', 'Cor/Raça', 'Naturalidade', 'sigla',
    'Início Vínculo',
    'Matriz Curricular',
    'Ingresso', 'Ingresso-Ano', 'Ingresso-Período', 'IRA', 'perfil',
    'Média das Aprovadas', 'Ponderada das Aprovadas', 'Média Total',
    'Ponderada Total',
    'Porcentagem concluído',
    'Status',
    'Nota SISU', 'Modalidade SISU', 'Descrição Modalidade SISU', 'ensino_medio',
    'Nacionalidade',
    'Número de Horas Exigidas no Curso',
    'Número de Horas Inscritas com Resultado',
    'Número de Horas Inscritas no Período Atual',
    'ano_conclusao_ensino_medio',
]

inativos_columns = [
    'Id (aleatório)', 'Sexo', 'Naturalidade', 'sigla',
    'Início Vínculo',
    'Matriz Curricular',
    'Ingresso', 'Ingresso-Ano', 'Ingresso-Período', 'IRA', 'perfil',
    'Média das Aprovadas', 'Ponderada das Aprovadas', 'Média Total',
    'Ponderada Total',
    'Status',
    'Ano Egresso', 'Período Egresso',
    'Nacionalidade',
    'Número de Horas Inscritas com Resultado',
    'Número de Horas Inscritas no Período Atual',
    'Número de Horas Reprovadas', 'Número de Horas Canceladas', 'Número de Horas Desistentes',
    'ano_conclusao_ensino_medio',
]

inativos_columns_sensitive_drop = [
    'Matricula', 'Nro UFSCar', 'Nome Civil', 'Nome Social',
    'E-mail', 'Email alternativo', 'Tipo de Nacionalidade',
    'Endereço', 'Telefone',
]


def process_ativos():
    ativos = pd.read_excel(RAW_ATIVOS)
    ativos = ativos[ativos_columns].copy()

    padrao = {
        'Id (aleatório)': 'Id',
        'Sexo': 'Sexo',
        'Cor/Raça': 'Raça',
        'Naturalidade': 'Cidade',
        'sigla': 'Estado',
        'Início Vínculo': 'Início_Vínculo',
        'Matriz Curricular': 'Matriz_Curricular',
        'Ingresso': 'Tipo_Ingresso',
        'Ingresso-Ano': 'Ano_Ingresso',
        'Ingresso-Período': 'Período_Ingresso',
        'IRA': 'IRA',
        'perfil': 'Perfil',
        'Média das Aprovadas': 'Media_Aprovadas',
        'Ponderada das Aprovadas': 'Ponderada_Aprovadas',
        'Média Total': 'Media_Total',
        'Ponderada Total': 'Ponderada_Total',
        'Porcentagem concluído': 'Porcentagem_Concluido_SIGA',
        'Status': 'Status',
        'Nota SISU': 'Nota_SISU',
        'Modalidade SISU': 'Modalidade_SISU',
        'Descrição Modalidade SISU': 'Descricao_Modalidade_SISU',
        'ensino_medio': 'Ensino_Medio',
        'Nacionalidade': 'Nacionalidade',
        'Número de Horas Exigidas no Curso': 'Numero_Horas_Exigidas_Curso',
        'Número de Horas Inscritas com Resultado': 'Numero_Horas_Inscritas_Resultado',
        'Número de Horas Inscritas no Período Atual': 'Numero_Horas_Inscritas_Periodo_Atual',
    }

    ativos = ativos.rename(columns=padrao)

    for col in ativos.select_dtypes(include="object"):
        ativos[col] = ativos[col].astype(str).str.strip()

    num_cols = [
        "IRA", "Media_Aprovadas", "Ponderada_Aprovadas", "Media_Total",
        "Ponderada_Total", "Porcentagem_Concluido_SIGA", "Nota_SISU",
        "Numero_Horas_Exigidas_Curso", "Numero_Horas_Inscritas_Resultado",
        "Numero_Horas_Inscritas_Periodo_Atual",
    ]
    for col in num_cols:
        if col in ativos.columns:
            ativos[col] = pd.to_numeric(ativos[col], errors="coerce")

    de_para_modalidade_sisu_binario = {
        '1':  {"Pessoa_PPI": 1, "Renda_Superior_1_5": 0, "EM_Escola_Publica": 0, "PCD": 0},
        '2':  {"Pessoa_PPI": 0, "Renda_Superior_1_5": 0, "EM_Escola_Publica": 0, "PCD": 0},
        '3':  {"Pessoa_PPI": 1, "Renda_Superior_1_5": 1, "EM_Escola_Publica": 0, "PCD": 0},
        '4':  {"Pessoa_PPI": 0, "Renda_Superior_1_5": 1, "EM_Escola_Publica": 0, "PCD": 0},
        '5':  {"Pessoa_PPI": 0, "Renda_Superior_1_5": 1, "EM_Escola_Publica": 0, "PCD": 0},
        '12': {"Pessoa_PPI": 1, "Renda_Superior_1_5": 1, "EM_Escola_Publica": 0, "PCD": 1},
        '13': {"Pessoa_PPI": 0, "Renda_Superior_1_5": 1, "EM_Escola_Publica": 0, "PCD": 1},
        '17': {"Pessoa_PPI": 1, "Renda_Superior_1_5": 0, "EM_Escola_Publica": 1, "PCD": 0},
        '20': {"Pessoa_PPI": 0, "Renda_Superior_1_5": 0, "EM_Escola_Publica": 1, "PCD": 0},
        '21': {"Pessoa_PPI": 1, "Renda_Superior_1_5": 1, "EM_Escola_Publica": 1, "PCD": 0},
    }

    modalidade_ativos = pd.DataFrame.from_dict(de_para_modalidade_sisu_binario, orient='index')
    ativos = ativos.merge(modalidade_ativos, how='left', left_on='Modalidade_SISU', right_index=True)

    ativos["Horas_Totais_Consideradas"] = (
        ativos["Numero_Horas_Inscritas_Resultado"].fillna(0)
        + ativos["Numero_Horas_Inscritas_Periodo_Atual"].fillna(0)
    )

    def arredondar_proximo_multiplo_30(valor):
        return np.ceil(valor / 30) * 30

    ativos["Horas_Pendentes"] = arredondar_proximo_multiplo_30(
        abs(
            (ativos["Porcentagem_Concluido_SIGA"] * ativos["Numero_Horas_Exigidas_Curso"] / 100)
            - ativos["Numero_Horas_Exigidas_Curso"]
        )
        - ativos["Numero_Horas_Inscritas_Periodo_Atual"].fillna(0)
    )

    ativos["Porcentagem_Inscrito"] = (
        ativos["Horas_Totais_Consideradas"] / ativos["Numero_Horas_Exigidas_Curso"]
    ) * 100

    ativos["Horas_Excedentes"] = np.where(
        ativos["Horas_Totais_Consideradas"] > ativos["Numero_Horas_Exigidas_Curso"],
        ativos["Horas_Totais_Consideradas"] - ativos["Numero_Horas_Exigidas_Curso"],
        0,
    )

    ativos["Horas_Aprovadas"] = ativos["Horas_Totais_Consideradas"] - ativos["Horas_Excedentes"]

    ativos["Porcentagem_Aprovado"] = np.where(
        ativos["Horas_Totais_Consideradas"] > 0,
        (ativos["Horas_Totais_Consideradas"] - ativos["Horas_Excedentes"])
        / ativos["Horas_Totais_Consideradas"] * 100,
        np.nan,
    )

    ativos["Porcentagem_Reprovado"] = np.where(
        ativos["Horas_Totais_Consideradas"] > 0,
        ativos["Horas_Excedentes"] / ativos["Horas_Totais_Consideradas"] * 100,
        np.nan,
    )

    ativos["Porcentagem_Aprovado"] = ativos["Porcentagem_Aprovado"].round(2)
    ativos["Porcentagem_Reprovado"] = ativos["Porcentagem_Reprovado"].round(2)
    ativos["Porcentagem_Inscrito"] = ativos["Porcentagem_Inscrito"].round(2)

    colunas_ordenadas_ativos = [
        "Id", "Sexo", "Raça", "Cidade", "Estado", "Nacionalidade",
        "Início_Vínculo", "Matriz_Curricular", "Tipo_Ingresso",
        "Ano_Ingresso", "Período_Ingresso", "Perfil", "Status",
        "IRA", "Media_Aprovadas", "Media_Total",
        "Ponderada_Aprovadas", "Ponderada_Total",
        "Numero_Horas_Exigidas_Curso", "Numero_Horas_Inscritas_Resultado",
        "Numero_Horas_Inscritas_Periodo_Atual", "Horas_Totais_Consideradas",
        "Horas_Aprovadas", "Horas_Pendentes", "Horas_Excedentes",
        "Porcentagem_Concluido_SIGA", "Porcentagem_Inscrito",
        "Porcentagem_Aprovado", "Porcentagem_Reprovado",
        "Pessoa_PPI", "Renda_Superior_1_5", "EM_Escola_Publica", "PCD",
        "Ensino_Medio", "Modalidade_SISU", "Descricao_Modalidade_SISU",
        "Nota_SISU",
        "ano_conclusao_ensino_medio",
    ]

    ativos = ativos[[c for c in colunas_ordenadas_ativos if c in ativos.columns]]

    ativos.to_excel(PROCESSED_ATIVOS, index=False)
    return ativos


def process_inativos():
    inativos = pd.read_csv(RAW_INATIVOS, sep=";")

    inativos = inativos.drop(columns=inativos_columns_sensitive_drop, errors="ignore")

    inativos['Id (aleatório)'] = range(1, len(inativos) + 1)

    inativos = inativos[inativos_columns].copy()

    rename_map = {
        "Id (aleatório)": "Id",
        "Sexo": "Sexo",
        "Naturalidade": "Cidade",
        "sigla": "Estado",
        "Início Vínculo": "Início_Vínculo",
        "Matriz Curricular": "Matriz_Curricular",
        "Ingresso": "Tipo_Ingresso",
        "Ingresso-Ano": "Ano_Ingresso",
        "Ingresso-Período": "Período_Ingresso",
        "IRA": "IRA",
        "perfil": "Perfil",
        "Média das Aprovadas": "Media_Aprovadas",
        "Ponderada das Aprovadas": "Ponderada_Aprovadas",
        "Média Total": "Media_Total",
        "Ponderada Total": "Ponderada_Total",
        "Status": "Status",
        "Ano Egresso": "Ano_Egresso",
        "Período Egresso": "Periodo_Egresso",
        "Nacionalidade": "Nacionalidade",
        "Número de Horas Inscritas com Resultado": "Numero_Horas_Inscritas_Resultado",
        "Número de Horas Inscritas no Período Atual": "Numero_Horas_Inscritas_Periodo_Atual",
        "Número de Horas Reprovadas": "Numero_Horas_Reprovadas",
        "Número de Horas Canceladas": "Numero_Horas_Canceladas",
        "Número de Horas Desistentes": "Numero_Horas_Desistentes",
    }

    inativos = inativos.rename(columns=rename_map)

    for col in inativos.select_dtypes(include="object"):
        inativos[col] = inativos[col].astype(str).str.strip()

    num_cols_inativos = [
        "Ano_Ingresso", "Ano_Egresso", "Periodo_Ingresso", "Periodo_Egresso",
        "IRA", "Numero_Horas_Inscritas_Resultado", "Numero_Horas_Inscritas_Periodo_Atual",
        "Numero_Horas_Reprovadas", "Numero_Horas_Canceladas", "Numero_Horas_Desistentes",
    ]
    for col in num_cols_inativos:
        if col in inativos.columns:
            inativos[col] = pd.to_numeric(inativos[col], errors="coerce")

    inativos["Tempo_Evasao"] = inativos["Ano_Egresso"] - inativos["Ano_Ingresso"]
    inativos = inativos[inativos["Tempo_Evasao"].between(0, 20)]

    matriz_map = {
        '2005/1': 3930,
        '2010/1': 3930,
        '2019/1': 3810,
    }

    def calcular_horas_obrigatorias(matriz):
        return matriz_map.get(matriz, None)

    inativos['Numero_Horas_Exigidas_Curso'] = inativos['Matriz_Curricular'].map(calcular_horas_obrigatorias)

    inativos['Horas_Aprovadas'] = (
        inativos['Numero_Horas_Inscritas_Resultado']
        - (
            inativos['Numero_Horas_Reprovadas'].fillna(0)
            + inativos['Numero_Horas_Canceladas'].fillna(0)
            + inativos['Numero_Horas_Desistentes'].fillna(0)
        )
    )

    inativos['Porcentagem_Concluido_SIGA'] = np.where(
        inativos['Numero_Horas_Exigidas_Curso'] > 0,
        inativos['Horas_Aprovadas'] / inativos['Numero_Horas_Exigidas_Curso'] * 100,
        np.nan,
    )

    inativos['Porcentagem_Inscrito'] = np.where(
        inativos['Numero_Horas_Exigidas_Curso'] > 0,
        inativos['Numero_Horas_Inscritas_Resultado'] / inativos['Numero_Horas_Exigidas_Curso'] * 100,
        np.nan,
    )

    inativos['Porcentagem_Aprovado'] = np.where(
        inativos['Numero_Horas_Inscritas_Resultado'] > 0,
        inativos['Horas_Aprovadas'] / inativos['Numero_Horas_Inscritas_Resultado'] * 100,
        np.nan,
    )

    inativos['Porcentagem_Reprovado'] = np.where(
        inativos['Numero_Horas_Inscritas_Resultado'] > 0,
        100 - inativos['Porcentagem_Aprovado'],
        np.nan,
    )

    inativos['Porcentagem_Concluido_SIGA'] = inativos['Porcentagem_Concluido_SIGA'].round(2)
    inativos['Porcentagem_Inscrito'] = inativos['Porcentagem_Inscrito'].round(2)
    inativos['Porcentagem_Aprovado'] = inativos['Porcentagem_Aprovado'].round(2)
    inativos['Porcentagem_Reprovado'] = inativos['Porcentagem_Reprovado'].round(2)

    colunas_ordenadas_inativos = [
        "Id", "Sexo", "Cidade", "Estado", "Nacionalidade",
        "Início_Vínculo", "Matriz_Curricular", "Tipo_Ingresso",
        "Ano_Ingresso", "Período_Ingresso", "Perfil", "Status",
        "IRA", "Media_Aprovadas", "Media_Total",
        "Ponderada_Aprovadas", "Ponderada_Total",
        "Ano_Egresso", "Periodo_Egresso", "Tempo_Evasao",
        "Numero_Horas_Exigidas_Curso", "Numero_Horas_Inscritas_Resultado",
        "Numero_Horas_Inscritas_Periodo_Atual",
        "Numero_Horas_Reprovadas", "Numero_Horas_Canceladas", "Numero_Horas_Desistentes",
        "Horas_Aprovadas",
        "Porcentagem_Concluido_SIGA", "Porcentagem_Inscrito",
        "Porcentagem_Aprovado", "Porcentagem_Reprovado",
        "ano_conclusao_ensino_medio",
    ]

    inativos = inativos[[c for c in colunas_ordenadas_inativos if c in inativos.columns]]

    inativos.to_excel(PROCESSED_INATIVOS, index=False)
    return inativos


ativos = process_ativos()
inativos = process_inativos()

concat = pd.concat([ativos, inativos], ignore_index=True)
concat = concat[[c for c in colunas_comuns_inativos if c in concat.columns]]

concat = concat.sample(frac=1, random_state=42).reset_index(drop=True)

concat['Id'] = range(1, len(concat) + 1)

concat['Início_Vínculo'] = pd.to_datetime(concat['Início_Vínculo'], errors='coerce').dt.strftime('%Y-%m-%d')
concat['Matriz_Curricular'] = concat['Matriz_Curricular'].astype(str).str.replace('2019-01-01 00:00:00', '2019/1').str.replace('2010-01-01 00:00:00', '2010/1').str.replace('2005-01-01 00:00:00', '2005/1')

print(f"Ativos: {len(ativos)}")
print(f"Inativos: {len(inativos)}")
print(f"Concat: {len(concat)}")

concat.to_excel(
    PROCESSED_CONCAT,
    index=False,
)
