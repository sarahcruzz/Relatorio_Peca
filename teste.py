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

df = pd.DataFrame(dados)
# Excluir linhas com valores NaN de Resistência (kgf)
df = df.dropna(subset=['Resistência (kgf)'])
# Calcular a função R (altura/diâmetro) apenas para os índices válidos
R = df['Altura (mm)'] / df['Diâmetro (mm)']
# Criar uma figura e uma grade de subplots com 2 linhas e 2 colunas
fig, axs = plt.subplots(2, 2, figsize=(12, 10))


# Gráfico de dispersão: Resistência versus Diâmetro
axs[0, 0].scatter(df['Diâmetro (mm)'], df['Resistência (kgf)'])
axs[0, 0].set_xlabel('Diâmetro (mm)')
axs[0, 0].set_ylabel('Resistência (kgf)')
axs[0, 0].set_title('Resistência das peças em função do Diâmetro')


# Gráfico de dispersão: R (altura/diâmetro) versus Resistência
axs[1, 0].scatter(R, df['Resistência (kgf)'])
axs[1, 0].set_xlabel('R (Altura/Diâmetro)')
axs[1, 0].set_ylabel('Resistência (kgf)')
axs[1, 0].set_title('Resistência das peças em função de R')
# Boxplot da Resistência


axs[0, 1].boxplot(df['Densidade'])
axs[0, 1].set_ylabel('Densidade')
axs[0, 1].set_title('Boxplot das Densidades das peças')


# Boxplot da Resistência
axs[1, 1].boxplot(df['Resistência (kgf)'])
axs[1, 1].set_ylabel('Resistência (kgf)')
axs[1, 1].set_title('Boxplot da Resistência das peças')


# (3) Processamento dos dados
#Cálculo do quatis
Q1 = np.percentile(dados_dict['Resistência (kgf)'], 25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados_dict['Resistência (kgf)'], 50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados_dict['Resistência (kgf)'], 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1 #cálculo da distância inter-quartil

#cálculo dos limites
x1 = min(dados_dict['Resistência (kgf)']) #menor valor de dados
xn = max(dados_dict['Resistência (kgf)']) #menor valor de dados
LI = max(x1, Q1 - 1.5*DQ)
LS = min(xn, Q3 + 1.5*DQ)

# (4) Apresentação dos resultados
print("Quartis:", Q1, "|", Q2 ,"|", Q3)
print("Limite inferior:", LI)
print("Limite superior:", LS)

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Mostrar todos os gráficos
plt.show()

 