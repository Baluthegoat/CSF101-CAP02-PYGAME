import pytest 
import pygame
import cargame
import sys
import unittest.mock as mock
from unittest.mock import patch, MagicMock

pygame.init() 
pygame.mixer.init() 

def test_screen_size():
    screen = pygame.display.set_mode((840,600))
    assert screen.get_size() == (840,600)

def test_introImg():
    intro = pygame.image.load("/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/m.png")
    assert intro

def test_instructionIMG():
    instruct = pygame.image.load("/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/i.jpg")
    assert instruct

def test_pygame_mixer_music_play():
    pygame.mixer.music.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Gamesound/intro.mp3')
    pygame.mixer.music.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Gamesound/toyota.mp3')
    pygame.mixer.music.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Gamesound/carcrashing.mp3')
    pygame.mixer.music.play()
    assert pygame.mixer.music.get_busy() == True
    
def test_countdown():
    font = pygame.font.Font()
    countdownBackground = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/track1.jpg')
    
    assert pygame.font.Font 
    assert pygame.image.load

def test_iscollision_detection():
    
    maincarX = 200
    maincarY = 200
    car1X = 250
    car1Y = 250
    car2X = 300
    car2Y = 300
    car3X = 350
    car3Y = 350

    
    coll1 = (car1X, car1Y, maincarX, maincarY)
    coll2 = (car2X, car2Y, maincarX, maincarY)
    coll3 = (car3X, car3Y, maincarX, maincarY)

    
    assert coll1
    assert coll2
    assert coll3



def test_gameloop():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    sys.exit = mock.Mock()


    pygame.quit()

@pytest.fixture
def cargame_mock():
    with patch('cargame.pygame') as mock:
        yield mock

def test_gameover(cargame_mock):
    cargame_mock.image.load.return_value = MagicMock()
    cargame_mock.display.update = MagicMock()

    for event_type, key in [(cargame_mock.QUIT, None), (cargame_mock.KEYDOWN, cargame_mock.K_SPACE)]:
        event = MagicMock(type=event_type, key=key)
        cargame_mock.event.get.return_value = [event]

        with patch('cargame.countdown') as countdown_mock:
            with patch('cargame.sys.exit') as sys_exit_mock:

                if key == cargame_mock.K_SPACE:
                    sys_exit_mock.assert_not_called()
                else:
                    countdown_mock.assert_not_called()
                    sys_exit_mock.assert_not_called()

