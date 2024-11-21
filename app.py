import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def charger_donnees(fichier):
    return pd.read_csv(fichier)

donnees = charger_donnees(r"C:\Users\Ariska\Desktop\python\BeansDataSet.csv")

st.title("Analyse des données Beans and Pods")

st.subheader("Affichage des données")
if st.checkbox("Afficher le dataset complet"):
    st.write(donnees)

st.subheader("Statistiques descriptives")
if st.checkbox("Afficher les statistiques descriptives"):
    st.write(donnees.describe())

st.subheader("Analyse d'une colonne spécifique")
colonne = st.selectbox("Sélectionnez une colonne :", donnees.columns[2:])  # Colonnes numériques

if colonne:
    st.write(f"Statistiques pour la colonne {colonne} :")
    st.write(donnees[colonne].describe())

    st.subheader(f"Distribution des valeurs pour {colonne}")
    fig, ax = plt.subplots()
    donnees[colonne].hist(ax=ax, bins=20)
    ax.set_title(f"Histogramme de {colonne}")
    ax.set_xlabel(colonne)
    ax.set_ylabel("Fréquence")
    st.pyplot(fig)

st.subheader("Comparaison entre plusieurs colonnes")
colonnes_a_comparer = st.multiselect("Sélectionnez les colonnes à comparer :", donnees.columns[2:])

if len(colonnes_a_comparer) > 1:
    st.write("Graphique comparatif :")
    st.line_chart(donnees[colonnes_a_comparer])

st.markdown("""
### Aoudia Fahem
""")
