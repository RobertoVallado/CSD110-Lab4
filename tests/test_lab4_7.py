import sys
import tests.util as util
import src.asciiturtle as turtle
import src.lab4_7 as lab

expected_bar2 = """ #
###
 #
"""
expected1x2x2 = '''###
###
###
'''

expected2x5x5 = '''#           #####
#           #
#           #
#           #
#####   #####
    #   #
    #   #
    #   #
    #########
        #   #
        #   #
        #   #
    #####   #####
    #           #
    #           #
    #           #
#####           #
'''

def bar2(t):
    t.forward(1)
    t.back(1)

def b1x2x2(t):
    t.forward(1)
    t.right(90)
    t.forward(1)
    t.penup()
    t.backward(1)
    t.left(90)
    t.backward(1)
    t.pendown()

def b2x5x5(t):
    t.forward(4)
    t.right(90)
    t.forward(4)
    t.left(90)
    t.forward(4)
    t.right(90)
    t.forward(4)
    t.penup()
    t.backward(8)
    t.left(90)
    t.backward(8)
    t.pendown()

def do_test(n, h, v, blade_func, expected):
    t = turtle.Turtle()
    lab.windmill(t, blade_func)
    out = t.path_as_str()
    assert util.output_is_equivalent(expected, out, True), util.format_message(f"When a 'blade' function of steps={n}, hsize={h}, vsize={v} is used, your code does not produce the correct output", expected, out)

def test_2bar():
    t = turtle.Turtle()
    lab.windmill(t, bar2)
    out = t.path_as_str()
    assert util.output_is_equivalent(expected_bar2, out, True), util.format_message(f"When a 'blade' function that makes a 2-space bar is used, your code does not produce the correct output", expected_bar2, out)

def test_1x2x2():
    do_test(1, 2, 2, b1x2x2, expected1x2x2)

def test_2x5x5():
    do_test(2, 5, 5, b2x5x5, expected2x5x5)
