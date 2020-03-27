import tkinter
from tkinter import *
from second import e
from useless import out
from tkinter import messagebox
import numpy as np
import copy

gridn = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grid1=[]

def setinitial():
    global gridn
    for i in range(0,9):
        for j in range(0,9):
            gridn[i][j]=0


def inputa(frame):
    global gridn, e, grid1
    setinitial()
    key=0
    k=0
    for i in range(0,9):
        for j in range(0,9):
            if e[k].get()=='':
                pass
            else:
                try:
                    if int(e[k].get(), 10) in range(1,10):
                        gridn[i][j]=(int(e[k].get(),10))
                        #print(grid[i][j])
                    else:
                        messagebox.showinfo("Error!!", "Invalid Inputs")
                        key = 1
                        break
                except ValueError as w:
                    messagebox.showinfo("Error!!", "Invalid Inputs")
                    key = 1
                    break
            k+=1

        if key==1:
            break

    if key==0:
        #print("Inputted Matrix")
        #print(np.matrix(gridn))
        #print('yes')

        l=out(gridn)
        if l==-1:
            messagebox.showinfo("Error!!", "Invalid Inputs")
        else:
            grid1 = copy.deepcopy(gridn)
            solve()

#print(np.matrix(grid))

def possible(y, x, n):# check if we can put a number, y-verical , x-horizontal
    global gridn
    for i in range(0, 9):
        if gridn[y][i] == n:
            return False
    for i in range(0, 9):
        if gridn[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if gridn[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global gridn, grid1, e, halt

    try:
        for y in range(9):
            for x in range(9):
                if gridn[y][x] == 0:
                    for n in range(1, 10):
                        if possible(y, x, n):
                            gridn[y][x] = n
                            solve()
                            gridn[y][x] = 0
                    return
        # print(gridn)
        # print(grid1)
        print(np.matrix(gridn))
        output()

    except Exception as t:
        messagebox.showinfo("Error!!", "Invalid Inputs")

def output():
    global gridn
    #print(gridn)
    k = 0
    for i in range(0, 9):
        for j in range(0, 9):
            e[k].delete(0, END)
            e[k].insert(INSERT, str(gridn[i][j]))
            k += 1








