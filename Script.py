import csv
from Class import Movies, TvSeries
import random

movieAndSeriesDatabase = []

# Add movies or TvSeries from external file csv


def add_to_base_from_csv_file(nameOfFile: str, movieOrTvSeries: int):
    'movieOrTvSeries: choose 0 for movie or 1 for TvSeries '
    with open(nameOfFile, newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=';')

        file.__next__()

        if movieOrTvSeries == False:
            for row in file:
                nameOfMovie = row[0]
                releaseDate = row[1]
                genre = row[2].split(',')
                numberOfPlays = row[3]
                movieAndSeriesDatabase.append(
                    Movies(nameOfMovie, releaseDate, genre, int(numberOfPlays)))
        else:
            for row in file:
                nameOfMovie = row[0]
                releaseDate = row[1]
                genre = row[2].split(',')
                numberOfPlays = row[3]
                numberOfSeason = row[4]
                numberOfEpisode = row[5]
                movieAndSeriesDatabase.append(
                    TvSeries(int(numberOfSeason), int(numberOfEpisode), nameOfMovie, releaseDate, genre, int(numberOfPlays)))

# Return only movies from database


def get_movies():
    moviesList = []
    for movie in movieAndSeriesDatabase:
        if isinstance(movie, TvSeries):
            continue
        else:
            moviesList.append(movie)

    sortByTitle = sorted(moviesList, key=lambda movie: movie.title)

    return sortByTitle

# Return only series from database


def get_series():
    seriesList = []
    for series in movieAndSeriesDatabase:
        if isinstance(series, TvSeries):
            seriesList.append(series)
        else:
            continue

    sortByTitle = sorted(seriesList, key=lambda series: series.title)

    return sortByTitle


def search(searchedTitle: str):
    for title in movieAndSeriesDatabase:
        if searchedTitle in title.title:
            print(title)


def generate_views(repetition):
    for _ in range(repetition+1):
        selectedTitle = random.choice(movieAndSeriesDatabase)
        selectedTitle.numberOfPlays = random.randint(1, 100)


def top_titles(contentType: int, numberOfTitles=3):
    'contentType: choose 0 for movie or 1 for TvSeries'
    if contentType == False:
        sortByView = sorted(
            get_movies(), key=lambda view: view.numberOfPlays, reverse=True)

    elif contentType == True:
        sortByView = sorted(
            get_series(), key=lambda view: view.numberOfPlays, reverse=True)

    return sortByView[0:numberOfTitles]


add_to_base_from_csv_file('TvSeriesDatabase.csv', 1)

add_to_base_from_csv_file('MovieDatabase.csv', 0)


generate_views(100)


print(top_titles(1))
