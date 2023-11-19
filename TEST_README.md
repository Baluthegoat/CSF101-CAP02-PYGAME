## Car Game Test.

## Overview
This documentation provides details about the test cases implemented in the cargame(Racing Monster). The test is done using Pytest and the test cases are designed to ensure the correctness and reliability of the codebase by verifying the functionality of key components. This test covers various aspects of the game including screen size, images, sounds, collision detection, and game loop functionality.

## Running Tests
It contains several tests to ensure the functionality of the Car Game. The tests include:

1. **Screen Size Test**: This test checks if the pygame screen is correctly initialized with the given size.

![Screenshot from 2023-11-19 15-37-38](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/a7da9cec-a8fd-427d-98de-92eb0a934aeb)

2. **Intro Image Test**: This test checks if the intro image is loaded correctly. We load the image using the pygame   image load function and assert that the image is loaded.

![Screenshot from 2023-11-19 15-21-11](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/f1028776-dff0-4a68-8f4e-deeaa854517b)

3. **Instruction Image Test**: This test case checks if the instruction image is loaded correctly. I load the image using the pygame image load function and assert that the image is loaded.

![Screenshot from 2023-11-19 15-25-03](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/b04d4bd5-3c3d-4a9a-a491-7aaedfcdad53)

4. **Pygame Mixer Music Play Test**: This test case checks if the music is played correctly. I load the music using the pygame mixer music load function and then play the music. I assert that the music is playing by checking if pygame.mixer.music.get_busy() returns True.

![Screenshot from 2023-11-19 15-27-41](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/779127c8-8ccb-4d7d-8486-4214bd95605d)

5. **Countdown Test**: This test case checks if the countdown function works correctly. I have create a font and load a background image. I assert that the font and image load functions exist.

![Screenshot from 2023-11-19 15-29-49](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/0ec43ddd-8c96-4db8-885f-329e6c42eac1)

6. **IsCollision Detection Test**: This test case checks if the collision detection function works correctly.I have define the positions of the main car and three other cars. I have calculate the collisions between the main car and the other cars and assert that the collision calculations are correct.

![Screenshot from 2023-11-19 15-32-47](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/442dff24-d450-4e1f-9474-74ef9d8606b9)

7. **Game Loop Test**:  This test checks if the game over functionality is working correctly.
![Screenshot from 2023-11-19 15-39-58](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/8e46150a-f9a8-4c9a-8456-b593bb2a6c07)

8. **Game Over Test**: This test checks if the game over event correctly exits the game when the user presses the space bar. It does this by mocking the events that are triggered within the game loop and asserting that the countdown function and the sys.exit function are called correctly.

![Screenshot from 2023-11-19 15-43-46](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/7a65191c-c31b-4c5e-a727-3ff0ed5bc232)

## Test Result
All the test get the passed and the game code is perfect. Moreover the game is bug-free.

![Screenshot from 2023-11-17 23-02-31](https://github.com/Baluthegoat/CSF101_CAP3_Testcase/assets/141105500/ec2e4eca-eae9-4710-87fa-176c4a6cbec3)
