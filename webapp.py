import streamlit as st
import pandas as pd
from backend import exctracter

# Titre de l'application
st.title("Bank Profit Navigator")
st.write("Extraction de mesures financières cruciales à partir de rapports financiers.")

num_banques = st.number_input("Nombre de banques", min_value=1, step=1)

banques_info = {
        'Nom de la banque': [],
        'Trimestre': [],
        'Année': []}

for i in range(num_banques):
    st.sidebar.header(f"Banque {i + 1}")
    nom_banque = st.sidebar.text_input(f"Nom de la banque {i + 1}",value="JP Morgan Chase")
    trimestre = st.sidebar.number_input(f"Trimestre {i + 1}", min_value=1, max_value=4, step=1)
    annee = st.sidebar.number_input(f"Année {i + 1}", min_value=1900, max_value=2100, step=1, value=2023)
    
    banques_info['Nom de la banque'].append(nom_banque)

    banques_info['Trimestre'].append(trimestre)

    banques_info['Année'].append(annee)

user_prompt = str(banques_info)

if st.button("Créer le CSV"):
    try :
        payload = exctracter(user_prompt)
        csv_file=pd.read_json(payload).to_csv(index=False)
        st.success("Le fichier banques_data.csv a été créé avec succès!")
        st.download_button(
            label="Télécharger CSV",
            data=csv_file,
            file_name='donnees_bancaires.csv',
            key='csv_button'
        )
    except:
        st.error("La création du fichier a échoué")
