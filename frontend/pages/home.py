import requests
import streamlit as st
from components.styles import *
from components.functions import * 



def home(url, 
         categorical_check, 
         discrete_check, 
         continuous_check, 
         datetime_check, 
         style_div, 
         style_div3, 
         style_div7, 
         style_h1_2, 
         style_h1_3, 
         style_p):

  ## HOME ##
  r = requests.get(url)
  js = r.json()

  # st.json(js)

  # Salva os dicionarios
  name = js["filename"]
  categorical = js["categorical_features"]
  discrete = js["discrete_features"]
  continuous = js["continuous_features"]
  datetime = js["datetime_features"]

  # cria os titulos coloridos
  cat = title_variable("Categóricas", style_div3, style_h1_2)
  disc = title_variable("Discretas", style_div3, style_h1_2)
  cont = title_variable("Contínuas", style_div3, style_h1_2)
  datet = title_variable("Data/Hora", style_div3, style_h1_2)

  # titulo do dataset
  title = title_variable(f"{name}", style_div7, style_h1_3)
  st.markdown(title, True)

  # Categorica
  if categorical_check:
    setor_variable(categorical, cat, style_div, style_p, describe_cat_disc_variable, table_cat_disc_generator)

  # Discreta
  if discrete_check:
    setor_variable(discrete, disc, style_div, style_p, describe_cat_disc_variable, table_cat_disc_generator)

  # # Continua
  if continuous_check:
    setor_variable_2(continuous, cont, style_div, style_p, describe_cont_datet_variable, table_cont_datet_generator)

  # Datetime
  if datetime_check:
    setor_variable_2(datetime, datet, style_div, style_p, describe_cont_datet_variable, table_cont_datet_generator, tipo = "datetime")