from turtle import *

state= {'turn':0}           #initially our spinner state will be null or stable


#we will define our spin function
def spinner():
    "Draw fidget spinner."
    clear()
    angle=state['turn']/5
    left(angle)                     #left means our spinner will rotate in anticlockwise and /// right means clockwise
    forward(100)                    #move forward with distance of 100

    #we will create a dot
    dot(120,'red')                  #120 is the size of dot
    back(100)
    left(120)
    forward(100)
    dot(120,'blue')                 #second dot
    back(100)
    left(120)
    forward(100)
    dot(120,'green')                 #third dot
    back(100)
    left(120)
    update()                        # it will update our step which we insert in our function


def animate():
    "Animate fidget spinner"

    #we will first check whether the state is 0 or not
    #if it is not 0 we will make it 0 by decrementing it with 1 in every time

    if state['turn']>0:
        state['turn']-=1

    spinner()                       #we will call that function till our spinner stops rotating
    ontimer(animate,20)             #we will install timer that calls animate after every 20 milliseconds


def flick():
    "Flick widget spinner"
    state['turn']+=50

hideturtle()                        #we will hide our turtle once our drawing part is done
tracer(False)                       #it turns animation to it's original state completion of rotation
#width(20)
onkey(flick,'space')                #by pressing what key spinner to rotate i have used space here
listen()                            # it will listen our space key ..... no of times you press it wil add and speed of spinner also increase
animate()
done()            