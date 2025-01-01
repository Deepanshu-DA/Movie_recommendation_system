import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

select_movie_name = st.selectbox('Select a movie to get recommendations:', movies['title'].values)


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=db29f33dc9897f5ea825275d28348fa1&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Available"
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_poster = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_poster
    except Exception as e:
        st.error("Error in fetching recommendations.")
        return [], []


if st.button('Predict'):
    recommended_movie_names, recommended_movie_posters = recommend(select_movie_name)

    if recommended_movie_names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(recommended_movie_posters[idx])
                st.text(recommended_movie_names[idx])
    else:
        st.write("No recommendations available.")
