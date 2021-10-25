import streamlit as st
import pandas as pd
import altair as alt
import requests


@st.cache
def title_variable(variable, style_div, style_h1):
  html = f"""
  <div style = '{style_div}'>
    <h1 style = '{style_h1}'>
      {variable}
    </h1>
  </div>
  """
  return html

@st.cache
def describe_cat_disc_variable(variable, style_div, style_p):
  lista_html = []
  for i in range(len(variable)):
    var = variable[i]
    perc_null = round(float(var['na_count']) * 100 / float(var['size']),2)
    html = f"""
    <div style = '{style_div}'>
      <p style = '{style_p}'>Tamanho: {var['size']}</p>
      <p style = '{style_p}'>Valores nulos: {var['na_count']} ({perc_null}%)</p>
      <p style = '{style_p}'>Tipo: {var['type']}</p>
    </div>
    """
    lista_html.append(html)
  return lista_html


@st.cache
def describe_cont_datet_variable(variable, style_div, style_p):
  lista_html = []
  for i in range(len(variable)):
    var = variable[i]
    perc_null = round(float(var['na_count']) * 100 / float(var['size']),2)
    html = f"""
    <div style = '{style_div}'>
      <p style = '{style_p}'>Tamanho: {var['size']}</p>
      <p style = '{style_p}'>Valores nulos: {var['na_count']} ({perc_null}%)</p>
      <p style = '{style_p}'>Tipo: {var['type']}</p>
      <p style = '{style_p}'>Valor mínimo: {var['min']}</p>
      <p style = '{style_p}'>Quartil - 25%: {var['quantile_25']}</p>
      <p style = '{style_p}'>Quartil - 50%: {var['quantile_50']}</p>
      <p style = '{style_p}'>Quartil - 75%: {var['quantile_75']}</p>
      <p style = '{style_p}'>Valor máximo: {var['max']}</p>
    </div>
    """
    lista_html.append(html)
  return lista_html


@st.cache
def describe_cat_disc_variable_comparation(var, style_div, style_p):
  perc_null = round(float(var['na_count']) * 100 / float(var['size']),2)
  html = f"""
  <div style = '{style_div}'>
    <p style = '{style_p}'>Nome: {var['name']}</p>
    <p style = '{style_p}'>Tamanho: {var['size']}</p>
    <p style = '{style_p}'>Valores nulos: {var['na_count']} ({perc_null}%)</p>
    <p style = '{style_p}'>Tipo: {var['type']}</p>
  </div>
  """
  return html


@st.cache
def describe_cont_datet_variable_comparation(var, style_div, style_p):
  perc_null = round(float(var['na_count']) * 100 / float(var['size']),2)
  html = f"""
  <div style = '{style_div}'>
    <p style = '{style_p}'>Name: {var['name']}</p>
    <p style = '{style_p}'>Tamanho: {var['size']}</p>
    <p style = '{style_p}'>Valores nulos: {var['na_count']} ({perc_null}%)</p>
    <p style = '{style_p}'>Tipo: {var['type']}</p>
    <p style = '{style_p}'>Valor mínimo: {var['min']}</p>
    <p style = '{style_p}'>Quartil - 25%: {var['quantile_25']}</p>
    <p style = '{style_p}'>Quartil - 50%: {var['quantile_50']}</p>
    <p style = '{style_p}'>Quartil - 75%: {var['quantile_75']}</p>
    <p style = '{style_p}'>Valor máximo: {var['max']}</p>
  </div>
  """
  return html


@st.cache
def table_cat_disc_generator(variable):
  df = pd.DataFrame()
  for i in range(len(variable)):
    df.loc[i, "nome"] = variable[i]["name"]
    df.loc[i, "tamanho"] = variable[i]["size"]
    df.loc[i, "nulos"] = variable[i]["na_count"]
    df.loc[i, "tipo"] = variable[i]["type"]
  return df

@st.cache
def table_cont_datet_generator(variable):
  df = pd.DataFrame()
  for i in range(len(variable)):
    df.loc[i, "nome"] = variable[i]["name"]
    df.loc[i, "tamanho"] = variable[i]["size"]
    df.loc[i, "nulos"] = variable[i]["na_count"]
    # df.loc[i, "tipo"] = variable[i]["type"]
    df.loc[i, "min"] = variable[i]["min"]
    df.loc[i, "25%"] = variable[i]["quantile_25"]
    df.loc[i, "50%"] = variable[i]["quantile_50"]
    df.loc[i, "75%"] = variable[i]["quantile_75"]
    df.loc[i, "max"] = variable[i]["max"]
  return df


def setor_variable(variable, title, style_div, style_p, describe_function, table_function):
  describe = describe_function(variable, style_div = style_div, style_p = style_p)
  st.markdown(title, True)

  resumo = st.expander("Resumo")
  table = table_function(variable)
  resumo.table(table)

  for j in range(len(describe)):
    container = st.container()
    name = variable[j]["name"]
    container.markdown(f"<h2>{name}</h2>", True)

    l1,l2,l3,l4 = container.columns([1,1,1,1])
    col1, col2 = container.columns([1,3])

    col1.markdown(describe[j], True)
    col1.markdown("##")

    keys = list(variable[j]["count_top10"].keys())
    values = list(variable[j]["count_top10"].values())
    dados = pd.DataFrame({f"Top 10": keys , "contagem":values})
    g = alt.Chart(dados).mark_bar().encode(
                                            y = alt.Y(f"Top 10", sort="-x"), 
                                            x = alt.X("contagem"), 
                                            tooltip = [f"Top 10", "contagem"]).configure_mark(color = "#1893f8").interactive()
    col2.altair_chart(g, use_container_width = True)

    if l4.checkbox("Gráficos adicionais", key = f"{name}"):

      keys = list(variable[j]["count_down10"].keys())
      values = list(variable[j]["count_down10"].values())
      dados = pd.DataFrame({f"Down 10": keys , "contagem":values})
      g = alt.Chart(dados).mark_bar().encode(
                                              y = alt.Y(f"Down 10", sort="-x"), 
                                              x = alt.X("contagem"), 
                                              tooltip = [f"Down 10", "contagem"]).configure_mark(color = "#1893f8").interactive()
      col2.altair_chart(g, use_container_width = True)


def setor_variable_2(variable, title, style_div, style_p, describe_function, table_function, tipo = ""):
  describe = describe_function(variable, style_div = style_div, style_p = style_p)
  st.markdown(title, True)


  resumo = st.expander("Resumo")
  table = table_function(variable)
  resumo.table(table)

  for j in range(len(describe)):
    container = st.container()
    name = variable[j]["name"]
    container.markdown(f"<h2>{name}</h2>", True)

    l1,l2,l3,l4 = container.columns([1,1,1,1])
    col1, col2 = container.columns([1,3])

    col1.markdown(describe[j], True)
    col1.markdown("##")

    if tipo == "datetime":
      keys = list(variable[j]["histogram"]["value_counts"].keys())
      values = list(variable[j]["histogram"]["value_counts"].values())
      dados = pd.DataFrame({f"{name}": keys , "contagem":values})
      dados[f"{name}"] = pd.to_datetime(dados[f"{name}"]).dt.strftime("%Y-%m-%d %H:%M:%S")
      dados.sort_values("contagem", ascending = False, inplace = True) 
      g = alt.Chart(dados).mark_bar().encode(
                                              y = alt.Y(f"{name}", sort = "-x"), 
                                              x = alt.X("contagem"), 
                                              tooltip = [f"{name}", "contagem"]).configure_mark(color = "#1893f8").interactive()
      col2.altair_chart(g, use_container_width = True)

    else:
      keys = list(variable[j]["histogram"]["value_counts"].keys())
      keys2 = [str(round(float(e),2)) for e in keys]
      values = list(variable[j]["histogram"]["value_counts"].values())
      dados = pd.DataFrame({f"{name}": keys2, "contagem":values})
      dados.sort_values("contagem", ascending = False, inplace = True) 
      g = alt.Chart(dados).mark_bar().encode(
                                              x = alt.X(f"{name}", sort = "-y"), 
                                              y = alt.Y("contagem"), 
                                              tooltip = [f"{name}", "contagem"]).configure_mark(color = "#1893f8").interactive().configure_axisX(labelAngle=330)
      col2.altair_chart(g, use_container_width = True)

    if l4.checkbox("Gráficos adicionais", key = f"{name}"):

      keys = list(variable[j]["count_top10"].keys())
      values = list(variable[j]["count_top10"].values())
      dados = pd.DataFrame({f"Top 10": keys , "contagem":values})
      g = alt.Chart(dados).mark_bar().encode(
                                              y = alt.Y("Top 10", sort = "-x"), 
                                              x = alt.X("contagem"), 
                                              tooltip = [f"Top 10", "contagem"]).configure_mark(color = "#1893f8").interactive()
      col2.altair_chart(g, use_container_width = True)


      keys = list(variable[j]["count_down10"].keys())
      values = list(variable[j]["count_down10"].values())
      dados = pd.DataFrame({f"Down 10": keys , "contagem":values})
      g = alt.Chart(dados).mark_bar().encode(
                                              y = alt.Y("Down 10", sort = "-x"), 
                                              x = alt.X("contagem"), 
                                              tooltip = [f"Down 10", "contagem"]).configure_mark(color = "#1893f8").interactive()
      col2.altair_chart(g, use_container_width = True)

def dataset_selection(js):
  colunas = []
  tipagem = []
  for key in (list(js.keys())[2:]):
    for i in range(len(js[key])):
      colunas.append(js[key][i]["name"])
      tipagem.append(key)

  return [colunas, tipagem]


def column_describer(js, tipagem, indice, coluna, col, style_div, style_p, title):
  lista = []
  for i in js[tipagem[indice]]:
    if i["name"]==coluna:
      if ((tipagem[indice] == "categorical_features") or (tipagem[indice] == "discrete_features")):
        var = describe_cat_disc_variable_comparation(i, style_div, style_p)
        col.markdown(f"#### {title}")
        col.markdown(var, True)
        col.markdown("##")
        lista.append(list(i["count_top10"].values()))

      elif ((tipagem[indice] == "continuous_features") or (tipagem[indice] == "datetime_features")):
        var = describe_cont_datet_variable_comparation(i, style_div, style_p)
        col.markdown(f"#### {title}")
        col.markdown(var, True)
        col.markdown("##")
        lista.append(list(i["count_top10"].values()))
    
    else: pass

  return lista

def request_dataset(lista_datasets, qual_dataset, title):
  st.sidebar.markdown(f"# {title}")
  dataset = st.sidebar.selectbox(f"{qual_dataset}:", lista_datasets)
  url = f"http://localhost/api/v1/summaries/{dataset}"
  r = requests.get(url)
  return r.json()

def comparation_plots(lista1, lista2, coluna1, coluna2, co):
  co_plot = pd.melt(co.reset_index(), id_vars = ['index'], value_vars = [coluna1, coluna2])
  co_plot.columns = ["indice", "colunas","valores"]
  co_plot["Top 10"] = co_plot["indice"].map({i: f"Top {i+1}" for i in range(10)})

  comparation_values_plot = alt.Chart(co_plot).mark_circle(color = "#1893f8").encode(
    alt.X("Top 10:N", sort = "-y"), 
    alt.Y(f"valores"), 
    color = alt.Color("colunas", scale = alt.Scale(range=["#1893f8","#e60014"])),  tooltip = ["Top 10", "valores"]).interactive().configure_circle(size = 500).configure_axisX(labelAngle=0)
  st.altair_chart(comparation_values_plot, use_container_width=True)

def comparation_values(lista1, lista2, coluna1, coluna2, col1, col2):
  co = pd.DataFrame({coluna1: lista1[0], coluna2: lista2[0]})

  col1.markdown("#### Correlação (Top 10)")
  corr = co.corr()
  col1.dataframe(corr.style.highlight_min(axis=0, color = "#A3CEF9"))
  col1.markdown("##")

  col2.markdown("#### Covariância (Top 10)")
  cov = co.cov()
  col2.dataframe(cov.style.highlight_max(axis=0, color = "#A3CEF9"))
  col2.markdown("##")

  return co


def describe_cidamo(texto,site,email,linkedin,twitter,instagram,github, youtube, style_a, style_div4, style_div5):

  html = f"""
  <div style = '{style_div4}'>
    <p>{texto}</p>
  </div> 
  <div style = '{style_div5}'>
    <a style = '{style_a}' href = '{site}' target="_blank" > site </a>
    <span style = 'font-size:1.4vw'> | <span>
    <a style = '{style_a}' href = '{email}' target="_blank" > email </a>
    <span style = 'font-size:1.4vw'> | <span>
    <a style = '{style_a}' href = '{linkedin}' target="_blank" > linkedin </a>
    <span style = 'font-size:1.4vw'> | <span>
    <a style = '{style_a}' href = '{twitter}' target="_blank" > twitter </a>
    <span style = 'font-size:1.4vw'> | <span>
    <a style = '{style_a}' href = '{instagram}' target="_blank" > instagram </a>
    <span style = 'font-size:1.4vw'> | <span>
    <a style = '{style_a}' href = '{github}' target="_blank" > github </a>
    <span style = 'font-size:1.4vw'> | <span>
    <a style = '{style_a}' href = '{youtube}' target="_blank" > youtube </a>
  </div> 
  """
  return html

def describe_people(nome,descricao, git, linkedin, style_div, style_div9, style_nome, style_p, style_a, style_image, image):
  html = f"""
  <div style = '{style_div}'>
    <img src='{image}' style = '{style_image}'/>
    <div style = '{style_div9}'>
      <p style = '{style_nome}'><b> {nome} </b> </p>
      <p style = '{style_p}'>{descricao}</p>
      <a style = '{style_a}' href = '{git}' target="_blank" > <b> Github </b> </a>
      <span> | </span>
      <a style = '{style_a}' href = '{linkedin}' target="_blank" > <b> Linkedin </b> </a>
    </div>
  </div>
  """
  return html

def describe_comparacoes(texto, style_div, style_p):
  html = f""" 
  <div style = '{style_div}'>
    <p style = '{style_p}'>{texto}</p>
  </div>
  """
  return html