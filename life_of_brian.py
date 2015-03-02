#!/usr/bin/env python
#import random, sys
from Tkinter import *
import time

pause = 0.2
iters = 50
width = 20
Fontsz = 5                              # defaults if no constructor args                            
class LifeBase(Frame):                            # a kind of Frame
    def __init__(self, parent=None,
                    fg='white', bg='black',
                    fontsz=Fontsz, degree=width) :
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.degree = degree
        self.label = {}
        self.drawBoard(fg, bg, fontsz)

	# defaults....
        blinker = ((1, 0), (1, 1), (1, 2))
        block   = ((0, 0), (1, 1), (0, 1), (1, 0))
        toad    = ((0, 0), (1, 0), (2, 0), (1, 1), (2, 1), (3, 1))
        glider  = ((0, 1), (1, 0), (0, 0), (0, 2), (2, 1))
        line    = ((0, 0), (1, 0), (2, 0), (3, 0))

        world   = (set(block) |
                    self.offset(blinker, (5, 2)) |
                    self.offset(glider, (15, 5)) |
                    self.offset(line, (4, 10)) |
                    self.offset(toad, (15, 12)) |
                    self.offset(block, (2, 15)))

        self.neighboring_cells = ((-1, -1), (-1, 0), (-1, 1), 
                                  ( 0, -1),          ( 0, 1), 
                                  ( 1, -1), ( 1, 0), ( 1, 1))

        self.life(world, iters)

    def drawBoard(self, fg, bg, fontsz):
        for j in range(self.degree):
            frm = Frame(self)
            frm.pack(expand=YES, fill=BOTH)
            for i in range(self.degree):
                widget = Label(frm, fg=fg, bg=bg, 
                                    text=' ', font=('courier', fontsz, 'bold'),
                                    relief=SUNKEN, bd=4, padx=10, pady=10)
                #widget.pack(side=LEFT, expand=YES, fill=BOTH)
                widget.pack(side=LEFT, expand=YES, fill=BOTH, ipadx=2)
                self.label[(i, j)] = widget

    def life(self,world, N):
        """Play Conway's game of life for N generations from initial world."""
        for g in range(N+1):
            self.display(world, g)
            time.sleep(pause)
            """counts is a dictionary of (x, y):<no.of neighbours>
            neighbours is a list of neighboring cells to all live cells
            the list is collapsed to a dictionary by counting duplicates
            counts = Counter(n for c in world
                                 for n in self.offset(self.neighboring_cells, c))
            """
            neighbours = []
            counts = {}
            for coord in world:
                for n in self.offset(self.neighboring_cells, coord):
                    neighbours.append(n)
	    print neighbours
            for n in neighbours:
                counts[n] = neighbours.count(n)
            world = set(c for c in counts if counts[c] == 3 
                              or counts[c] == 2 and c in world)
        return world
 
    def offset(self,world, delta):
        "Slide/offset all the cells in world by delta, a (dx, dy) vector."
        (dx, dy) = delta
        return set((x+dx, y+dy) for (x, y) in world)
 
    def display(self,world, g):
        """Display the world as a grid of characters."""
        print '          GENERATION {0}'.format(g)

        Xs, Ys = zip(*world)
        print Xs, Ys
        for y in range(self.degree):
            for x in range(self.degree):
                labelx = self.label[(x, y)]
                if(x, y) in world:
                    print '(X, Y) %d,%d is in world' % (x,y)
                    labelx.config(bg="purple")
                else:
                    labelx.config(bg="black")
        self.update()
 

if __name__=='__main__':
        root = Tk()
        LifeBase(root).mainloop()
#End of Life_0.1_alt.py
