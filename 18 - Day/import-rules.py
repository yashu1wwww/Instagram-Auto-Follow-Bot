"""
        Basic Import
"""

import turtle
a = turtle.Turtle()


"""
        From Import
"""
from turtle import Turtle
b = Turtle()


"""
        Import *  ( Means -> import all things from module )
"""
from turtle import *

c = Turtle()


"""
        Aliasing Modules
"""
import turtle as t

d = t.Turtle()
screen = t.Screen()
