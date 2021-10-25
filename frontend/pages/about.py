import streamlit as st
from components.styles import *
from components.functions import * 

def about(texto, site, email, linkedin, twitter, instagram, github, youtube, style_a, style_div4, style_div5, style_div8, style_div9, style_nome, style_p, style_image):

  texto = describe_cidamo(texto,site,email,linkedin,twitter,instagram,github, youtube, style_a, style_div4, style_div5)
  st.markdown(texto, True)

  st.markdown("## Responsáveis pelo projeto:")

  k = describe_people("Kally Chung", kally_is, "https://github.com/chunggnuhc", "https://www.linkedin.com/in/kally-chung/",  style_div8,style_div9, style_nome,style_p, style_a,style_image, "https://avatars.githubusercontent.com/u/6722874?v=4")
  st.markdown(k, True)

  l = describe_people("Leonel Fernandes", leonel_is, "https://github.com/LeoFernanndes","https://www.linkedin.com/in/leonel-fernandes-balbino-288705ba/", style_div8,style_div9, style_nome, style_p,style_a,style_image, "https://avatars.githubusercontent.com/u/58197167?v=4")
  st.markdown(l, True)

  r = describe_people("Rogério Mainardes", rogerio_is, "https://github.com/RogerioOMDS", "https://www.linkedin.com/in/rogerioomds/",style_div8,style_div9, style_nome,style_p, style_a,style_image, "https://avatars.githubusercontent.com/u/63982716?v=4")
  st.markdown(r, True)
