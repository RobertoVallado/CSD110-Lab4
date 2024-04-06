import sys
import tests.util as util
import src.asciiturtle as turtle
import src.lab4_5 as lab

expected1x2x2 = '''##
 #
'''

expected4x2x2 = '''##
 ##
  ##
   ##
    #
'''
expected1x7x2 = '''#######
      #
'''

expected1x2x7 = '''##
 #
 #
 #
 #
 #
 #
'''
expected3x4x5 = '''####
   #
   #
   #
   ####
      #
      #
      #
      ####
         #
         #
         #
         #
'''

def do_test(n, h, v, expected):
    t = turtle.Turtle()
    lab.steps(t, n, h, v)
    out = t.path_as_str()
    assert util.output_is_equivalent(expected, out, True), util.format_message(f"When steps={n}, hsize={h}, vsize={v} your code does not produce the correct output", expected, out)

def test_1x2x2():
    do_test(1, 2, 2, expected1x2x2)

def test_4x2x2():
    do_test(4, 2, 2, expected4x2x2)


def test_1x7x2():
    do_test(1, 7, 2, expected1x7x2)


def test_1x2x7():
    do_test(1, 2, 7, expected1x2x7)

def test_3x4x5():
    do_test(3, 4, 5, expected3x4x5)