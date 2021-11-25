##############################################################################
##############################################################################
#                                                                            #
#                         Importation des librairies                         #
#                                                                            #
##############################################################################
##############################################################################
import streamlit as st
#from streamlit import caching

#-----------------------------------#
# general
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

#-----------------------------------#
# plotly
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import iplot, plot
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
## fixer le theme
import plotly.io as pio
pio.templates.default = 'ggplot2'


##############################################################################
##############################################################################
#                                                                            #
#                         Définition des fonctions                           #
#                                                                            #
##############################################################################
##############################################################################

##############################################################################
# Fonction principale :
# permet d'afficher les différentes pages
##############################################################################
def main():
    PAGES = {
        "Accueil": page1,
        "Label Ville Amie des Animaux 🐶": page2,
        #"Exploration des données : \n Réduction de dimension" : page2_1,
        #"Prédiction du DQR": page3,
        #"Prédiciton du DQR : Amélioration des modèles" : page4
        #"Clustering" : page10
        #"Références - Liens" : page50
    }

    st.sidebar.title('Navigation 🧭')
    page = st.sidebar.radio("", list(PAGES.keys()))
    PAGES[page]()
    
    
        
##############################################################################
# Fonctions correspondant aux différentes pages
##############################################################################


#==============================   Page 1  ===================================#
#===============================  Accueil  ==================================#
def page1():
    st.title('App Open Data')
    st.write("##")
    st.write("""
             Bienvenue !
             
             Application qui présente quelques réutilisations de données open data.
             
             
             """)


#==============================   Page 2  ====================================#
#========================  Label Ville Amie des Animaux  ==========================#
def page2():
                 
    st.title('Label Ville Amie des Animaux 🐶')
    st.write("##")
    
    dataset = pd.read_csv("datasets/label-ville-amie-des-animaux.csv", delimiter=';')

    fig = px.scatter_mapbox(dataset, lat="latitude", lon="longitude", 
                        hover_name="commune", 
                        hover_data={"distinction" : True,
                                   "latitude" : False,
                                    "longitude" : False},
                        color="distinction",
                        color_discrete_sequence=px.colors.qualitative.Bold,
                        #zoom=3, 
                        height=600, width=900,
                        mapbox_style='carto-positron'
                       )

    fig.update_layout(
        hoverlabel=dict(
        bgcolor="white",
        font_size=12,
#       font_family="Rockwell"
        )
        )   
    st.write(fig)


             
#########################################################
if __name__=="__main__":
    main()
 