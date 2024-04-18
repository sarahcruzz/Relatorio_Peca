# Importações
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# entradas dos dados
arquivo = "C:\\Users\\dsadm\\Desktop\\Relatorio_python\\dados.csv"
dados = pd.read_csv(arquivo, header=0, delimiter=';')
dados_dict = dados.to_dict('list')

# processamento dos dados
N = len(dados_dict['Diâmetro (mm)']) # Acha o número de dados
k = 1 + 3.32 * np.log10(N) # Calcula o número de bins
k = np.round(k) # Arredonda o número p/ um inteiro

# Apresentação dos dados
plt.hist(dados_dict['Diâmetro (mm)'], bins=int(k))
plt.show()
 
plt.hist(dados_dict['Altura (mm)'], bins=int(k))
plt.show()

plt.hist(dados_dict['Massa (g)'], bins=int(k))
plt.show()

plt.hist(dados_dict['Resistência (kgf)'], bins=int(k))
plt.show()

plt.hist(dados_dict['Raio (mm)'], bins=int(k))
plt.show()

plt.hist(dados_dict['Volume (mm^3)'], bins=int(k))
plt.show()

plt.hist(dados_dict['Densidade '], bins=int(k))
plt.show()

plt.hist(dados_dict['R (altura/diâmetro)'], bins=int(k))
plt.show()

plt.hist(dados_dict['Área base'], bins=int(k))
plt.show()
