import turtle as tr

s = tr.Screen()

tr.setup(800, 800)
s.bgcolor('black')
tr.speed(200)
tr.tracer(400)
tr.pensize(1)
col = ('blue','green','white','orange')

for i in range(3):
    for n in range(400):
        tr.color(col[n%4])
        tr.circle(190-n/2,90)
        tr.left(90)
        tr.circle(190-n/2,90)
        tr.color(col[n%4])
    tr.left(30)
s.exitonclick()