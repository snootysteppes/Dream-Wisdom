import pygame
import RPi.GPIO as GPIO
import random

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up Pygame
pygame.init()
pygame.mixer.init()  # pygame sounds

# Function to play random fact
def play_fact():
    fact_files = [
        "/home/stemclub/Documents/compressed/gold.wav",
        "/home/stemclub/Documents/compressed/germanic.wav",
        "/home/stemclub/Documents/compressed/filmloc.wav",
        "/home/stemclub/Documents/compressed/skincell.wav",
        "/home/stemclub/Documents/compressed/chocolate.wav"
    ]
    rand_fact = random.choice(fact_files)
    pygame.mixer.music.load(rand_fact)
    pygame.mixer.music.play()

# Function to play random music
def play_music():
    music_files = [
        "/home/stemclub/Documents/music/1.wav",
        "/home/stemclub/Documents/music/2.wav",
        "/home/stemclub/Documents/music/3.wav",
        "/home/stemclub/Documents/music/4.wav",
        "/home/stemclub/Documents/music/5.wav"
    ]
    music_file = random.choice(music_files)
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

# Main game loop
while True:
    # Check if button 1 is pressed
    if not GPIO.input(17):
        play_fact()

    # Check if button 2 is pressed
    if not GPIO.input(27):
        play_music()

    # Check if button 3 is pressed
    if not GPIO.input(21):
        print("Stopping all sounds")
        pygame.mixer.music.load("/home/stemclub/Music/silence.wav")
        pygame.mixer.music.play()

    # Pygame event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GPIO.cleanup()
            quit()
