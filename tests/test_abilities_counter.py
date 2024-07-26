import pytest
from unittest.mock import Mock
from game_mechanics.abilities import counter



def test_counter_doesnt_work():
    # Set up test
    mock_player = Mock()
    mock_opponent = Mock()
    mock_to_be_countered = Mock()
    mock_counter_card_ = Mock()
    mock_counter_parameters = {'keywords': ['blue']}
    
    mock_player.hand = []
    mock_opponent.hand = []
    mock_player.graveyard = []
    mock_opponent.graveyard = []
    mock_to_be_countered.keywords = ["green"]
    mock_player.hand.append(mock_to_be_countered)
    mock_opponent.hand.append(mock_counter_card_)
    variables = {"played_card": mock_to_be_countered, "interrupt_card": mock_counter_card_}

    mock_players = [mock_player, mock_opponent]

    # Run test
    result = counter(mock_players, mock_counter_parameters, variables=variables)

    # assert
    assert result == False



def test_counter_works_one_on_one_parameter():
    # Set up test
    mock_player = Mock()
    mock_opponent = Mock()
    mock_to_be_countered = Mock()
    mock_counter_card_ = Mock()
    mock_counter_parameters = {'keywords': ['blue']}
    
    mock_player.hand = []
    mock_opponent.hand = []
    mock_player.graveyard = []
    mock_opponent.graveyard = []
    mock_to_be_countered.keywords = ["blue"]
    mock_player.hand.append(mock_to_be_countered)
    mock_opponent.hand.append(mock_counter_card_)
    variables = {"played_card": mock_to_be_countered, "interrupt_card": mock_counter_card_}

    mock_players = [mock_player, mock_opponent]

    # Run test
    result = counter(mock_players, mock_counter_parameters, variables=variables)

    # assert
    assert result == True



def test_counter_works_two_on_three_parameter():
    # Set up test
    mock_player = Mock()
    mock_opponent = Mock()
    mock_to_be_countered = Mock()
    mock_counter_card_ = Mock()
    mock_counter_parameters = {'keywords': ['blue', 'monster']}
    
    mock_player.hand = []
    mock_opponent.hand = []
    mock_player.graveyard = []
    mock_opponent.graveyard = []
    mock_to_be_countered.keywords = ['blue', 'monster','counter']
    mock_player.hand.append(mock_to_be_countered)
    mock_opponent.hand.append(mock_counter_card_)
    variables = {"played_card": mock_to_be_countered, "interrupt_card": mock_counter_card_}

    mock_players = [mock_player, mock_opponent]

    # Run test
    result = counter(mock_players, mock_counter_parameters, variables=variables)

    # assert
    assert result == True



if __name__ == "__main__":
    pytest.main([__file__])