# Movie Recommendation System

A personalized movie recommendation system built using Python and Streamlit.  
This system provides movie suggestions based on your preferred genres, cast, and directors.  
It includes a rating feature to display user ratings and visualizes movie details.

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Sohibjon-0703/movie_rec_streamlit.git
cd movie_rec_streamlit
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

Using venv (built-in Python module):
```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:
```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

After activating the virtual environment, install the required libraries:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

Start the Streamlit app with:
```bash
streamlit run app.py
```

This will open the movie recommendation app in your web browser at http://localhost:8501

## Features

* Personalized Recommendations: Get movie suggestions based on your favorite genres, cast, and directors.
* Rating System: Rate movies and see your ratings summarized in a chart.
* Movie Details: View detailed information such as movie name, year, genre, cast, director, and IMDB rating.
* Visualization: Interactive charts display your rating summaries.


## Folder Structure

```bash
movie_recommendation/
├── app.py                  # Main Streamlit application
├── recommender.py          # Backend recommendation logic
├── requirements.txt        # Project dependencies
├── data/                   # Directory containing movie data
└── README.md               # This file
```


## Dependencies

* Python 3.x
* Streamlit
* Pandas
* Scikit-learn
* Seaborn
* Altair

(Additional dependencies are listed in requirements.txt)
