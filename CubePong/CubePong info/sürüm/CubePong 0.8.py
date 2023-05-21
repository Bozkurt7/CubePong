import turtle, random
import winsound

s = input("istediğin kelimeyi gir: ")

l = input("istediğin kelimeyi gir: ")

def start_screen():
    turtle.setup(width=1200, height=750)
    turtle.bgcolor("#2600ff")
    turtle.title("Start Screen")

    çizgi1 = turtle.Turtle()
    çizgi1.speed(0.25)
    çizgi1.shape('square')
    çizgi1.color('#ff0000')
    çizgi1.penup()
    çizgi1.goto(520, 0)
    çizgi1.shapesize(100, 50)

    title = turtle.Turtle()
    title.color("white")
    title.penup()
    title.setpos(-410, 250)
    title.write("CubePong'a Hoş Geldiniz", font=("Arial", 50, "bold"))
    
    button = turtle.Turtle()
    button.color("white")
    button.shape("square")
    button.shapesize(6, 12)
    button.penup()
    button.setpos(20, -15)

    button_text = turtle.Turtle()
    button_text.color("black")
    button_text.penup()
    button_text.setpos(-50, -50)
    button_text.write("Start", font=("Arial", 48, "bold")) 
     
    button_text = turtle.Turtle()
    button_text.color("black")
    button_text.penup()
    button_text.setpos(-580, -355)
    button_text.write("CRATED BY İSMAİL BURAK ÖZÇİFTÇİ ", font=("Arial", 18, "bold"))



    def play_game(x, y):
        turtle.bye()  
        game()
    
    turtle.onscreenclick(play_game)
    turtle.mainloop()

def game():
    turtle.setup(width=800, height=600)
    turtle.bgcolor("white")
    turtle.title("Start")
    turtle.mainloop()

start_screen()

import turtle, random
import winsound

pencere = turtle.Screen()
pencere.title("CubePong⚽")
pencere.bgcolor("#26d15c")
pencere.setup(width=1500, height=900)
pencere.tracer(0)

çizgic = turtle.Turtle()
çizgic.speed(0.25)
çizgic.shape('square')
çizgic.color('white')
çizgic.penup()
çizgic.goto(-550, 0)
çizgic.shapesize(25, 0.50)

çizgid = turtle.Turtle()
çizgid.speed(0.25)
çizgid.shape('square')
çizgid.color('white')
çizgid.penup()
çizgid.goto(550, 0)
çizgid.shapesize(25, 0.50)

çizgia = turtle.Turtle()
çizgia.speed(0.25)
çizgia.shape('square')
çizgia.color('white')
çizgia.penup()
çizgia.goto(-695, 255)
çizgia.shapesize(0.50, 15)

çizgib = turtle.Turtle()
çizgib.speed(0.25)
çizgib.shape('square')
çizgib.color('white')
çizgib.penup()
çizgib.goto(-695, -255)
çizgib.shapesize(0.50, 15)

çizgia = turtle.Turtle()
çizgia.speed(0.25)
çizgia.shape('square')
çizgia.color('white')
çizgia.penup()
çizgia.goto(695, -255)
çizgia.shapesize(0.50, 15)

çizgib = turtle.Turtle()
çizgib.speed(0.25)
çizgib.shape('square')
çizgib.color('white')
çizgib.penup()
çizgib.goto(695, 255)
çizgib.shapesize(0.50, 15)

t = turtle.Turtle()
t.speed(1.50)
t.shape('circle')
t.color('white')
t.penup()
t.shapesize(15, 15)
t.dx = 0.5000
t.dy = 0.5000

t = turtle.Turtle()
t.speed(1.50)
t.shape('circle')
t.color('#26d15c')
t.penup()
t.shapesize(14, 14)
t.dx = 0.5000
t.dy = 0.5000

çizgi = turtle.Turtle()
çizgi.speed(0.25)
çizgi.shape('square')
çizgi.color('white')
çizgi.penup()
çizgi.goto(0, 0)
çizgi.shapesize(45, 0.50)


raket_a = turtle.Turtle()
raket_a.speed(0.25)
raket_a.shape('square')
raket_a.color('blue')
raket_a.penup()
raket_a.goto(-575, 0)
raket_a.shapesize(8, 3)


raket_b = turtle.Turtle()
raket_b.speed(0.25)
raket_b.shape('square')
raket_b.color('red')
raket_b.penup()
raket_b.goto(575, 0)
raket_b.shapesize(8, 3)



ball = turtle.Turtle()
ball.speed(1.50)
ball.shape('circle')
ball.color('black')
ball.shapesize(1.7, 1.7)
ball.penup()
ball.dx = 0.85
ball.dy = 0.85

yazi = turtle.Turtle()
yazi.speed(0)
yazi.color('white')
yazi.penup()
yazi.goto(0, 380)
yazi.write("{}:0   {}:0".format(s, l), align='center', font=('Courier', 35, 'bold'))
yazi.hideturtle()
puan_a = 0
puan_b = 0


def raket_a_up():
    y = raket_a.ycor()
    y = y + 20
    raket_a.sety(y)

def raket_a_down():
    y = raket_a.ycor()
    y = y - 20
    raket_a.sety(y)

def raket_a_right():
    x = raket_a.xcor()
    x = x + 20
    raket_a.setx(x)

def raket_a_left():
    x = raket_a.xcor()
    x = x - 20
    raket_a.setx(x)



def raket_b_up():
    y = raket_b.ycor()
    y = y + 20
    raket_b.sety(y)

def raket_b_down():
    y = raket_b.ycor()
    y = y - 20
    raket_b.sety(y)

def raket_b_right():
    x = raket_b.xcor()
    x = x + 20
    raket_b.setx(x)

def raket_b_left():
    x = raket_b.xcor()
    x = x - 20
    raket_b.setx(x)


raket_a_puan = 0
raket_b_puan = 0


pencere.listen()
pencere.onkeypress(raket_a_up, 'w')
pencere.onkeypress(raket_a_down, 's')
pencere.onkeypress(raket_a_right, 'd')
pencere.onkeypress(raket_a_left, 'a')

pencere.onkeypress(raket_b_up, 'Up')
pencere.onkeypress(raket_b_down, 'Down')
pencere.onkeypress(raket_b_right, 'Right')
pencere.onkeypress(raket_b_left, 'Left'),




while True:
    pencere.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>370 or ball.ycor()<-390:
        ball.dy = ball.dy * -1
    

    if ball.xcor()>800:
        winsound.PlaySound('f', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        puan_a = puan_a + 1
        yazi.clear()
        yazi.write("{}:{}   {}:{}".format(s, puan_a, l, puan_b), align='center', font=('Courier', 35, 'bold'))
    if ball.xcor()<-800:
        winsound.PlaySound('f', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        puan_b = puan_b + 1
        yazi.clear()
        yazi.write("{}:{}   {}:{}".format(s, puan_a, l, puan_b), align='center', font=('Courier', 35, 'bold'))


    if raket_a.ycor() + 5 >= 500:
        raket_a.sety(250)
    if raket_b.ycor() + 5 >= 500:
        raket_b.sety(250)
    if raket_a.ycor() - 5 <= -500:
        raket_a.sety(-250)
    if raket_b.ycor() - 5 <= -500:
        raket_b.sety(-250)

    if raket_a.xcor() + 5 >= 750:
        raket_a.setx(535)
    if raket_b.xcor() + 5 >= 750:
        raket_b.setx(535)
    if raket_a.xcor() - 5 <= -750:
        raket_a.setx(-535)
    if raket_b.xcor() - 5 <= -750:
        raket_b.setx(-535)

    if (ball.xcor()>540 and ball.xcor()<550) and (ball.ycor()<raket_b.ycor()+60 and ball.ycor()>raket_b.ycor()-60):
        winsound.PlaySound('f.wav', winsound.SND_ASYNC)
        ball.setx(540)
        ball.dx = ball.dx * -1

    if (ball.xcor()<-540 and ball.xcor()>-550) and (ball.ycor()<raket_a.ycor()+60 and ball.ycor()>raket_a.ycor()-60):
        winsound.PlaySound('f.wav', winsound.SND_ASYNC)
        ball.setx(-540)
        ball.dx = ball.dx * -1
        
    if (ball.xcor()>540 and ball.xcor()<550) and (ball.ycor()<raket_b.ycor()+60 and ball.ycor()>raket_b.ycor()-60):
        winsound.PlaySound('g1.wav', winsound.SND_ASYNC)
        ball.setx(540)
        ball.dx = ball.dx * -1
        ball.dx += 10
        ball.dy += 10
    if (ball.xcor()<-540 and ball.xcor()>-550) and (ball.ycor()<raket_a.ycor()+60 and ball.ycor()>raket_a.ycor()-60):
        winsound.PlaySound('g1.wav', winsound.SND_ASYNC)
        ball.setx(-540)
        ball.dx = ball.dx * -1
        ball.dx += 10
        ball.dy += 10
