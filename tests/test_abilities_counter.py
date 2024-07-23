import pytest
from game_mechanics.abilities import counter


class mock_class():
    def __init__(self, i) -> None:
        pass


def test_no_matching_cards():
    mock_player = mock_class(0)
    mock_opponent = mock_class(1)
    mock_card_counter = mock_class(2)
    mock_card_ = mock_class(2)
    mock_parameters = {'target': 'player', 'keywords': ['blue']}
    
    #set up a test
    mock_player.hand = []
    mock_opponent.table = []
    mock_card.keywords = []
    mock_player.table.append(mock_card)
    
    mock_players = [mock_player, mock_opponent]

    result = counter(mock_players, mock_parameters, mock_card_counter)

    # assert
    assert result == True



def test_matching():
    pass


if __name__ == "__main__":
    pytest.main([__file__])