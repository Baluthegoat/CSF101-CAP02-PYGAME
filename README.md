## Test Documentation.

# Overview
This documentation provides details about the test cases implemented in the cargame project. The test cases are designed to ensure the correctness and reliability of the codebase by verifying the functionality of key components.

# Test Cases
test_screen_size
This test case checks if the screen size is set correctly using the Pygame library. It creates a Pygame display with a specified size and asserts that the screen's size matches the expected dimensions.

Resources Used:

Pygame library
Pytest framework
Justification:

Pygame is used for graphical user interface development in the cargame project.
Pytest is employed for easy and organized unit testing.
test_introImg
This test case verifies the loading of the introductory image. It loads the specified image file and asserts that the image is successfully loaded.

Resources Used:

Pygame library
Pytest framework
Justification:

Ensures the correct loading of necessary images for the game.
test_instructionIMG
Similar to test_introImg, this test case checks the loading of the instruction image.

Resources Used:

Pygame library
Pytest framework
Justification:

Validates the loading of another essential image.
test_pygame_mixer_music_play
This test case checks the functionality of Pygame mixer for playing music. It loads three different music files and asserts that the music playback is initiated.

Resources Used:

Pygame library
Pytest framework
Justification:

Ensures the correct loading and playing of game sounds.
test_countdown
This test case focuses on the countdown functionality. It checks the loading of a background image for the countdown and asserts the availability of required resources.

Resources Used:

Pygame library
Pytest framework
Justification:

Validates the countdown feature and associated image loading.
test_iscollision_detection
This test case checks the collision detection logic in the game. It defines positions for the main car and three other cars, creating collision tuples for each pair, and asserts their existence.

Resources Used:

Pygame library
Pytest framework
Justification:

Verifies the correctness of collision detection in the game.
test_gameloop
This test case checks the game loop functionality. It sets up a Pygame screen, a clock, and mocks the system exit to ensure the game loop can be exited without actual system termination.

Resources Used:

Pygame library
Pytest framework
unittest.mock
Justification:

Validates the behavior of the game loop.
test_gameover
This test case focuses on the game-over scenario. It mocks Pygame functions related to image loading and display update, simulating a game-over event triggered by either quitting or pressing the space key. Assertions are made based on the expected behavior of the game-over event.

Resources Used:

Pygame library
Pytest framework
unittest.mock
Justification:

Ensures proper handling of game-over conditions.


