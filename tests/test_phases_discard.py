import pytest
from unittest.mock import Mock, patch



def test_discard_1_under_hand_limit():
    # Mock test data
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



if __name__ == "__main__":
    pytest.main([__file__])