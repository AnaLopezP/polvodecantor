from turtle import *
#CONSTRUCCIÓN FRACTAL
def square(size):
    for i in range(4):
        forward(size)
        left(90)
def cantor(size, tolerance):
    init = pos()
    penup()
    goto(init + (size/3, size/3))
    pendown()
    square(size/3)
    if size/3<tolerance:
        return
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            if i==1 and j == 1:
                continue
            penup()
            goto(init + (i*size/3, j*size/3))
            cantor(size/3, tolerance)
if __name__ == '__main__':
    color('red', 'yellow')
    speed(0)
    size = 100
    penup()
    goto(-size/2, -size/2)
    pendown()
    begin_fill()
    square(size)
    cantor(size, 2)
    end_fill()
    done()