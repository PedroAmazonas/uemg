import turtle,matplotlib,numpy
import matplotlib.pyplot
def media():
	media=0
	notas=[]
	while len(notas) <6:
		nota=float(input("Dijite a nota:"))
		notas.append(nota)
	for i in notas:
		media+=i
	media/=len(notas)
	print(f"media:{media}")
#media()

def menor():
	menor=0
	count=0
	while count<10:
		numero=int(input("dijite um número:"))
		if count==0 :
			menor=numero
		if numero<menor:
			menor=numero
		count+=1
	print(f"menor: {menor}")
#menor()

def matematica():
	x = -5
	while x <=5:
		print(f"x:{x},y={5*x+2}")
		x+=1
#matematica()

def salario():
	dias=int(input("quantas dias você trabalhou"))
	salario=dias*8*25
	print(f"salario: {salario}")
#salario()

def fatorial():
	num=int(input('Dijite um numero'))
	c=num
	while c > 1:
		num *= c-1
		c-=1
	print(f"fatorial {num}")
#fatorial()

def fibonacci(elem):
	l=[1,1]
	for i in range(1,elem-1):
		l.append(l[-1]+l[-2])
	print(l)
#fibonacci(10)

def tabauda(num):
	for i in range(1,10+1):
		print(f"{i} * {num} = {i*num}")
#tabauda(8)

def numeros(*args):
		numl=[]
		for i in args:
			numl.append(i)
		print(args)
		print(numl)	

		print(f"menor:{min(numl)}\nmaior:{max(numl)}")
		print(f"soma:{sum(numl)}\nmédia:{sum(numl)/len(numl)}")
#numeros(1,2,3,4,5,6,7,8,9,10)
def Triangulo(t,side,retas):
	n=int(360/retas)
	m=int(360/n)
	for _ in range(m):
		t.forward(side)
		t.left(n)
	t.clear()	
	t= turtle.Turtle()	
	ts=turtle.Screen()
	ts.exitonclick()	
	#ts.setworldcoordinates(0, 0,1000,)
	t.screen.setup (width=800, height=600, startx=-5, starty=-5)
	t.pendown			
#Triangulo(t,90)
def funcao(a,b,c):
	x=numpy.linspace(-20,20,400)
	y=a*x**2+b*x+c
	matplotlib.pyplot.xlabel("X")
	matplotlib.pyplot.ylabel("f(X)")
	matplotlib.pyplot.title("Função de Segundo Grau")
	matplotlib.pyplot.grid(True)
	matplotlib.pyplot.plot(x,y)
	matplotlib.pyplot.show()
funcao(2,2,3)
def Barra(t,heigth):
	def drawBar(t, height):
		""" Get turtle t to draw one bar, of height. """
		t.begin_fill()               # start filling this shape
		t.left(90)
		t.forward(height)
		t.write(str(height))
		t.right(90)
		t.forward(40)
		t.right(90)
		t.forward(height)
		t.left(90)
		t.end_fill()                 # stop filling this shape

	xs = [88,48, 117, 200, 240, 160, 260, 220]  #
	maxheight = max(xs)
	numbars = len(xs)
	border = 10
	ts.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
	for a in xs:
		drawBar(t, a)
#Barra(t,25)		
