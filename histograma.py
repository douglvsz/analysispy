import pandas as pd
import matplotlib.pyplot as plt

dataTable = pd.read_csv("table.csv")

categorias = ['MASCULINO', 'FEMININO', 'OUTROS']
dataTableFilter = dataTable[dataTable['sexo'].isin(categorias)]

freqSexo = dataTableFilter['sexo'].value_counts()

plt.figure(figsize=(8, 6))
freqSexo.plot(kind='bar', color=['pink', 'blue', 'green'])
plt.title('Histograma da Distribuição dos Gêneros')
plt.xlabel('Gêneros')
plt.ylabel('Frequência')
plt.xticks(rotation=0)
plt.show()
