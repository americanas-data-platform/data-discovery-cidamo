import requests
import streamlit as st
from PIL import Image
from components.styles import *
from components.functions import *
from pages.home import home
from pages.comparation import comparation
from pages.about import about

st.set_page_config( 
    page_title = 'Data Quality',
    page_icon = '✅',
    layout = 'wide'
)

# Coletando o nome de todos os datasets
url = "http://localhost/api/v1/summaries/"
req = requests.get(url)
json_data = req.json()

lista_datasets = []
for k in range(len(json_data)):
  name = json_data[k]["filename"]
  lista_datasets.append(name)

logo = Image.open("images/LOGO_DATA.png")
st.sidebar.image(logo)
st.sidebar.markdown("# Menu inicial")
page = st.sidebar.radio("Selecione a página",["Introdução", "Data Quality", "Comparações", "Sobre"])



if page == "Introdução":
  st.header("Seja bem vindo ao Data Quality.")
  
  st.subheader("Projeto fruto de uma parceria Americanas - SA com CiDAMO.")

  col1, col2 = st.columns([1,1])
  col1.write("Aqui vai uma imagem")

  col2.write("Aqui vai outra imagem")










elif page == 'Data Quality':

  ## SIDEBAR ##
  st.sidebar.markdown("# Datasets")

  selected_dataset = st.sidebar.selectbox("Selectione seu dataset", lista_datasets)
  st.sidebar.markdown("# Selecione os tipos de variaveis: ")

  categorical_check = st.sidebar.checkbox("Categóricas")
  discrete_check = st.sidebar.checkbox("Discretas")
  continuous_check = st.sidebar.checkbox("Contínuas")
  datetime_check = st.sidebar.checkbox("Data/Hora")
  
  url = f"http://localhost/api/v1/summaries/{selected_dataset}"

  home(url, categorical_check, discrete_check, continuous_check, datetime_check, style_div, style_div3, style_div7, style_h1_2, style_h1_3, style_p)


elif page == 'Comparações':

  explicacao = describe_comparacoes(exp,style_div10,style_p)
  st.markdown(explicacao, True)

  js1 = request_dataset(lista_datasets, "Primeiro dataset", "Dataset 1") 
  colunas1, tipagem1 = dataset_selection(js1)
  coluna1 = st.selectbox("Selecione a coluna do primeiro dataset:", colunas1, key= "coluna1")

  js2 = request_dataset(lista_datasets, "Segundo dataset", "Dataset 2")
  colunas2, tipagem2 = dataset_selection(js2)
  coluna2 = st.selectbox("Selecione a coluna do segundo dataset:", colunas2, key= "coluna2")

  col1, col2 = st.columns([1,1])

  comparation(js1, colunas1, coluna1, tipagem1, js2, colunas2, coluna2, tipagem2, col1, col2, style_div, style_p)


elif page == "Sobre":


  st.header("Sobre o projeto")

  image = Image.open("images/cidamo.jpg")

  c1,c2,c3 = st.columns([1,3,1])
  c2.image(image)

  about(texto, site, email, linkedin, twitter, instagram, github, youtube, style_a, style_div4, style_div5, style_div8, style_div9, style_nome, style_p, style_image)




