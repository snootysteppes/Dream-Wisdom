import pygame
import RPi.GPIO as GPIO
import random
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 

# Set up Pygame
pygame.init()
pygame.mixer.init() # pygame sounds
 

# Function to be called when button 1 is pressed, can change file path
def fact(): # random fact
    rand_fact = random.randint(1,5)
    if rand_fact == 1:
        pygame.mixer.music.load("/home/stemclub/Documents/compressed/gold.wav")
        pygame.mixer.music.play()
    elif rand_fact == 2:
        pygame.mixer.music.load("/home/stemclub/Documents/compressed/germanic.wav")
        pygame.mixer.music.play()
    elif rand_fact == 3:
        pygame.mixer.music.load("/home/stemclub/Documents/compressed/filmloc.wav")
        pygame.mixer.music.play()
    elif rand_fact == 4:
        pygame.mixer.music.load("/home/stemclub/Documents/compressed/skincell.wav")
        pygame.mixer.music.play()
    elif rand_fact == 5:
        pygame.mixer.music.load("/home/stemclub/Documents/compressed/chocolate.wav")
        pygame.mixer.music.play()
    time.sleep(1)
 
# Function to be called when button 2 is pressed
def relax():
    print("Playing relaxing music")
    music_random = random.randint(1,5)
    if music_random == 1:
        music1 = pygame.mixer.music.load("/home/stemclub/Documents/music//1.wav")
        pygame.mixer.music.play()
    elif music_random == 2:
        music2 = pygame.mixer.music.load("/home/stemclub/Documents/music//2.wav")
        pygame.mixer.music.play()
    elif music_random == 3:
        music3 = pygame.mixer.music.load("/home/stemclub/Documents/music//3.wav")
        pygame.mixer.music.play()
    elif music_random == 4:
        music4 = pygame.mixer.music.load("/home/stemclub/Documents/music//4.wav")
        pygame.mixer.music.play()
    elif music_random == 5:
        music5 = pygame.mixer.music.load("/home/stemclub/Documents/music//5.wav")
        pygame.mixer.music.play()
 
# Main game loop
while True:
    # Check if button 1 is pressed
    if not GPIO.input(17):
        fact()
        time.sleep(1)
 
    # Check if button 2 is pressed
    if not GPIO.input(27):
        relax() 
    
    if not GPIO.input(21):
        print("Stopping all sounds")
        pygame.mixer.music.load("/home/stemclub/Music/silence.wav") # as an alternative to stopping the music, which doesn't seem to work, we just replace the sound with a 1 second wav file of silence.
        pygame.mixer.music.play()
        time.sleep(0)
 
    # Pygame event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GPIO.cleanup()
            quit()
