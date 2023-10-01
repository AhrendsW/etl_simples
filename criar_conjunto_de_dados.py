import pandas as pd
import random
from datetime import datetime, timedelta
import os

diretorio_atual = os.path.dirname(__file__)

def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Laura', 'Bruno', 'Camila', 'Lucas', 'Larissa']
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Pereira', 'Ferreira', 'Rodrigues', 'Martins', 'Almeida', 'Lima', 'Gomes']

cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Brasília', 'Salvador', 'Curitiba', 'Recife', 'Fortaleza', 'Manaus']

cargos = ['Gerente de Soluções', 'Gerente de Equipe', 'Assessor 1', 'Assessor 2', 'Assessor 3', 'Escriturário']

data = []
for _ in range(200):
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    data_contratacao = random_date(datetime(2000, 1, 1), datetime(2021, 9, 30))
    sexo = random.choice(['Masculino', 'Feminino'])
    cidade = random.choice(cidades)
    cargo = random.choice(cargos)

    salarios = {
    'Escriturário': {'São Paulo': 8000, 'Rio de Janeiro': 8000, 'Brasília': 9000},
    'Assessor 1': {'São Paulo': 11000, 'Rio de Janeiro': 11000, 'Brasília': 12000},
    'Assessor 2': {'São Paulo': 13000, 'Rio de Janeiro': 13000, 'Brasília': 14000},
    'Assessor 3': {'São Paulo': 15000, 'Rio de Janeiro': 15000, 'Brasília': 16000},
    'Gerente de Equipe': {'São Paulo': 18000, 'Rio de Janeiro': 18000, 'Brasília': 20000},
    'Gerente de Soluções': {'São Paulo': 25000, 'Rio de Janeiro': 25000, 'Brasília': 28000},
    }

    if cargo in salarios:
        if cidade in salarios[cargo]:
            salario = salarios[cargo][cidade]
        else:
            salario = 7000  
    else:
        salario = 0  

    data.append([nome, sobrenome, data_contratacao, salario, sexo, cidade, cargo])

df = pd.DataFrame(data, columns=['Nome', 'Sobrenome', 'DataContratacao', 'Salario', 'Sexo', 'Cidade', 'Cargo'])

duplicate_indices = random.sample(range(len(df)), 10)
duplicated_data = df.iloc[duplicate_indices].copy()
duplicated_data.index = random.sample(range(len(df)), 10)
df = pd.concat([df, duplicated_data]).sort_index().reset_index(drop=True)

empty_indices = random.sample(range(len(df)), 5)
df.loc[empty_indices, 'Salario'] = None
df.loc[empty_indices, 'Sexo'] = None

caminho_arquivo_csv = os.path.join(diretorio_atual, 'fonte_dados.csv')

df.to_csv(caminho_arquivo_csv, sep=';', encoding='utf-8', index=False)
