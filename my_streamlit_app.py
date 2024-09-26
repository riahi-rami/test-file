
import streamlit as st

st.title('Calculateur de recettes de café')

# Prix des articles
prix = {
    "Express": 1.4,
    "Direct": 2,
    "Cappuccino": 1.5,
    "Eau minérale 1.5L": 1.5,
    "Eau minérale 0.5L": 1,
    "Thé": 1,
    "Gazouz": 1.7
}

# Images des articles
images = {
    "Express": "Express.jpg",
    "Direct": "Direct.jpg",
    "Cappuccino": "Cappuccino.jpg",
    "Eau minérale 1.5L": "Eau minérale 1.5L.jpg",
    "Eau minérale 0.5L": "Eau minérale 0.5L.jpg",
    "Thé": "Thé.jpg",
    "Gazouz": "Gazouz.jpg"
}

# Quantités vendues
quantites = {}
gobelets = {}

for article in prix:
    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        st.image(images[article], width=100)
    with col2:
        quantites[article] = st.number_input(f"Quantité de {article} vendue :", min_value=0, value=0, key=f"qty_{article}")
    with col3:
        if article in ["Express", "Cappuccino"]:
            gobelets[article] = st.number_input(f"Avec gobelet (+0.1) :", min_value=0, value=0, key=f"gob_{article}")
        elif article == "Direct":
            gobelets[article] = st.number_input(f"Avec gobelet (+0.5) :", min_value=0, value=0, key=f"gob_{article}")

# Calcul de la recette totale
recette_totale = 0
for article in prix:
    recette_totale += prix[article] * quantites[article]
    if article in gobelets:
        if article in ["Express", "Cappuccino"]:
            recette_totale += 0.1 * gobelets[article]
        elif article == "Direct":
            recette_totale += 0.5 * gobelets[article]

# Affichage de la recette totale
st.write(f"Recette totale : {recette_totale} DT")
# Saisie de la recette réelle
recette_reelle = st.number_input("Recette réelle (somme dans la caisse) :", min_value=0.0, value=0.0)

# Calcul de la différence
difference = recette_reelle - recette_totale

# Affichage du résultat
if difference < 0:
    st.write(f"Différence : {difference} DT")
else:
    express_manquants = round(difference / prix["Express"])
    st.write(f"Résultat : {express_manquants} Express non tapés")

import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-opacity: 0.2;
    }}
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Capture..png')
