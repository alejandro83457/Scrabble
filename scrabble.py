letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Contains dict with letters and points mapped
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Added blank tile points
letter_to_points[' '] = 0


def score_word(word):
    """ func will add up points for word """
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


# TEST for score_word()
brownie_points = score_word('BROWNIE')
# print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': [
    'ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# Will contain dict with all players and their total pts
player_to_points = {}

# Calculates the points for each word for each player
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

# TEST for loop
# print(player_to_points)


# Testing purposes
