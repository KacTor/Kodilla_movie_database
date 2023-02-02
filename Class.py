class Movies:

    def __init__(self, title, releaseDate, genre, numberOfPlays) -> None:
        self.title = title
        self.releaseDate = releaseDate
        self.genre = genre
        self.numberOfPlays = numberOfPlays

    def play(self):
        self.numberOfPlays += 1

    def __str__(self) -> str:
        return f'{self.title} ({self.releaseDate})'

    def __repr__(self) -> str:
        return f'{self.title} ({self.releaseDate}) Views: {self.numberOfPlays}'


class TvSeries(Movies):

    def __init__(self, numberOfSeason, numberOfEpisode, *args) -> None:
        super().__init__(*args)
        self.numberOfSeason = numberOfSeason
        self.numberOfEpisode = numberOfEpisode

    def __str__(self) -> str:
        return f'{self.title} S{self.numberOfSeason:02d}E{self.numberOfEpisode:02d}.'

    def __repr__(self) -> str:
        return f'{self.title} S{self.numberOfSeason:02d}E{self.numberOfEpisode:02d} Views: {self.numberOfPlays}'
