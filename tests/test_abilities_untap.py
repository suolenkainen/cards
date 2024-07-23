import pytest
from game_mechanics.abilities import untap


class mock_class():
    def __init__(self, i) -> None:
        pass



def test_untap_no_keywords_tapped():
    mock_player = mock_class(1)
    mock_opponent = mock_class(2)
    mock_card = mock_class(3)
    mock_parameters = {'target': 'player', 'keywords': ['blue']}
    
    #set up a test
    mock_player.table = []
    mock_card.keywords = ['green']
    mock_card.tapped = True
    mock_player.table.append(mock_card)
    
    mock_players = [mock_player, mock_opponent]

    # Check that when no keywords, returns false
    result_keyword = untap(mock_players, mock_parameters)

    # setup new test
    mock_player.table = []
    mock_card = mock_class(4)
    mock_card.keywords = ['blue']
    mock_card.tapped = False
    mock_player.table.append(mock_card)

    # Check that when tapped, returns false
    result_tapped = untap(mock_players, mock_parameters)

    #assert
    assert result_keyword == False
    assert result_tapped == False



def test_untap_one_target():
    mock_player = mock_class(1)
    mock_opponent = mock_class(2)
    mock_card = mock_class(3)
    mock_parameters = {'target': 'player', 'keywords': ['blue'], 'sort': ["priority"]}
    
    #set up a test
    mock_player.table = []
    mock_card.keywords = ['blue']
    mock_card.tapped = True
    mock_card.priority = 0
    mock_player.table.append(mock_card)
    
    mock_players = [mock_player, mock_opponent]

    # Check that when no keywords, returns false
    result_one_target = untap(mock_players, mock_parameters)

    #assert
    assert result_one_target == True



def test_untap_one_target():
    mock_player = mock_class(1)
    mock_opponent = mock_class(2)
    mock_card = mock_class(3)
    mock_parameters = {'target': 'player', 'keywords': ['blue'], 'sort': ["priority"]}
    
    #set up a test
    mock_player.table = []
    mock_card.keywords = ['blue']
    mock_card.tapped = True
    mock_card.priority = 0
    mock_player.table.append(mock_card)
    
    mock_players = [mock_player, mock_opponent]

    # Check that when no keywords, returns false
    result_one_target = untap(mock_players, mock_parameters)

    #assert
    assert result_one_target == True
    
    

def test_untap_one_of_two_target():
    mock_player = mock_class(1)
    mock_opponent = mock_class(2)
    mock_card_1 = mock_class(3)
    mock_card_2 = mock_class(4)
    mock_parameters = {'amount': 1, 'target': 'player', 'keywords': ['blue'], 'sort': ["priority"]}
    
    #set up a test
    mock_player.table = []
    mock_card_1.keywords = ['blue']
    mock_card_1.name = "1"
    mock_card_1.tapped = True
    mock_card_1.priority = 0
    mock_player.table.append(mock_card_1)
    
    mock_card_2.keywords = ['blue']
    mock_card_2.name = "2"
    mock_card_2.tapped = True
    mock_card_2.priority = 1
    mock_player.table.append(mock_card_2)
    
    mock_players = [mock_player, mock_opponent]

    # Check that when no keywords, returns false
    result_one_two_target = untap(mock_players, mock_parameters)

    #assert
    assert result_one_two_target == True



def test_untap_two_of_three_target():
    mock_player = mock_class(1)
    mock_opponent = mock_class(2)
    mock_card_1 = mock_class(3)
    mock_card_2 = mock_class(4)
    mock_card_3 = mock_class(5)
    mock_parameters = {'amount': 2, 'target': 'player', 'keywords': ['blue'], 'sort': ["priority"]}
    
    #set up a test
    mock_player.table = []
    mock_card_1.keywords = ['blue']
    mock_card_1.name = "1"
    mock_card_1.tapped = True
    mock_card_1.priority = 0
    mock_player.table.append(mock_card_1)
    
    mock_card_2.keywords = ['blue']
    mock_card_2.name = "2"
    mock_card_2.tapped = True
    mock_card_2.priority = 1
    mock_player.table.append(mock_card_2)

    mock_card_3.keywords = ['blue']
    mock_card_3.name = "3"
    mock_card_3.tapped = True
    mock_card_3.priority = 3
    mock_player.table.append(mock_card_3)
    
    mock_players = [mock_player, mock_opponent]

    # Check that when no keywords, returns false
    result_two_target = untap(mock_players, mock_parameters)

    #assert
    assert result_two_target == True



def test_untap_up_to_two_of_one_target():
    mock_player = mock_class(1)
    mock_opponent = mock_class(2)
    mock_card_1 = mock_class(3)
    mock_parameters = {'amount': 2, 'upto': True, 'target': 'player', 'keywords': ['blue'], 'sort': ["priority"]}
    
    #set up a test
    mock_player.table = []
    mock_card_1.keywords = ['blue']
    mock_card_1.name = "1"
    mock_card_1.tapped = True
    mock_card_1.priority = 0
    mock_player.table.append(mock_card_1)
    
    mock_players = [mock_player, mock_opponent]

    # Check that when no keywords, returns false
    result_upto_target = untap(mock_players, mock_parameters)

    #assert
    assert result_upto_target == True



if __name__ == "__main__":
    pytest.main([__file__])