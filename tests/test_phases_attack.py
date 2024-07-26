import pytest
from unittest.mock import Mock, patch



def test_no_opponent_blockers():
    # Mock test data
    mock_attacking_monster = Mock()
    mock_attacking_monster.keywords = []
    mock_attacking_monster.tapped = False
    mock_attacking_monster.attack = 1
    
    mock_opponent = Mock()
    mock_opponent.table = []
    mock_opponent.health = 1
    mock_player = Mock()
    mock_player.table = [mock_attacking_monster]
            
    mock_players = [mock_player, mock_opponent]

    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import attack

        # Call the function under test and there should be no blocker
        attack(mock_attacking_monster, mock_players)

        #assert
        assert mock_attacking_monster.tapped == True
        assert mock_player.table[0].tapped == True
        assert mock_opponent.health == 0


def test_opponent_block_equals_attacker():
    # Mock test data
    mock_attacking_monster = Mock()
    mock_attacking_monster.keywords = []
    mock_attacking_monster.tapped = False
    mock_attacking_monster.attack = 1
    mock_attacking_monster.defence = 1

    mock_non_blocking_monster = Mock()
    mock_non_blocking_monster.type = "monster"
    mock_non_blocking_monster.keywords = []
    mock_non_blocking_monster.tapped = True
    mock_non_blocking_monster.attack = 1
    mock_non_blocking_monster.defence = 1

    mock_blocking_monster = Mock()
    mock_blocking_monster.type = "monster"
    mock_blocking_monster.keywords = []
    mock_blocking_monster.tapped = False
    mock_blocking_monster.attack = 1
    mock_blocking_monster.defence = 1

    mock_opponent = Mock()
    mock_opponent.health = 1
    mock_opponent.actions = []
    mock_opponent.graveyard = []
    mock_player = Mock()
    mock_player.graveyard = []
    mock_opponent.table = [mock_non_blocking_monster, mock_blocking_monster]
    mock_player.table = [mock_attacking_monster]
            
    mock_players = [mock_player, mock_opponent]

    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import attack
        # Call the function under test and there should be no blocker
        attack(mock_attacking_monster, mock_players)

        #assert
        assert mock_player.table == []
        assert mock_player.graveyard == [mock_attacking_monster]
        assert mock_opponent.table == [mock_non_blocking_monster]
        assert mock_opponent.graveyard == [mock_blocking_monster]
        assert mock_opponent.health == 1



def test_opponent_block_less_than_attacker():
    # Mock test data
    mock_attacking_monster = Mock()
    mock_attacking_monster.keywords = []
    mock_attacking_monster.tapped = False
    mock_attacking_monster.attack = 2
    mock_attacking_monster.defence = 2

    mock_non_blocking_monster = Mock()
    mock_non_blocking_monster.type = "monster"
    mock_non_blocking_monster.keywords = []
    mock_non_blocking_monster.tapped = True
    mock_non_blocking_monster.attack = 1
    mock_non_blocking_monster.defence = 1

    mock_blocking_monster = Mock()
    mock_blocking_monster.type = "monster"
    mock_blocking_monster.keywords = []
    mock_blocking_monster.tapped = False
    mock_blocking_monster.attack = 1
    mock_blocking_monster.defence = 1

    mock_opponent = Mock()
    mock_opponent.health = 1
    mock_opponent.actions = []
    mock_opponent.graveyard = []
    mock_player = Mock()
    mock_player.graveyard = []
    mock_opponent.table = [mock_non_blocking_monster, mock_blocking_monster]
    mock_player.table = [mock_attacking_monster]
            
    mock_players = [mock_player, mock_opponent]

    # Run test
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import attack
        
        attack(mock_attacking_monster, mock_players)

        #assert
        assert mock_player.table == [mock_attacking_monster]
        assert mock_player.graveyard == []
        assert mock_attacking_monster.tapped == True
        assert mock_opponent.table == [mock_non_blocking_monster]
        assert mock_opponent.graveyard == [mock_blocking_monster]
        assert mock_opponent.health == 1



def test_opponent_2_blockers():
    # Mock test data
    mock_attacking_monster = Mock()
    mock_attacking_monster.keywords = []
    mock_attacking_monster.tapped = False
    mock_attacking_monster.attack = 2
    mock_attacking_monster.defence = 2

    mock_blocking_monster_1 = Mock()
    mock_blocking_monster_1.type = "monster"
    mock_blocking_monster_1.keywords = []
    mock_blocking_monster_1.tapped = False
    mock_blocking_monster_1.attack = 1
    mock_blocking_monster_1.defence = 1

    mock_blocking_monster_2 = Mock()
    mock_blocking_monster_2.type = "monster"
    mock_blocking_monster_2.keywords = []
    mock_blocking_monster_2.tapped = False
    mock_blocking_monster_2.attack = 1
    mock_blocking_monster_2.defence = 1

    mock_opponent = Mock()
    mock_opponent.health = 1
    mock_opponent.actions = []
    mock_opponent.graveyard = []
    mock_player = Mock()
    mock_player.graveyard = []
    mock_opponent.table = [mock_blocking_monster_1, mock_blocking_monster_2]
    mock_player.table = [mock_attacking_monster]
            
    mock_players = [mock_player, mock_opponent]

    # Run test
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import attack
        
        attack(mock_attacking_monster, mock_players)

        #assert
        assert mock_player.table == []
        assert mock_player.graveyard == [mock_attacking_monster]
        assert mock_opponent.table == []
        assert mock_blocking_monster_1 in mock_opponent.graveyard
        assert mock_blocking_monster_2 in mock_opponent.graveyard
        assert mock_opponent.health == 1



def test_attacker_is_blocker():
    # Mock test data
    mock_player = Mock()
    mock_opponent = Mock()
    mock_attacking_monster = Mock()
    mock_attacking_monster.keywords = ["blocker"]
    
    mock_players = [mock_player, mock_opponent]

    # Run test
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import attack
        # Call the function under test and the attack should stop before damage
        result_none = attack(mock_attacking_monster, mock_players)

        #assert
        assert result_none == None
        assert mock_player == mock_player
        assert mock_attacking_monster.keywords == ["blocker"]




if __name__ == "__main__":
    pytest.main([__file__])