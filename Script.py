import csv
from Class import Movies, TvSeries
import random
import datetime

today = datetime.date.today().strftime("%d-%m-%Y")

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


def add_full_season(title: str, releaseDate: int, genre: str, numberOfSeason: int, amountOfEpisode: int):
    numberOfEpisode = 1
    for _ in range(amountOfEpisode):
        newEpisode = TvSeries(numberOfSeason, numberOfEpisode,
                              title, releaseDate, genre, 0)
        movieAndSeriesDatabase.append(newEpisode)
        numberOfEpisode += 1

    return movieAndSeriesDatabase


if __name__ == "__main__":

    add_to_base_from_csv_file('TvSeriesDatabase.csv', 1)

    add_to_base_from_csv_file('MovieDatabase.csv', 0)

    add_full_season('Band of Brothers', 2001, 'Drama', 1, 9)

    print('Library of movies and series:')
    for row in movieAndSeriesDatabase:
        print(row)

    generate_views(100)

    print(f'Top 3 movies and TvSeries of today ({today}):')

    print('MOVIE:')

    for index, row in enumerate(top_titles(0), 1):
        print(f'{index} -> {row}')

    print('TvSeries:')

    for index, row in enumerate(top_titles(1), 1):
        print(f'{index} -> {row}')
