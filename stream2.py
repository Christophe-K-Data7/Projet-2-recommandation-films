import streamlit as st
import pandas as pd
import base64
import requests
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np
import time 

def main():
    # Lecture des données
    df_final = pd.read_csv("df_final.csv")

    # Fonction pour rechercher un film par son nom
    def search_movie(title):
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "d6e046b00186d5cc2135e145fb7af15e",  # Votre clé API TMDb
            "query": title
        }
        response = requests.get(url, params=params)
        return response.json()

    # Définir le style CSS global
    set_global_styles()

    # Définir l'image de fond pour la barre latérale
    side_bg = "affiche.jpg"
    set_sidebar_background(side_bg)

    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choisissez une page", ["Accueil", "Présentations Ali & Son's", "Soirée en tête à tête avec...", "Un genre, mille plaisirs", "Mon film, mon aventure","Durée idéale pour s'évader"])

    if page == "Accueil":
        show_home()
    elif page == "Présentations Ali & Son's":
        show_page1()
    elif page == "Soirée en tête à tête avec...":
        show_page2(df_final)  # Passez df_final en argument à show_page2
    elif page == "Un genre, mille plaisirs":
        show_page3(df_final)  # Passez df_final en argument à show_page3
    elif page == "Mon film, mon aventure":
        show_page4(df_final)  # Passez df_final en argument à show_page4
    elif page == "Durée idéale pour s'évader":
        show_page5(df_final)  # Passez df_final en argument à show_page5
def set_global_styles():
    # CSS pour l'image de fond de la barre latérale et la couleur de fond du contenu principal
    side_bg = "affiche.jpg"
    side_bg_ext = 'data:image/jpg;base64,{}'.format(base64.b64encode(open(side_bg, "rb").read()).decode())
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #F6DEB9;
        }}
        .css-1d391kg {{
            background-image: url("{side_bg_ext}");
            background-size: cover;
        }}
        .st-bb {{
            background-color: rgba(246, 222, 185, 0.5);
        }}
        </style>
    """, unsafe_allow_html=True)

def progress_bar_animation():
    # Centrer verticalement et horizontalement la barre de progression
    col1, col2, col3 = st.columns([1, 2, 1])

    # Espacement pour centrer verticalement
    col1.write("")
    col3.write("")

    # Barre de progression au centre
    with col2:
        progress_bar = st.progress(0)

    # Styles CSS pour rendre la barre de progression transparente
    st.markdown(
        """
        <style>
        .stProgress > div > div {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Fonction pour simuler une tâche longue
    def simulate_long_task():
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.05)  # Simulation d'une tâche longue

    # Appeler la fonction de simulation
    simulate_long_task()

def show_home():
    title_html = """
    <h1 style="text-align: center;">
        Bienvenue sur la page officielle<br>
        <span style="display: inline-block; margin-top: 10px;">d'Ali & Son's</span>
    </h1>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    # Intégrer un fichier audio MP3 en boucle
   # st.audio("https://ia804508.us.archive.org/20/items/keys-of-moon-the-epic-hero/KeysOfMoon-TheEpicHero.mp3", format="audio/mpeg", start_time=0, loop=True)

    # Intégrer un fichier vidéo MP4 local et le faire tourner en boucle
    #with open('7989632-uhd_2160_4096_25fps.mp4', 'rb') as video_file:
     #   video_bytes = video_file.read()
      #  st.video(video_bytes, format='video/mp4', start_time=0, loop=True)

    

def show_page1():
    st.title("Présentations Ali & Son's")
    markdown_text = """
    ## 🎥 Pourquoi Ali & Son's ?

    Parce que nous savons que regarder un film, c'est bien plus qu'une simple activité de loisir. C'est une aventure, un moment de détente, et parfois même une leçon de vie. Et tout ça, nous le faisons avec un soupçon d'humour, beaucoup de pop-corn et une grande dose de passion !

    ## 🍿 Nos Équipements :

    - **Écran XXL** : Si grand qu'on pourrait y voir passer un troupeau de moutons !
    - **Son Dolby Atmos** : Tellement immersif que vous entendrez les oiseaux chanter même pendant un film d'horreur.
    - **Fauteuils Ultra-Confort** : Réputés pour être plus confortables que le canapé de votre grand-mère, et ça, c'est pas peu dire !

    ## 🎬 Notre Sélection de Films :
    Des blockbusters aux films d'auteurs, en passant par les comédies locales et les documentaires animaliers (parce qu'on sait que les vaches aiment aussi le cinéma), il y en a pour tous les goûts.

    ## 🍦 Côté Gourmandises :
    Notre stand de friandises est une attraction à lui seul. Pop-corn, bonbons, glaces, et même quelques spécialités locales pour ravir vos papilles. Parce qu'un film sans grignoter, c'est comme la Creuse sans ses champs verdoyants, ça manque de saveur !

    ## 👨‍👩‍👧‍👦 Chez Ali & Son's, tout le monde est le bienvenu :
    Que vous soyez venu en famille, entre amis, ou en solitaire pour une session de ciné-thérapie, vous trouverez toujours un accueil chaleureux chez nous. Et n'oubliez pas notre mascotte, Gustave le sanglier, toujours prêt pour une séance photo à l'entrée du cinéma !

    Alors, n'attendez plus, venez faire un tour chez Ali & Son's. Ici, le cinéma, c'est plus qu'un loisir, c'est un véritable spectacle !

    ## 📅 Horaires : 
    Ouvert tous les jours, même quand il pleut des cordes (et en Creuse, on sait que ça arrive souvent !)

    ## 📍 Adresse : 
    En plein centre-ville, impossible de nous manquer (juste suivez les panneaux avec Gustave le sanglier)

    ## Ali & Son's : 
    Le cinéma où l'on rit, où l'on pleure, et où l'on vit des moments inoubliables, au cœur de la Creuse. 🎉

    Venez nombreux, et n'oubliez pas : chez Ali & Son's, le pop-corn est toujours chaud et l'humour toujours au rendez-vous !
    """
    st.markdown(markdown_text)

def show_page2():
    st.title("Système de recommandation avec l'acteur favori")

    markdown_text = """
    
    🎬 Quel est votre acteur préféré ?

    Chez Ali & Son's, nous croyons que chaque film devient encore plus magique grâce aux talents exceptionnels des acteurs. 🎥

    Dites-nous, quel acteur fait battre votre cœur et illumine vos écrans ? 🌟

    Partagez avec nous le nom de votre acteur préféré et découvrez des recommandations de films spécialement sélectionnées pour vous ! 🍿✨
    
    """
    st.markdown(markdown_text)

input_acteur = st.text_input('Quel est votre acteur favori ? :')

if input_acteur:
    films_de_lacteur = df_final[df_final['primaryName'] == input_acteur]
    films_de_lacteur_unique = films_de_lacteur.drop_duplicates(subset=['primaryTitle'])

    if len(films_de_lacteur_unique) > 0:
        random_films_acteur = films_de_lacteur_unique.sample(n=3)
        st.write(f"Voici trois films dans lesquels {input_acteur} a joué :")
        for i, film in random_films_acteur.iterrows():
            st.write(film['primaryTitle'])
    else:
        st.write(f"Aucun film trouvé pour l'acteur {input_acteur}.")

def show_page3():
    st.title("Un genre, mille plaisirs")

    markdown_text = """
    🎬 Quel est votre genre de film préféré ?

    Chez Ali & Son's, nous savons que chacun a ses propres goûts cinématographiques. 🎥

    Que vous soyez amateur de comédies hilarantes, de thrillers palpitants, de drames émouvants ou de science-fiction captivante, nous voulons tout savoir ! 🌟

    Partagez avec nous votre genre de film préféré et laissez-nous vous recommander des pépites cinématographiques qui vous feront vibrer. 🍿✨
    """
    st.markdown(markdown_text)
    
    input_genre = st.text_input('Quel genre de film aimez-vous ? :')

    if input_genre:
        genre_souhaite = df_final[df_final['genres'].str.contains(input_genre, case=False, na=False)]
        genre_souhaite_unique = genre_souhaite.drop_duplicates(subset=['primaryTitle'])

        if len(genre_souhaite_unique) > 0:
            random_films = genre_souhaite_unique.sample(n=3)
            st.write(f"Voici trois films du genre {input_genre} :")
            for i, film in random_films.iterrows():  
                st.write(film['primaryTitle'])
        else:
            st.write(f"Aucun film trouvé pour le genre {input_genre}.")

def show_page4():
    st.title("Mon film, mon aventure")

    markdown_text = """
    🎬 Quel est le titre de votre film préféré ?

    Chez Ali & Son's, nous adorons connaître les coups de cœur cinématographiques de nos visiteurs ! 🌟

    Dites-nous, quel est le film qui vous a le plus marqué, fait rire, pleurer ou rêver ? 🎥

    Partagez avec nous le titre de votre film préféré et laissez-nous vous surprendre avec des recommandations personnalisées ! 🍿✨
    """
    st.markdown(markdown_text)

    df_final = pd.read_csv("df_final.csv")

    # Pour remplacer les NaN par 0 dans le get dummies 
    df_final = df_final.fillna(0)

    # Demande d'entrée utilisateur
    input_film = st.text_input('Entrez le titre de votre film préféré :').lower()

    if st.button("Rechercher"):
        if input_film:
            movie_data = search_movie(input_film)
            if movie_data["total_results"] > 0:
                first_movie = movie_data["results"][0]
                # Affichez les détails du film
        st.write("Titre:", first_movie["title"])
        st.write("Année de sortie:", first_movie["release_date"])
        st.write("Description:", first_movie["overview"])
                # Vérifiez si l'affiche du film est disponible
        if first_movie["poster_path"]:
                    # Construisez l'URL de l'affiche
            poster_url = f"https://image.tmdb.org/t/p/w500{first_movie['poster_path']}"
                    # Affichez l'affiche
            st.image(poster_url, caption="Affiche du film", use_column_width=True)
        else:
                st.write("Affiche non disponible")
    else:
        st.write("Aucun résultat trouvé pour ce titre")

    if input_film:


#Regrouper les films par titre pour éviter les doublons
#regroupe les données par titre de film et calcule la moyenne des autres lignes pour éviter les doublons, puis reinitialise l'index
        #df_final = df_final.groupby('primaryTitle').mean().reset_index()

        numeric_columns = df_final.select_dtypes(include=['int64', 'float64']).columns.tolist()
        numeric_columns.append('primaryTitle')
        df_final = df_final[numeric_columns].groupby('primaryTitle').mean().reset_index()
#df_final[numeric_columns] = df_final[numeric_columns].apply(pd.to_numeric, errors='coerce')
#df_final = df_final.groupby('primaryTitle').mean().reset_index()

#Sélectionner les lignes numériques
        X = df_final.select_dtypes(include = 'number')

#Normalisation - Préparation des données pour le modèle k-Means
        scaler = StandardScaler().fit(X)
        X_scaled = scaler.transform(X)

#Créer le modèle K-means avec 20 clusters pour avoir des gros groupes
        kmeans = KMeans(n_clusters=20)
        kmeans.fit(X_scaled)

#Caractéristiques du film d'entrée
#On ne prend en compte dans les caractéristiques que les données numériques du film donné en input
    caracteristiques_film = df_final[df_final['primaryTitle'].str.lower() == input_film].select_dtypes(include = 'number')

#Vérifier que les caractéristiques du film donné ne sont pas vides
    if not caracteristiques_film.empty:
    # Applique la même transformation au film donné en input
        caracteristiques_film_scaled = scaler.transform(caracteristiques_film)
    # Prédit le groupe auquel appartient le film entré en input puis récupère le premier élément
        cluster_input_film = kmeans.predict(caracteristiques_film_scaled)[0]

    # Trouver les films dans le même groupe que le film donné
        films_meme_groupe = df_final[kmeans.labels_ == cluster_input_film]

    # Sélectionner 3 films aléatoires dans le même cluster que le film donné (à l'exclusion du film donné)
    # Détermine le nombre maximal de films similaires à afficher dans le groupe, en limitant à 3 films au maximum.
        num_similaires = min(3, len(films_meme_groupe) - 1)
    # Vérifie s'il y a au moins un film similaire dans le même groupe
        if num_similaires > 0:
        # Sélectionne aléatoirement les indices des films similaires dans le groupe
            indices_similaires = np.random.choice(films_meme_groupe.index, num_similaires, replace=False)
        # Sélectionne les noms des films similaires dans le groupe en utilisant les indices sélectionnés
            similar_films = films_meme_groupe.loc[indices_similaires, 'primaryTitle']
            print(f"Les films similaires à {input_film} dans le même cluster sont :")
        # Parcourt les noms des films similaires dans le groupe
            for i, similar_film in enumerate(similar_films):
            # Affiche le nom du film similaire, en commençant par 1, suivi du nom du film ainsi de suite
                print(f"{i+1}. {similar_film}")
        else:
            print(f"Aucun film similaire à {input_film} n'a été trouvé dans le même cluster.")
#Si film inscrit en input pas trouvé dans le df
    else:
        print(f"Le film '{input_film}' n'a pas été trouvé dans la base de données.")

    
def show_page5():
    st.title("Durée idéale pour s'évader")

    markdown_text = """ 
    🎬 Combien de temps avez-vous pour un bon film ?

    Chez Ali & Son's, nous savons que chaque minute compte. ⏰

    Que vous ayez juste une petite heure ou tout un après-midi à consacrer à une séance de cinéma, nous avons le film parfait pour vous ! 🌟

    Dites-nous combien de temps vous souhaitez consacrer à votre film, et laissez-nous vous surprendre avec des recommandations adaptées. 🍿✨
    """
    st.markdown(markdown_text)

    df_final = pd.read_csv("df_final.csv")

    # Pour remplacer les NaN par 0 dans le get dummies 
    df_final = df_final.fillna(0)

    # Demande d'entrée utilisateur pour la durée souhaitée du film
    input_temps = st.number_input("Quelle durée souhaitez-vous accorder à votre film aujourd'hui ? (en minutes) :", min_value=0, max_value=500, step=10)

    if input_temps > 0:
        # Regrouper les films par titre pour éviter les doublons
        df_final_unique = df_final.groupby('primaryTitle').mean().reset_index()

        # Gérer les valeurs manquantes
        df_final_unique = df_final_unique.fillna(df_final_unique.mean())

        # Sélectionner les lignes numériques
        X = df_final_unique.select_dtypes('number').drop(columns=['runtimeMinutes'])

        # Normalisation - Préparation des données pour le modèle de Régression Linéaire 
        scaler = StandardScaler().fit(X)
        X_scaled = scaler.transform(X)

        # Entraînement du modèle de régression linéaire
        modelLR = LinearRegression().fit(X_scaled, df_final_unique['runtimeMinutes'])

        # Prédire les durées de films à partir de la variable X normalisée 
        predicted_durations = modelLR.predict(X_scaled)

        # Création d'une nouvelle colonne avec les prédictions du runtimeMinutes
        df_final_unique['predicted_runtimeMinutes'] = predicted_durations

        # Filtrer les films dont la durée prédite est proche du nombre mis en input
        tolerance = 10  # Tolérance de 10 minutes
        films_filtres = df_final_unique[np.abs(df_final_unique['predicted_runtimeMinutes'] - input_temps) <= tolerance]

        # Vérifier que les caractéristiques de durée de film ne sont pas vides
        if not films_filtres.empty:
            st.write(f"Les films qui ont une durée approximative de {input_temps} minutes sont :")
            num_similaires = min(3, len(films_filtres))
            random_indices = np.random.choice(films_filtres.index, num_similaires, replace=False)
            for i, idx in enumerate(random_indices):
                similar_film = films_filtres.loc[idx, 'primaryTitle']
                poster_path = df_final.loc[df_final['primaryTitle'] == similar_film, 'poster_path'].iloc[0]
                poster_url = f"https://image.tmdb.org/t/p/w780/{poster_path}"
                st.write(f"{i+1}. {similar_film}")

                if isinstance(poster_url, str):  # Vérifier si poster_url est une chaîne de caractères (URL valide)
                    st.image(poster_url, caption=similar_film, width=200)
                else:
                    st.write(f"Le poster pour le film '{similar_film}' n'est pas disponible.")
        else:
            st.write(f"Aucun film avec une durée approximative de {input_temps} minutes n'a été trouvé dans la base de données.")


def set_sidebar_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()