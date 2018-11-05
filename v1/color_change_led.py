import RPi.GPIO as GPIO, time
import os, random

red_light = 7
yellow_light =13
green_light = 15
blue_light = 11

color_red = 31
color_blue = 37
color_green=33

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(green_light,GPIO.OUT)
GPIO.setup(yellow_light,GPIO.OUT)
GPIO.setup(blue_light,GPIO.OUT)

GPIO.setup(color_blue,GPIO.OUT)
GPIO.setup(color_red,GPIO.OUT)
GPIO.setup(color_green,GPIO.OUT)

GPIO.setup(29, GPIO.IN)

def play_music():
    no = random.randint(1,9)
    if (no == 1):
        os.system('omxplayer -o alsa /home/pi/halloween_music/cuckoo-clock.mp3')
    elif (no == 2):
        os.system('omxplayer -o alsa /home/pi/halloween_music/evil-laugh.mp3')
    elif (no == 3):
        os.system('omxplayer -o alsa /home/pi/halloween_music/female-scream.mp3')
    elif (no == 4):
        os.system('omxplayer -o alsa /home/pi/halloween_music/funeral-bells.mp3')
    elif (no == 5):
        os.system('omxplayer -o alsa /home/pi/halloween_music/ghost-scream.mp3')
    elif (no == 6):
        os.system('omxplayer -o alsa /home/pi/halloween_music/glados-hello-where-are-you.mp3')
    elif (no == 7):
        os.system('omxplayer -o alsa /home/pi/halloween_music/glados-laugh.mp3')
    elif (no == 8):
        os.system('omxplayer -o alsa /home/pi/halloween_music/howling-wolf.mp3')
    else:
        os.system('omxplayer -o alsa /home/pi/halloween_music/thriller-laugh.mp3')


def time_sleep():
    no = random.randint(1,5)
    if   (no == 1):
        return 0.5
    elif (no == 2):
        return 0.1
    elif (no == 3):
        return 0.25
    elif (no == 4):
        return 1
    elif (no == 5):
        return 0.05
        
def lights():
    t =0.1
    t = time_sleep()
    no = random.randint(1,4)
    if (no == 1):
        GPIO.output(red_light, True)
        time.sleep(t)
        GPIO.output(red_light, False)
    elif (no == 2):
        GPIO.output(blue_light, True)
        time.sleep(t)
        GPIO.output(blue_light, False)
    elif (no == 3):
        GPIO.output(green_light, True)
        time.sleep(t)
        GPIO.output(green_light, False)
    elif (no == 4):
        GPIO.output(yellow_light, True)
        time.sleep(t)
        GPIO.output(yellow_light, False)

    no = random.randint(1,7)
    if (no > 3):
        GPIO.output(color_red,True)
        no = no - 4
    if (no > 1):
        GPIO.output(color_blue,True)
        no = no -2
    if (no ==1 ):
        GPIO.output(color_green,True)
    time.sleep(t)    
    GPIO.output(color_green,False)
    GPIO.output(color_blue,False)
    GPIO.output(color_red,False)
        
current_state = 0
try:
    while True:
        current_state = GPIO.input(29)
        if current_state == 1:
            print 'motion sensor'
            GPIO.output(red_light, True)
            GPIO.output(yellow_light, True)
            GPIO.output(blue_light, True)
            GPIO.output(green_light, True)
            GPIO.output(color_blue,True)
            play_music()
            GPIO.output(yellow_light, False)
            GPIO.output(blue_light, False)
            GPIO.output(green_light, False)
            GPIO.output(red_light, False)
            for i in range (25):
                lights() 


except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

