import sys
import tests.util as util
import src.asciiturtle as turtle
import src.lab4_9 as lab

expected1x1 = """##"""

expected2x3 = """## ##


## ##"""

expected5x5 = """##   ##   ##   ##   ##




##   ##   ##   ##   ##




##   ##   ##   ##   ##




##   ##   ##   ##   ##




##   ##   ##   ##   ##
"""

def bar2(t):
    t.forward(1)
    t.back(1)

def do_test(grid_size, spacing, expected):
    t = turtle.Turtle()
    lab.stamp_grid(t, grid_size, spacing, bar2)
    out = t.path_as_str()
    assert util.output_is_equivalent(expected, out, True), util.format_message(f"When grid_size={grid_size}, spacing={spacing}, your code does not produce the correct output.\nNOTE: in the tests, stamp function produces the simple drawing ##", expected, out)

def test1x1():
    do_test(1, 1, expected1x1)

def test1x3():
    do_test(1, 3, expected1x1)

def test2x3():
    do_test(2, 3, expected2x3)

def test5x5():
    do_test(5, 5, expected5x5)
