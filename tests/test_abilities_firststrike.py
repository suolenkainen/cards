import pytest
from unittest.mock import Mock
from game_mechanics.abilities import first_strike



def test_monsters_ability():
    # Set up test
    mock_player = Mock()
    mock_opponent = Mock()
    mock_parameters = {"target": "self"}

    mock_players = [mock_player, mock_opponent]

    # Run test
    result = first_strike(mock_players, mock_parameters)

    # assert
    assert result == False



def test_no_viable_targets_on_table():
    # Set up test
    mock_player = Mock()
    mock_opponent = Mock()
    mock_table_card_m = Mock()
    mock_table_card_e = Mock()
    mock_parameters = {'target': 'player', 'keywords': ['blue']}
    
    mock_table_card_m.keywords = ["green"]
    mock_table_card_e.keywords = ["blue"]
    mock_table_card_m.type = "monster"
    mock_table_card_e.type = "enchantment"
    
    mock_player.table = [mock_table_card_m, mock_table_card_e]

    mock_players = [mock_player, mock_opponent]

    # Run test
    result = first_strike(mock_players, mock_parameters)

    # assert
    assert result == False



def test_viable_targets_on_table_but_one_has_firststrike_already():
    # Set up test
    mock_player = Mock()
    mock_opponent = Mock()
    mock_enchantment_card = Mock()
    mock_table_card_1 = Mock()
    mock_table_card_2 = Mock()
    mock_enchantment_card.type = "enchantment"
    mock_parameters = {'target': 'player', 'keywords': ['blue'], 'sort': ["priority"]}
    
    mock_table_card_1.keywords = ["blue"]
    mock_table_card_2.keywords = ["blue"]
    mock_table_card_1.type = "monster"
    mock_table_card_2.type = "monster"
    mock_table_card_1.priority = 3
    mock_table_card_2.priority = 2
    mock_table_card_1.abilities = [['first_strike', "target:self"]]
    mock_table_card_2.abilities = []
    
    mock_player.table = [mock_table_card_1, mock_table_card_2]

    mock_players = [mock_player, mock_opponent]

    # Run test
    result = first_strike(mock_players, mock_parameters, card=mock_enchantment_card)

    # assert
    assert result == True



if __name__ == "__main__":
    pytest.main([__file__])