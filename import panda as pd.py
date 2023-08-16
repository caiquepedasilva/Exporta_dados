import pandas as pd
import tabula

lista_tabelas = tabula.read_pdf("lista2.pdf",pages="all")
tabelas = tabula.convert_into("lista2.pdf", "teste2.csv", output_format="csv", pages="all")
print(lista_tabelas)