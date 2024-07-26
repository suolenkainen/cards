import pytest
from unittest.mock import Mock, patch


def test_discard_1_under_hand_limit():
    # Mock the player object
    mock_player = Mock()
    mock_card_1 = Mock()
    mock_card_2 = Mock()
    mock_player.hand = [
        mock_card_1,
        mock_card_2
    ]

    mock_player.hand_size = 1
    mock_player.graveyard = []
    mock_player.next_draw_amount = 0

    # Patch the abilities module to avoid import errors
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import discard_phase

        # Call the function under test
        discard_phase(mock_player)

        # Assertions
        assert mock_player.hand_size == 1
        assert mock_card_1 in mock_player.graveyard
        assert mock_card_2 in mock_player.graveyard
        assert mock_player.hand == []



## Use test data to cover 3 cases: mixed tap, monster moving to action list, manapool filling up, but with actions and manapool already begun
def test_draw_cards_full_hand():
    # Mock the player object
    mock_player = Mock()
    mock_player.draw_deck = Mock()
    mock_card_1 = Mock()
    mock_card_2 = Mock()
    mock_card_3 = Mock()
    mock_player.draw_deck.cards = [
        mock_card_1,
        mock_card_2,
        mock_card_3
    ]

    mock_player.next_draw_amount = 1
    mock_player.hand = []
    mock_player.hand_size = 2
    
    # Patch the abilities module to avoid import errors
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import draw_cards

        # Call the function under test
        draw_cards(mock_player)

        # Assertions
        assert mock_player.next_draw_amount == -1 # negative because the player draws two cards (1-2=-1).
        assert mock_player.draw_deck.cards == [mock_card_3]
        assert mock_player.hand == [mock_card_1, mock_card_2]



def test_draw_cards_after_allowing_more_draws_than_hand_limit():
    # Mock the player object
    mock_player = Mock()
    mock_player.draw_deck = Mock()
    mock_card_1 = Mock()
    mock_card_2 = Mock()
    mock_card_3 = Mock()
    mock_card_4 = Mock()
    mock_player.draw_deck.cards = [
        mock_card_1,
        mock_card_2,
        mock_card_3,
    ]

    mock_player.next_draw_amount = 2
    mock_player.hand = [mock_card_4]
    mock_player.hand_size = 2

    # Patch the abilities module to avoid import errors
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import draw_cards

        # Call the function under test
        draw_cards(mock_player)

        # Assertions
        assert mock_player.next_draw_amount == 0 # 0 because the player draws two cards (2-2=0).
        assert mock_player.draw_deck.cards == [mock_card_3]
        assert mock_player.hand == [mock_card_4, mock_card_1, mock_card_2]



def test_draw_cards_more_than_in_deck():
    # Mock the player object
    mock_player = Mock()
    mock_player.draw_deck = Mock()
    mock_card_1 = Mock()
    mock_card_2 = Mock()
    mock_player.draw_deck.cards = [
        mock_card_1,
        mock_card_2
    ]

    mock_player.next_draw_amount = 3
    mock_player.hand = []
    mock_player.hand_size = 2
    
    # Patch the abilities module to avoid import errors
    with patch.dict('sys.modules', {'abilities': Mock()}):
        from game_mechanics.phases import draw_cards

        # Call the function under test
        draw_cards(mock_player)

        # Assertions
        assert mock_player.next_draw_amount == 1
        assert mock_player.draw_deck.cards == []
        assert mock_player.hand == [mock_card_1, mock_card_2]







# TODO: Create a way to check enchantment validity. It should be similar to what already happens in the abilities
def test_enchantment_validity(players):
    # Todo: When attack is OK, make this
    return True




if __name__ == "__main__":
    pytest.main([__file__])