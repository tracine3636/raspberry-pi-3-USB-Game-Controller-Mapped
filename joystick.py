import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)


import pygame


pygame.init()

clock = pygame.time.Clock()

FPS = 30

running = True



#basic do joystick

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)

joystick.init()

screen = pygame.display.set_mode((400,300))

pygame.display.set_caption('Control')





while running:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

    clock.tick(FPS)

    pygame.display.update()

    verticalaxis1 = joystick.get_axis(1)

    if verticalaxis1 < -0.1:
        print('Left Arm Moved Up')
        GPIO.output(12, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(12, GPIO.LOW)

    verticalaxis = joystick.get_axis(1)

    if verticalaxis > 0.1:

        print('Left Arm Moved Down')
        GPIO.output(6, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(6, GPIO.LOW)


    horizontalaxis = joystick.get_axis(0)

    if horizontalaxis < -0.1:

        print('Left Shoulder Moved Left')
        GPIO.output(19, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(19, GPIO.LOW)

    horizontalaxis = joystick.get_axis(0)

    if horizontalaxis > 0.1:

        print('Left Shoulder Moved Right')
        GPIO.output(20, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(20, GPIO.LOW)
   
   # verticalaxis2 = joystick.get_axis(3)

    #if verticalaxis2 < -0.1:
     #   print('Right Arm Moved Up')
      #  GPIO.output(24, GPIO.HIGH)
       # sleep(0.1)
        #GPIO.output(24, GPIO.LOW)

    #verticalaxis2 = joystick.get_axis(3)

    #if verticalaxis2 > 0.1:

     #   print('Right Arm Moved Down')
      #  GPIO.output(25, GPIO.HIGH)
       # sleep(0.1)
        #GPIO.output(25, GPIO.LOW)

   # horizontalaxis2 = joystick.get_axis(2)

    #if horizontalaxis2 < -0.1:

     #   print('Right Shoulder Moved Left')
      #  GPIO.output(10, GPIO.HIGH)
       # sleep(0.1)
        #GPIO.output(10, GPIO.LOW)
   
    #horizontalaxis2 = joystick.get_axis(2)

    #if horizontalaxis2 > 0.1:

     #   print('Right Shoulder Moved Right')
      #  GPIO.output(9, GPIO.HIGH)
       # sleep(0.1)
        #GPIO.output(9, GPIO.LOW)

    L1 = joystick.get_button(5)

    if L1:
        print ('Left Fore Arm 1 ')
        GPIO.output(26, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(26, GPIO.LOW)
        

    L2 = joystick.get_button(7)

    if L2:
        print ("Left Fore Arm 2")
        GPIO.output(27, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(27, GPIO.LOW)
        


    R1 = joystick.get_button(6)

    if R1:
        print ('Right Fore Arm 3')
        GPIO.output(13, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(13, GPIO.LOW)
        

    R2 = joystick.get_button(9)

    if R2:
        print ("Right Fore Arm 4")
        GPIO.output(16, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(16, GPIO.LOW)
        

    A = joystick.get_button(0)

    if A:
        print ("Left Gripper Close")
        GPIO.output(4, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(4, GPIO.LOW)
        
   
    B = joystick.get_button(1)
   
    if B:
   
        print ("Right Gripper Close")
        GPIO.output(22, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(22, GPIO.LOW)
        
    Y = joystick.get_button(4)
   
    if Y:
   
        print ("Left Gripper Open")
        GPIO.output(5, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(5, GPIO.LOW)
        

    X = joystick.get_button(3)
   
    if X:
   
        print ("Right Gripper Open")
        GPIO.output(23, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(23, GPIO.LOW)

    START = joystick.get_button(8)
   
    if START:
   
        print ("Left Wrist Down")
        GPIO.output(17, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(17, GPIO.LOW)

    SELECT = joystick.get_button(10)
   
    if SELECT:
   
        print ("Left Wrist Up")
        GPIO.output(18, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(18, GPIO.LOW)

        




pygame.quit()


