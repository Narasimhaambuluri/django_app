import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_api.settings")
django.setup()

from movies.models import Movie


def load_movies():
    df = pd.read_csv("movies.csv")
    df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
    df["Meta_score"] = pd.to_numeric(df["Meta_score"], errors="coerce")
    df["IMDB_Rating"] = pd.to_numeric(df["IMDB_Rating"], errors="coerce")

    for _, row in df.iterrows():
        Movie.objects.create(
            poster_link=str(row["Poster_Link"]),
            series_title=str(row["Series_Title"]),
            released_year=(
                int(row["Released_Year"]) if pd.notna(row["Released_Year"]) else 0
            ),
            certificate=(
                str(row["Certificate"]) if pd.notna(row["Certificate"]) else "N/A"
            ),
            runtime=str(row["Runtime"]) if pd.notna(row["Runtime"]) else "N/A",
            genre=str(row["Genre"]) if pd.notna(row["Genre"]) else "N/A",
            imdb_rating=(
                float(row["IMDB_Rating"]) if pd.notna(row["IMDB_Rating"]) else 0.0
            ),
            overview=str(row["Overview"]) if pd.notna(row["Overview"]) else "",
            meta_score=int(row["Meta_score"]) if pd.notna(row["Meta_score"]) else 0,
            director=str(row["Director"]) if pd.notna(row["Director"]) else "N/A",
            star1=str(row["Star1"]) if pd.notna(row["Star1"]) else "N/A",
            star2=str(row["Star2"]) if pd.notna(row["Star2"]) else "N/A",
            star3=str(row["Star3"]) if pd.notna(row["Star3"]) else "N/A",
            star4=str(row["Star4"]) if pd.notna(row["Star4"]) else "N/A",
            no_of_votes=int(row["No_of_Votes"]) if pd.notna(row["No_of_Votes"]) else 0,
            gross=str(row["Gross"]) if pd.notna(row["Gross"]) else "N/A",
        )


if __name__ == "__main__":
    load_movies()
