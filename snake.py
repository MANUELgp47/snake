import turtle
import time
import random 
#-----------------------------------------------------Sin refactorizar
delay =0.1
body = [] #se agregan los segmentos a la serpiente 
velocidad=20
score=0
record=0

wn=turtle.Screen()# crea ventana

#parametros de la ventana
wn.title("Juego serpiente")
wn.setup(width=600, height=600)#tamaño
wn.bgcolor("white")#background color

#cabeza
#Turtle obj
head=turtle.Turtle()
head.speed(0)
head.shape('circle')#forma
head.color("green")
head.penup()#para que no deje rastro
head.goto(0,0)#pos de salida
#para que espere una instrucción 
head.direction="stop"

#config comida
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)
food.direction="stop"


#score
text= turtle.Turtle()
text.speed(0)
text.penup()
text.hideturtle()#Esconder la clecha (cabeza)
text.goto(0,260)
text.write(f'Puntos 0       Record 0', align="center", font=("calibri", 24))
#funciones----------------
def mov():
    #Movimiento hacer con switch mas adelante
    
    if head.direction=="up":
        #almacenar el valor acutal de la coordenada
        y= head.ycor()#recive la coordenada
        head.sety(y+velocidad)

    if head.direction=="down":
        #almacenar el valor acutal de la coordenada
        y= head.ycor()#recive la coordenada
        head.sety(y-velocidad)

    if head.direction=="right":
        #almacenar el valor acutal de la coordenada
        x= head.xcor()#recive la coordenada
        head.setx(x+velocidad)

    if head.direction=="left":
        #almacenar el valor acutal de la coordenada
        x= head.xcor()#recive la coordenada
        head.setx(x-velocidad)    

def dirUP():
    head.direction="up" 
def dirDown():
    head.direction="down" 
def dirRight():
    head.direction="right" 
def dirLeft():
    head.direction="left"         

def pintataMarcador():
    text.clear()
    text.write(f'Puntos {score}       Record {record}', align="center", font=("calibri", 24))

#conectar la ventana con el teclado
wn.listen()
wn.onkeypress(dirUP, "Up")# si no está en mayuscula falla 
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")

#main
while True:
    wn.update()
    
    
    #colisiones con la ventana
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #eliminar segmento( no los borra solo los esconde )
        # luego los elimina del vector
        for seg in body:
            seg.goto(1000, 1000)

        body.clear()
        score=0
        pintataMarcador()

    #colisiones de cabeza y comida
    if head.distance(food)<20:#cuando esté a menos de 20 px de food
        x= random.randint(-280, 280)
        y= random.randint(-280, 280)
        food.goto(x, y)#mueve laa comida a otro sitio si la toca

        #agrega segmento al comer
        segment=turtle.Turtle()
        segment.speed(0)
        segment.shape('circle')
        segment.color("blue")
        segment.penup()
        body.append(segment)

        
        score +=1
        if score > record:
            record=score
            
        pintataMarcador()

    totalSeg = len(body)
    for i in range(totalSeg-1 , 0, -1): #numeros del n al 0 decrementando de -1
        x= body[i-1].xcor()
        y= body[i-1].ycor()
        body[i].goto(x, y)#el i va hacia el i-1 (siguiendolo)

    if totalSeg > 0: # si ya hay segmentos
        x= head.xcor()    
        y = head.ycor()
        body[0].goto(x, y)#el primer segmiento sigue a la cabeza


    mov()
    #colision con el cuerpo
    for seg in body:
        if seg.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            for seg in body:
                seg.goto(1000, 1000)

            body.clear()
            score=0
            pintataMarcador()


    
    time.sleep(delay)
turtle.done()