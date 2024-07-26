import pytest
from unittest.mock import Mock, patch



def test_name():
    mock_player = Mock()
    mock_opponent = Mock()
    mock_card = Mock()
    
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