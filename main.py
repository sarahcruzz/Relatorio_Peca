# # Importações
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # entradas dos dados
# arquivo = "C:\\Users\\dsadm\\Desktop\\Relatorio_Peca\\dados.csv"
# dados = pd.read_csv(arquivo, header=0, delimiter=';')
# dados_dict = dados.to_dict('list')

# # processamento dos dados
# N = len(dados_dict['Diâmetro (mm)']) # Acha o número de dados
# k = 1 + 3.32 * np.log10(N) # Calcula o número de bins
# k = np.round(k) # Arredonda o número p/ um inteiro

# # Apresentação dos dados
# plt.hist(dados_dict['Diâmetro (mm)'], bins=int(k))
# plt.show()
 
# plt.hist(dados_dict['Altura (mm)'], bins=int(k))
# plt.show()

# plt.hist(dados_dict['Massa (g)'], bins=int(k))
# plt.show()

# plt.hist(dados_dict['Resistência (kgf)'], bins=int(k))
# plt.show()

# plt.hist(dados_dict['Raio (mm)'], bins=int(k))
# plt.show()

# plt.hist(dados_dict['Volume (mm^3)'], bins=int(k))
# plt.show()

# plt.hist(dados_dict['Densidade '], bins=int(k))
# plt.show()

# plt.hist(dados_dict['R (altura/diâmetro)'], bins=int(k))
# plt.show()

# plt.hist(dados_dict['Área base'], bins=int(k))
# plt.show()

# Importações
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# entradas dos dados
arquivo = "C:\\Users\\dsadm\\Desktop\\Relatorio_Peca\\dados.csv"
dados = pd.read_csv(arquivo, header=0, delimiter=';')
dados_dict = dados.to_dict('list')

# processamento dos dados
N = len(dados_dict['Diâmetro (mm)'])  # Acha o número de dados
k = 1 + 3.32 * np.log10(N)  # Calcula o número de bins
k = np.round(k)  # Arredonda o número p/ um inteiro

# Cria um subplot com 3 linhas e 3 colunas
fig, axs = plt.subplots(3, 3, figsize=(12, 12))

# Plotagem de cada histograma em um subplot
axs[0, 0].hist(dados_dict['Diâmetro (mm)'], bins=int(k))
axs[0, 0].set_title('Diâmetro (mm)')

axs[0, 1].hist(dados_dict['Altura (mm)'], bins=int(k))
axs[0, 1].set_title('Altura (mm)')

axs[0, 2].hist(dados_dict['Massa (g)'], bins=int(k))
axs[0, 2].set_title('Massa (g)')

axs[1, 0].hist(dados_dict['Resistência (kgf)'], bins=int(k))
axs[1, 0].set_title('Resistência (kgf)')

axs[1, 1].hist(dados_dict['Raio (mm)'], bins=int(k))
axs[1, 1].set_title('Raio (mm)')

axs[1, 2].hist(dados_dict['Volume (mm^3)'], bins=int(k))
axs[1, 2].set_title('Volume (mm^3)')

axs[2, 0].hist(dados_dict['Densidade'], bins=int(k))
axs[2, 0].set_title('Densidade')

axs[2, 1].hist(dados_dict['R (altura/diâmetro)'], bins=int(k))
axs[2, 1].set_title('R (altura/diâmetro)')

axs[2, 2].hist(dados_dict['Área base'], bins=int(k))
axs[2, 2].set_title('Área base')

# Ajusta a disposição dos subplots para evitar sobreposição de títulos
plt.tight_layout()
plt.show()
