# Importando SQLite
import sqlite3 as lite

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