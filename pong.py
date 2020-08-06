import turtle

janela = turtle.Screen()
janela.title("Pong by printf")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

#Score
score_a = 0
score_b = 0

#Player A
player_a = turtle.Turtle() #objeto do player A
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=4, stretch_len=1) #tamanho do player
player_a.penup()
player_a.goto(-380,0)

#Player B
player_b = turtle.Turtle() #objeto do player B
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=4, stretch_len=1) #tamanho do player
player_b.penup()
player_b.goto(380,0)

#Bola
bola = turtle.Turtle() #objeto da bola
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.ex = 0.1 #define a velocidade da bola no eixo x e y na velocidade de 2 pixels 
bola.ey = 0.1

#Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Player A: 0 PlayerB: 0", align="center", font=("Courier",24, "normal"))


#Movimento do Player A
def player_a_up():
     y = player_a.ycor()
     y += 20 
     player_a.sety(y)

def player_a_down():
     x = player_a.ycor()
     x -= 20
     player_a.sety(x)

#Movimento do Player B
def player_b_up():
     y = player_b.ycor()
     y += 20 
     player_b.sety(y)

def player_b_down():
     x = player_b.ycor()
     x -= 20
     player_b.sety(x)


#Mapeamento de Teclado
janela.listen()
janela.onkeypress(player_a_up, "w")
janela.onkeypress(player_a_down, "s")
janela.onkeypress(player_b_up, "Up")
janela.onkeypress(player_b_down, "Down")


#loop principal do game
while True:
     janela.update()

     #Move a bola
     bola.setx(bola.xcor() + bola.ex)
     bola.sety(bola.ycor() + bola.ey)

     #Checa a borda
     if bola.ycor() > 290:
          bola.sety(290)
          bola.ey *= -1

     if bola.ycor() < -290:
          bola.sety(-290)
          bola.ey *= -1


     if bola.xcor() > 390:
          bola.goto(0,0)
          bola.ex *= -1
          score_a += 1
          placar.clear()
          placar.write("Player A: {}  PlayerB: {}".format(score_a,score_b), align="center",font=("Courier",24, "normal"))

     if bola.xcor() < -390:
          bola.goto(0,0)
          bola.ex *= -1
          score_b += 1
          placar.clear()
          placar.write("Player A: {}  PlayerB: {}".format(score_a,score_b), align="center",font=("Courier",24, "normal"))


     #Colisao da bola com os players
     if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < player_b.ycor() + 40 and bola.ycor() > player_b.ycor() -40):
          bola.setx(340)
          bola.ex *= -1

     if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < player_a.ycor() + 40 and bola.ycor() > player_a.ycor() -40):
          bola.setx(-340)
          bola.ex *= -1


