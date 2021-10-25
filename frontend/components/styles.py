
style_a = 'text-align: left; color: #666666; font-size: 1rem; text-decoration:none;font-family: Arial;'
style_p = 'text-align: left; color: #666666; font-size: 1.2vw'
style_h1_2 = 'text-align: center; color: white; font-size: 2.3vw;font-family: Arial;'
style_h1_3 = 'text-align: center; color: white; font-size: 3.0vw;font-family: Arial;'
style_div = 'box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); border-radius: 5px; margin-top: 0.5%; border-top: 10%; padding: 7%;'
style_div2 = 'box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); border-radius: 2px; padding: 10px; margin-top: 10px; padding-left: 10%; '
style_div3 = 'box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin-top: 20px; margin-bottom: 20px; border-top: 20px; background-color: #e60014; border-radius: 2px'
style_div4 = 'font-size: 3.0vw; font-family: Arial; margin-bottom:0px; padding-bottom:0px; border-bottom:0px'
style_div5 = 'text-align: center; font-size: 1rem; font-family: Arial;font-weight:400; margin-top:0px; padding-top:0px;'
style_div7 = 'box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); margin-top: 10px; margin-bottom: 10px; border-top: 20px; background-color: #1893f8; border-radius: 5px; padding: 8px;'
style_div8 = 'box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); border-radius: 5px; margin-top: 2%; border-top: 10%; padding: 2%; display:flex'
style_div9 = 'border-radius: 5px; margin-top: 5%; margin-left: 2%; border-top: 10%; padding: 1%;'
style_div10 = 'box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); border-radius: 5px; margin-top: 0%; margin-bottom:3%; border-top: 0%; padding: 2%;'
style_image = 'padding: 0.01%; margin: 1px; border-radius: 5px; border: 1px;  height: 15vw'
style_nome = 'text-align: left; color: #666666; font-size: 1.6vw'

texto = """O CiDAMO é um grupo de estudo, pesquisa e desenvolvimento nas áreas de Ciência de Dados, Aprendizagem de Máquina e Otimização. Foi fundado em 2019 pelos professores Abel Soares Siqueira e Lucas Garcia Pedroso do departamento de matemática da UFPR com o finalidade inicial de reunir pessoas com interesse em estudar Ciência de Dados, Aprendizagem de Máquina e Otimização.
Com o amadurecimento e o crescimento do grupo, o CiDAMO tem trabalhado com os objetivos de produzir pesquisa de ponta em temas multidisciplinares, de capacitar e aperfeiçoar a próxima geração de profissionais nas áreas relacionadas à ciência de dados e otimização, além de fortalecer a relação entre a academia e o mercado de trabalho por meio de troca de conhecimentos e crescimento mútuo.
Desde então, diversos eventos (meetups e o CiDWeek) e seleção de novos integrantes foram feitos para alcançar os objetivos propostos. 
Para acompanhar mais sobre o grupo CiDAMO e seus eventos: """

site = "http://cidamo.com.br/"
email = "grupo.cidamo@gmail.com"
linkedin = "https://www.linkedin.com/company/grupo-cidamo/"
twitter = "https://twitter.com/grupo_cidamo"
instagram = "https://www.instagram.com/grupo.cidamo/"
github = "https://github.com/CiDAMO"
youtube = "https://www.youtube.com/channel/UCiVFjGGCh63QZ3-kswfQdRw"

exp = """<h4>Comparações de duas variáveis:</h4>
        Nesta sessão é possível fazer comparações entre as variaveis de duas tabelas que você selecionar para isso, selecione os datasets no menu do lado esquerdo, e em seguida selecione também quais as variáveis que você deseja comparar nos seletores abaixo.
        <br>
        <br>
        ATENÇÃO: As tabelas de correlação, covariância e o gráfico de dispersão ao final dessa página usam somente informações dos top 10 valores mais presentes em cada uma das variáveis que você está comparando.
        """

introducao1 = """ 
Este é um projeto que surgiu de uma parceria entre Americanas - SA e o Grupo CiDAMO (Ciência de Dados, Aprendizagem de Máquina e Otimização).

Essencialmente este projeto tem como intuito a criação de uma ETL completa a partir da base de dados do [Kaggle: Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce).

<h2>Como funciona:</h2>

No lado esquerdo desta página, tem o *Menu inicial*, que será usado para a navegação das páginas desta aplicação. A funcionalidade das páginas seguem explicadas a seguir:


<h3>Data Quality</h3>

O Data Quality consiste na essência deste trabalho. No menu lateral, primeiramente selecione o dataset a ser analisado a partir da lista dos datasets disponibilizados. Escolhido o seu dataset, basta marcar quais os tipo de variáveis que você deseja analisar em tela:

"""


introducao2 = """

Escolhido o dataset e os tipos de variáveis, na tela ao lado são exibidas as estatísticas das variáveis deste dataset que correspondem aos tipo selecionado.

Logo abaixo do título com o tipo de variável, tem um quadro com o resumo de todas as variáveis desde tipo no dataset. E logo em seguida, apresentam-se as estatíscas de cada variável em detalhe.

Independente do tipo de variável, sempre serão mostradas o *tamanho* do conjunto de dados (quantidade de linhas), o *tipo* da variável dentro da aplicação e quantidade de *valores nulos*. Em relação aos gráficos, serão mostrados os top 10 valores mais frequentes. Para visualizar os 10 valores menos frequentes, clicar na opção do *Gráficos adicionais* no canto superior a direita do gráfico.

Já para cada tipo de variável, são informadas medidas estatísticas diferentes. No caso de variáveis de contínuas ou data/hora, são exibidos os quartis, o valor máximo e mínimo.
"""



introducao3 = """
O gráfico ao lado das medidas estatísticas é interativo, isto é, você pode utilizando o scroll dar zoom em diferentes regiões do gráfico. Além disso, é possível clicar, arrastar e deixando o mouse em cima, dar uma descrição mais específica do valor atribuído para a coluna.

Note ainda que existe um check de 'Gráficos adicionais', e marcando ele são apresentadas outros gráficos em relação a esta variável.

<h3>Comparações</h3>

A sessão de comparações tem como intuito observar as informações de duas variáveis distintas simultâneamente, sendo tanto ou do mesmo dataset ou de dois diferentes.

Ao selecionar esta seção, no Menu lateral são disponibilizadas duas caixas seletoras para a escolha dos datasets. Escolhidos estes, em tela são disponibilizados outras duas caixas seletoras para a seleção das respectivas variáveis dos datasets anteriormente selecionado.

Escolhidas as variáveis para cada dataset, são mostradas as informações completas sobre estas (tal como era realizado no Data Quality na sessão anterior) bem como são disponibilizadas algumas informações simples de cruzamento entre os top 10 valores das duas.
"""



introducao4 = """
Tem-se então as tabelas de correlação e covariância entre as duas variáveis selecionadas, e ainda um gráfico que exibe a contagem simultânea dos 10 valores mais frequentes.


<h3>Sobre</h3>

Finalmente, na ultima sessão, é possível conhecer mais sobre o grupo CiDAMO e os integrantes do grupo que se envolveram neste projeto.

Navegar nesta sessão e se conectar aos responsáveis pelo projeto no Linkedin faz parte da experiência do Data Discovery! ;)
"""


kally_is = """ 
Kally Chung é analista de dados e agregada do grupo CiDAMO. Formada em Matemática Aplicada Computacional pela UNICAMP e embora tenha trabalhado por 5 anos na área da Educação na UFPR, há 2 anos tem trabalhado como analista de dados.
"""

rogerio_is = """ 
Rogerio Mainardes ingressou no grupo CiDAMO em 2020. Formado em Matemática pela UFPR, além de professor de Matemática de nível Ensino Médio também atua no mercado como Cientista de Dados. 
"""

leonel_is = """ 
Leonel é um estudante de Engenharia Mecânica com gosto particular por processos, dados e qualidade que atualmente atua como desenvolvedor backend.
"""