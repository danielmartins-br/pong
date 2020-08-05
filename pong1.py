import turtle

janela = turtle.Screen()
janela.title("Pong by printf")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

#Player A
player_a = turtle.Turtle() #objeto do player A
player_a.speed(0)
player_a.shape("square")
player_a.color("green")
#tamanho do player
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-380,0)

#Player B
player_b = turtle.Turtle() #objeto do player B
player_b.speed(0)
player_b.shape("square")
player_b.color("green")
#tamanho do player
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(380,0)

#Bola
bola = turtle.Turtle() #objeto da bola
bola.speed(0)
bola.shape("square")
bola.color("white")
#tamanho do player
bola.penup()
bola.goto(0,0)

#loop principal do game
while True:
     janela.update()
