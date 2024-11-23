# Importando SQLite
import sqlite3 as lite

# Importando Pandas
import pandas as pd

# Criando conexão
con = lite.connect('dados.db')

# Funções de inserção ----------------------------------------------------
# Inserir categorias
def inserir_categoria(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Categoria (nome) VALUES (?)"
		cur.execute(query, i)

#inserir_categoria(["Alimentacao"])

# Inserir receitas
def inserir_receita(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
		cur.execute(query, i)

# Inserir gastos
def inserir_gasto(i):
	with con:
		cur = con.cursor()
		query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
		cur.execute(query, i)

# Funções para deletar ----------------------------------------------------
# Deletar receitas
def deletar_receita(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Receitas WHERE id=?"
		cur.execute(query, i)

# Deletar gastos
def deletar_gasto(i):
	with con:
		cur = con.cursor()
		query = "DELETE FROM Gastos WHERE id=?"
		cur.execute(query, i)

# Funções para ver dados ----------------------------------------------------
# Ver categoria
def ver_categoria():
	lista_itens = []
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Categoria")
		linha = cur.fetchall()
		for l in linha:
			lista_itens.append(l)
	return lista_itens

print(ver_categoria())

# Ver receitas
def ver_receitas():
	lista_itens = []
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Receitas")
		linha = cur.fetchall()
		for l in linha:
			lista_itens.append(l)
	return lista_itens

print(ver_receitas())

# Ver gastos
def ver_gastos():
	lista_itens = []
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Gastos")
		linha = cur.fetchall()
		for l in linha:
			lista_itens.append(l)
	return lista_itens

print(ver_gastos())

# Função para dados da tabela
def tabela():
	gastos = ver_gastos()
	receitas = ver_receitas()

	tabela_lista = []

	for i in gastos:
		tabela_lista.append(i)

	for i in receitas:
		tabela_lista.append(i)
	
	return tabela_lista

# Função para dados do gráfico de barra
def bar_valores():
	# Receita total
	receitas = ver_receitas()
	receitas_lista = []

	for i in receitas:
		receitas_lista.append(i[3])

	receita_total = sum(receitas_lista)

	# Despesa total
	gastos = ver_gastos()
	gastos_lista = []

	for i in gastos:
		gastos_lista.append(i[3])

	gasto_total = sum(gastos_lista)

	# Saldo total
	saldo_total = receita_total - gasto_total

	return [receita_total, gasto_total, saldo_total]

# Função para dados do gráfico pie
def pie_valores():
	gastos = ver_gastos()
	tabela_lista = []

	for i in gastos:
		tabela_lista.append(i)

	dataframe = pd.DataFrame(tabela_lista, columns=['id', 'categoria', 'data', 'valor'])
	dataframe = dataframe.groupby('categoria')['valor'].sum()

	lista_quantias = dataframe.values.tolist()
	lista_categorias = []

	for i in dataframe.index:
		lista_categorias.append(i)
	
	return([lista_categorias, lista_quantias])

# Função para dados de porcentagem
def porcentagem_valor():
	# Receita total
	receitas = ver_receitas()
	receitas_lista = []

	for i in receitas:
		receitas_lista.append(i[3])

	receita_total = sum(receitas_lista)

	# Despesa total
	gastos = ver_gastos()
	gastos_lista = []

	for i in gastos:
		gastos_lista.append(i[3])

	gasto_total = sum(gastos_lista)

	# Porcentagem total
	total = ((receita_total - gasto_total) / receita_total) * 100

	return [total]