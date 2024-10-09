import unittest
from unittest.mock import patch
from app import play_game, get_scores, get_db


class pythonInputTests(unittest.TestCase):

    # Tests the user input when taking a guess (correct) :
    @patch('builtins.input', return_value = int(50))
    @patch('random.randint', return_value=50)
    def test_correctGuess (self, mock_randint, mock_input):
        # Arrange & Act
        print("------------------------------------------------------------")
        print("                                                            ")
        print("TEST DESC --> Checks that the game passes when the num is correctly guessed")
        print("                                                            ")
        guess = play_game()
        print("Test Complete - Passed")   
        print("                                                            ")     
        # Assert
        mock_input.assert_called()
        mock_randint.assert_called_with(1, 100)
    
    # Tests the user input when taking a guess (incorrect):
    @patch('builtins.input', side_effect=[35, 59, "n"])
    @patch('random.randint', return_value=59)
    def test_incorrectGuess (self, mock_randint, mock_input):
        # Arrange & Act
        print("------------------------------------------------------------")
        print("                                                            ")
        print("TEST DESC --> Checks that the game respondes correcly to an incorrect guess")
        print("                                                            ")
        guess = play_game()
        print("Test Complete - Passed")   
        print("                                                            ")     
        # Assert
        mock_input.assert_called()
        mock_randint.assert_called_with(1, 100)

    
class pythonReplayTests(unittest.TestCase):

    # Tests that the game can be replayed:
     @patch('builtins.input', side_effect=[23, 86, "y", 45, "n"])
     @patch('random.randint', side_effect=[86, 45])
     def test_replayability (self, mock_randint, mock_input):
        # Arrange & Act
        print("------------------------------------------------------------")
        print("                                                            ")
        print("TEST DESC --> Checks that the game is able to be replayed")
        print("                                                            ")
        guess = play_game()
        guess_2 = play_game()
        print("Test Complete - Passed")   
        print("                                                            ")     
        # Assert
        mock_input.assert_called()
        mock_randint.assert_called_with(1, 100)

        mock_input.assert_called()
        mock_randint.assert_called_with(1, 100)


class pythonDbTests(unittest.TestCase):

    # Tests that the apps database works correctly:
     @patch('builtins.input', side_effect=[20, 36, 92, "n"])
     @patch('random.randint', return_value=92)
     def test_database (self, mock_randint, mock_input):
        # Arrange & Act
        print("------------------------------------------------------------")
        print("                                                            ")
        print("TEST DESC --> Checks that the game scores can be retrieved")
        print("                                                            ")
        guess     = play_game()
        getScores = get_scores()
        getDb     = get_db()
        print("Test Complete - Passed")   
        print("                                                            ")     
        # Assert
        mock_input.assert_called()
        mock_randint.assert_called_with(1, 100)

#---------------------------
if __name__ == "__main__":
    unittest.main()
