import pandas
# manipulador de base de dados

tabela = pandas.read_csv("cancelamentos.csv")
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