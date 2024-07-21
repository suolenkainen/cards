"""
The tkinker calls this function every few seconds to run the game.
"""

import setup
import phases

def setup_mock_game():
    # Create players
    players = []
    for i in range(2):
        player = setup.player_object()
        player.id = i
        player.name = "player "+str(i)
        players.append(player)
    
    players.append(0)
    players.append(1)

    return players


def turn_order(players):
    # Identify, who is the player and who is opponent
    player = players[0]
    opponent = players[1]

    # Switch order. After player 1 has played, turn counter rises by one.
    if players[2] == 0:
        players[2] == 1
    else: 
        players[2] = 0
        players[3] += 1
    players[0] = opponent
    players[1] = player

    return players


def game(players):
    player = players[0]
    opponent = players[1]
    
    # Player phases
    phases.untap_phase(player)

    phases.sort_hand(player)

    phases.discard_phase(player)

    phases.draw_cards(player)

    return turn_order(players)
     


if __name__ == "__main__":
    setup_mock_game()