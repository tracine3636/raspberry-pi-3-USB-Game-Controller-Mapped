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





#Left Vertical Joystick--------------------
    L_verticalaxis = joystick.get_axis(1)
    if L_verticalaxis < -0.1:

        print('Left Joystick Up, left shoulder moves up')
        GPIO.output(6, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(6, GPIO.LOW)

    L_verticalaxis = joystick.get_axis(1)
    if L_verticalaxis > 0.1:

        print('Left Joystick Down, left shoulder moves down')
        GPIO.output(12, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(12, GPIO.LOW)

#Left Horizontal Joystick------------------
    L_horizontalaxis = joystick.get_axis(0)
    if L_horizontalaxis < -0.1:

        print('Left Joystick Left, left shoulder moves left')
        GPIO.output(19, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(19, GPIO.LOW)

    L_horizontalaxis = joystick.get_axis(0)
    if L_horizontalaxis > 0.1:

        print('Left Joystick Right, left shoulder moves right')
        GPIO.output(20, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(20, GPIO.LOW)

#Right Vertical Joystick-------------------
    R_verticalaxis = joystick.get_axis(3)
    if R_verticalaxis < -0.1:

        print('Right Joystick Up, right shoulder moves up')
        GPIO.output(25, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(25, GPIO.LOW)

    R_verticalaxis = joystick.get_axis(3)
    if R_verticalaxis > 0.1:

        print('Right Joystick Down, right shoulder moves down')
        GPIO.output(24, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(24, GPIO.LOW)

#Right Horizontal Joystick----------------
    R_horizontalaxis = joystick.get_axis(2)
    if R_horizontalaxis < -0.1:

        print('Right Joystick Left. right shoulder moves left')
        GPIO.output(10, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(10, GPIO.LOW)

    R_horizontalaxis = joystick.get_axis(2)
    if R_horizontalaxis > 0.1:

        print('Right Joystick Right, right shoulder moves right')
        GPIO.output(9, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(9, GPIO.LOW)


#L1_Button--------------------------------
    L1 = joystick.get_button(6)
    if L1:
        print ('L1 button, left wrist moves up')
        GPIO.output(18, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(18, GPIO.LOW)

#L2_Button-------------------------------
    L2 = joystick.get_button(8)
    if L2:
        print ('L2 button, left wrist moves down')
        GPIO.output(17, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(17, GPIO.LOW)

#R1_Button-------------------------------
    R1 = joystick.get_button(7)
    if R1:
        print ("R1 button, right wrist moves up")
        GPIO.output(2, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(2, GPIO.LOW)

#R2_Button-------------------------------
    R1 = joystick.get_button(9)
    if R1:
        print ("R2 button, right wrist moves down")
        GPIO.output(3, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(3, GPIO.LOW)

#Y_Button-------------------------------
    Y = joystick.get_button(4)
    if Y:
        print ("Y button, left forearm moves up")
        GPIO.output(13, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(13, GPIO.LOW)

#X_Button-------------------------------
    X = joystick.get_button(3)
    if X:
        print ("X button, right forearm moves up")
        GPIO.output(26, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(26, GPIO.LOW)

#B_Button-------------------------------
    B = joystick.get_button(1)
    if B:
        print ("B button, right forearm moves down")
        GPIO.output(27, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(27, GPIO.LOW)

#A_Button-------------------------------
    A = joystick.get_button(0)
    if A:
        print ("A button, left forearm moves down")
        GPIO.output(16, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(16, GPIO.LOW)

#SELECT_Button-------------------------
    SELECT = joystick.get_button(10)
    if SELECT:
        print ("SELECT button, left gripper  opens")
        GPIO.output(5, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(5, GPIO.LOW)


#START_Button--------------------------
    START= joystick.get_button(11)
    if START:
        print ("START button, right gripper opens")
        GPIO.output(23, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(23, GPIO.LOW)


#L_Click_Button------------------------
    L_CLICK= joystick.get_button(13)
    if L_CLICK:
        print ("L_CLICK, left gripper closes")
        GPIO.output(4, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(4, GPIO.LOW)


#R_Click_Button------------------------
    R_CLICK= joystick.get_button(14)
    if R_CLICK:
        print ("R_CLICK button, right gripper closes")
        GPIO.output(22, GPIO.HIGH)
        sleep(0.3)
        GPIO.output(22, GPIO.LOW)

#------------------------------------=
#left joystick = Axis1, Axis=0
#right joystick= Axis3, Axis=2
#0=A
#1=B
#2
#3=X
#4=Y
#5=
#6=L1
#8=L2
#7=R1
#9=R2
#4=Y
#10=SELECT
#11=START
#12
#13=L_CLICK
#14=R_CLICK

#----------------------------------------------------
pygame.quit()


