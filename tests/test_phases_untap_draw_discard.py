import pytest
from unittest.mock import Mock, patch



## Use test data to cover 3 cases: mixed tap, monster moving to action list, manapool filling up.
def test_untap_phase_1():
    # Mock the player object
    mock_player = Mock()
    # mock_player.name = "TestPlayer"
    mock_player.table = [
        Mock(tapped=True, type="monster", color="red"),
        Mock(tapped=False, type="mana", color="blue"),
        Mock(tapped=True, type="mana", color="green")
    ]
    mock_player.actions = []
    mock_player.manapool = []

    # Patch the abilities module to avoid import errors
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import untap_phase

        # Call the function under test
        untap_phase(mock_player)

        # Assertions
        assert mock_player.actions == [mock_player.table[0]]
        assert "blue" in mock_player.manapool
        assert mock_player.table[0].tapped is False
        assert mock_player.table[1].tapped is False
        assert mock_player.table[2].tapped is False



## Use test data to cover 3 cases: mixed tap, monster moving to action list, manapool filling up, but with actions and manapool already begun
def test_untap_phase_2():
    # Mock the player object
    mock_player = Mock()
    mock_action_card = Mock()    
    mock_player.table = [
        Mock(tapped=True, type="monster", color="yellow"),
        Mock(tapped=False, type="mana", color="brown"),
        Mock(tapped=True, type="mana", color="black")
    ]

    mock_player.actions = [mock_action_card]
    mock_player.manapool = ["white"]

    # Patch the abilities module to avoid import errors
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import untap_phase

        # Call the function under test
        untap_phase(mock_player)

        # Assertions
        assert mock_player.actions == [mock_action_card, mock_player.table[0]]
        assert "brown" in mock_player.manapool
        assert "black" in mock_player.manapool
        assert mock_player.table[0].tapped is False
        assert mock_player.table[1].tapped is False
        assert mock_player.table[2].tapped is False



## Test a player without any actions in list
def test_actions_empty():
    # Mock the player and cards
    mock_player = Mock()
    mock_player.actions = []
    
    players = [mock_player]

    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import action
        
        # Call the function under test
        action(players)    
        
        # Assert that the player actions haven't changed
        assert mock_player.actions == []



## Test a player with monster in the action list
def test_action_with_monster():
    # Mock the player and cards
    mock_card_with_monster = Mock()
    mock_card_with_monster.abilities = []
    mock_card_with_monster.type = "monster"
    
    mock_player = Mock()
    mock_player.actions = [mock_card_with_monster]
    
    players = [mock_player]

    # Patch the dependencies
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import action
        with patch('game_mechanics.phases.attack') as mock_attack:
            
            # Call the function under test
            action(players)
        
            # Assert call_abilities was called for card with abilities
            mock_attack.assert_called_once_with(mock_card_with_monster, players)
            
            # Assert the card with type monster was removed from actions
            assert mock_card_with_monster not in mock_player.actions



## Test a player with ability in the action list
def test_action_with_ability():
    # Mock the player and cards
    mock_card_with_ability = Mock()
    mock_card_with_ability.abilities = ["channel"]
    mock_card_with_ability.type = "enchantment"
    
    mock_player = Mock()
    mock_player.actions = [mock_card_with_ability]
    
    players = [mock_player]

    # Patch the dependencies
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import action
        
        # Call the function under test
        action(players)
        
        # Assert the card with ability was removed from actions
        assert mock_card_with_ability not in mock_player.actions  



if __name__ == "__main__":
    pytest.main([__file__])