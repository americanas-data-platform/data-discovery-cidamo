import streamlit as st
from components.styles import *
from components.functions import * 

def comparation(js1, colunas1, coluna1, tipagem1, js2, colunas2, coluna2, tipagem2, col1, col2, style_div, style_p):

  indice1 = colunas1.index(coluna1)
  indice2 = colunas2.index(coluna2)

  lista1 = column_describer(js1, tipagem1, indice1, coluna1, col1, style_div, style_p, "Dataset 1")

  lista2 = column_describer(js2, tipagem2, indice2, coluna2, col2, style_div, style_p, "Dataset 2")

  co = comparation_values(lista1, lista2, coluna1, coluna2, col1, col2)

  comparation_plots(lista1, lista2, coluna1, coluna2, co)
