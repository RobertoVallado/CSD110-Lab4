import sys
import util

expected_output = '''####         
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

def test_output_is_the_same(capsys):
    if 'src.lab4_3' in sys.modules.keys():
        sys.modules.pop('src.lab4_3')
    import src.lab4_3
    out, err = capsys.readouterr()
    assert util.output_is_equivalent(expected_output, out, True), util.format_message("Your code does not produce the expected output", expected_output, out)