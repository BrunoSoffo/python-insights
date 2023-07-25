import pandas as pd
import plotly.express as px

# manipulador de base de dados

tabela = pd.read_csv("cancelamentos.csv")
print(tabela)

tabela = tabela.dropna()
#remove linhas com algum campo n preenchido
print(tabela.info())
#exibe as informações de preenchimento e propriedades da tabela

tabela = tabela.drop("CustomerID", axis = 1)
#axis = 1 ---- coluna
#axis = 0 ---- linha
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))
#Conta quantos valores foram preenchidos

print(tabela["duracao_contrato"].value_counts())
print(tabela["duracao_contrato"].value_counts(normalize=True))

print(tabela.groupby("duracao_contrato").mean())
print(tabela.groupby("assinatura").mean())

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
#fazendo a análise dos dados sem os contratos mensais
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True))

display(tabela["assinatura"].value_counts(normalize=True))
display(tabela.groupby("assinatura").mean(numeric_only=True))

grafico = px.histogram(tabela, x="assinatura", color="cancelou")
grafico.show()