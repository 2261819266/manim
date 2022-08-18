from manimlib import Scene, Circle, Line, Write
from manimlib import LEFT, RIGHT, UP
from numpy import double
# from lib.graph import *

class Node :
    x : int 
    y : int
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

class main(Scene) :
    def construct(self) -> None:
        # c = [
        #     Circle(arc_center = LEFT * 5),
        #     Circle(arc_center = RIGHT * 3),
        # ]
        # line = Line(LEFT * 5, RIGHT * 3, buff = 1, include_tip = True)
        # self.play(Write(c[0]), Write(c[1]))
        # self.play(Write(line.add_tip()))
        fin = open("in.in")
        l = fin.readline().split(' ')
        n = int(l[0])
        m = int(l[1])
        r = double(l[2])
        nodes = [Node()] * (n + 1)
        circles = [Circle()] * (n + 1)
        # graph = Graph(1, n + 1)
        for i in range(1, n + 1) :
            l = fin.readline().split(' ')
            circles[i] = Circle(
                radius = r,
                arc_center = RIGHT * int(l[0]) +
                UP * int(l[1]),
            )
            nodes[i] = Node(int(l[0]), int(l[1]))
            self.play(Write(circles[i]))
        for i in range(0, m) :
            l = fin.readline().split(' ')
            u = int(l[0])
            v = int(l[1])
            w = int(l[2])
            x = nodes[u].x * RIGHT + nodes[u].y * UP 
            y = nodes[v].x * RIGHT + nodes[v].y * UP 
            line = Line(x, y, buff = r)
            line.add_tip()
            self.play(Write(line))
