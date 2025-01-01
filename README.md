# Movie Recommender System

## Overview
The **Movie Recommender System** is a web application built using Streamlit that provides movie recommendations based on a selected movie. The app utilizes a precomputed similarity matrix to suggest movies similar to the one chosen by the user.

## Features
- **Movie Selection**: Users can select a movie from a dropdown menu.
- **Recommendations**: The app displays five recommended movies along with their posters.
- **Interactive Interface**: The app is user-friendly and provides an engaging experience.

## Requirements
To run the application, you need the following:

- Python 3.7+
- Required Python libraries:
  ```bash
  streamlit
  pandas
  requests
  pickle
## Installation
1. Clone the repository or download the source code.
2. Ensure you have Python installed on your system.
3. Install the required libraries by running:
   ```bash
   pip install streamlit pandas requests
 ## Files
- `app.py`: The main application script.
- `movies.pkl`: A pickle file containing movie data in dictionary format.
- `similarity.pkl`: A pickle file containing the similarity matrix.

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
2. In the browser, select a movie from the dropdown menu.
3. Click the **Predict** button to get recommendations.
4. The app will display the recommended movies and their posters.

## Key Functions

### `fetch_poster(movie_id)`
Fetches the poster URL for a given movie ID using the TMDB API.

- **Parameters**:  
  `movie_id` (int) - The ID of the movie.  
- **Returns**:  
  A URL string of the movie poster or a placeholder image if unavailable.

### `recommend(movie)`
Provides a list of recommended movies and their posters based on the selected movie.

- **Parameters**:  
  `movie` (str) - The title of the selected movie.  
- **Returns**:  
  A tuple containing a list of recommended movie titles and their poster URLs.

## API Usage
The app uses the [TMDB API](https://www.themoviedb.org/documentation/api) to fetch movie posters.  
Ensure you have a valid API key and replace `db29f33dc9897f5ea825275d28348fa1` in the code with your own key.

## Notes
- Ensure the `movies.pkl` and `similarity.pkl` files are in the same directory as the script.
- If the API key is invalid or rate-limited, the app will display placeholder images.

## Troubleshooting
- **Error in Fetching Recommendations**: Ensure the `movies.pkl` and `similarity.pkl` files are not corrupted.
- **Poster Fetching Issues**: Verify the TMDB API key and internet connectivity.

## Future Enhancements
- Add a search bar for easier movie selection.
- Improve error handling and logging.
- Incorporate user ratings or genres for better recommendations.

## License
This project is open-source and available under the MIT License.

