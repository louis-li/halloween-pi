import RPi.GPIO as GPIO, time
import os, random

red_light = 12
yellow_light =13
green_light = 15
blue_light = 11
fifth_light = 16

color_red = 32
color_blue = 36
color_green=38

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(green_light,GPIO.OUT)
GPIO.setup(yellow_light,GPIO.OUT)
GPIO.setup(blue_light,GPIO.OUT)
GPIO.setup(fifth_light,GPIO.OUT)

GPIO.setup(31, GPIO.IN)

def play_music():
    no = random.randint(1,13)
    print(no)
    if (no == 1):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/01_Monster_Parade.mp3')
    elif (no == 2):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/03_Love_song_by_a_ghost_duet.mp3')
    elif (no == 3):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/05_We_all_gonna_die.mp3')
    elif (no == 4):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/05_We_all_gonna_die.mp3')
    elif (no == 5):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/06_The_graveyard.mp3')
    elif (no == 6):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/08_The_Swamp.mp3')
    elif (no == 7):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/09_Hello_Michael.mp3')
    elif (no == 8):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/10_The_Witch_Are_Going_Magical.mp3')
    elif (no == 9):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/11_The_Old_Witch_Place.mp3')
    elif (no == 10):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/13_Ghost_Surf_Rock.mp3')
    elif (no == 11):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/hallowneen/halloween_music/08_-_MICKEY_MAOS.mp3')
    elif (no == 12):
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/Halloween_-_06_-_Evil_Makings.mp3')
    else:
        os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/halloween/halloween_music/12_Halloween_Ghost_Party.mp3')
    print('music is over')

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

#Main        
current_state = 0
print('Pending')
try:
    while True:
        current_state = GPIO.input(31)
	GPIO.output(red_light, True)
	GPIO.output(yellow_light, True)
	GPIO.output(blue_light, True)
	GPIO.output(green_light, True)
	GPIO.output(fifth_light,True)
        if current_state == 1:
            print('motion detected')
            play_music()
            GPIO.setup(red_light, GPIO.OUT)
            GPIO.setup(green_light,GPIO.OUT)
            GPIO.setup(yellow_light,GPIO.OUT)
            GPIO.setup(blue_light,GPIO.OUT)
            GPIO.setup(fifth_light,GPIO.OUT)


except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

