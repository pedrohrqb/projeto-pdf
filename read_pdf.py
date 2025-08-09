import tabula

lista_tabelas = tabula.read_pdf("resultadoogmo.pdf", pages="all")
print(len(lista_tabelas))