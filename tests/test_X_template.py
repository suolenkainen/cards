import pytest


class mock_class():
    def __init__(self, i) -> None:
        pass


def test_name():
    mock_player = mock_class(0)
    mock_opponent = mock_class(1)
    mock_card = mock_class(2)
    
    #set up a test
    mock_player.table = []
    mock_card.keywords = []
    mock_player.table.append(mock_card)
    
    mock_players = [mock_player, mock_opponent]

    result = True

    #assert
    assert result == True



if __name__ == "__main__":
    pytest.main([__file__])