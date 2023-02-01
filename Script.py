import csv
from Class import Movie, TvSeries

movieAndSeriesDatabase = []


def add_to_base_from_csv_file(nameOfFile: str, movieOrTvSeries: int):
    'movieOrTvSeries, choose 0 for movie or 1 for TvSeries '
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
                    Movie(nameOfMovie, releaseDate, genre, int(numberOfPlays)))
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


add_to_base_from_csv_file('TvSeriesDatabase.csv', 1)

add_to_base_from_csv_file('MovieDatabase.csv', 0)


print(movieAndSeriesDatabase)
