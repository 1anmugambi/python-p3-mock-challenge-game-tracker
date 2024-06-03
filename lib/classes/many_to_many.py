class Game:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string")
        self._title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores) if scores else 0


class Player:
    all = []

    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters")
        self._username = username
        self.__class__.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str) or not (2 <= len(new_username) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters")
        self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        players = [player for player in cls.all if player.played_game(game)]
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise Exception("Player must be an instance of Player")
        if not isinstance(game, Game):
            raise Exception("Game must be an instance of Game")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise Exception("Score must be an integer between 1 and 5000")
        self._player = player
        self._game = game
        self._score = score
        self.__class__.all.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
