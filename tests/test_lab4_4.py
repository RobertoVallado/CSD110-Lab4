import sys
import tests.util as util
import src.lab4_4 as lab
import src.asciiturtle as turtle

expected1 = '''####
   #
   #
   #
'''

expected2 = '''####   
   #   
   #   
   ####
      #
      #
      #
'''
expected4 = '''####         
   #         
   #         
   ####      
      #      
      #      
      ####   
         #   
         #   
         ####
            #
            #
            #
'''

expected6 = '''####               
   #               
   #               
   ####            
      #            
      #            
      ####         
         #         
         #         
         ####      
            #      
            #      
            ####   
               #   
               #   
               ####
                  #
                  #
                  #
'''

def do_test(n, expected):
    t = turtle.Turtle()
    lab.steps(t, n)
    out = t.path_as_str()
    assert util.output_is_equivalent(expected, out, True), util.format_message(f"When size={n} your code does not produce the correct output", expected, out)

def test_1():
    do_test(1, expected1)

def test_2():
    do_test(2, expected2)

def test_4():
    do_test(4, expected4)

def test_6():
    do_test(6, expected6)