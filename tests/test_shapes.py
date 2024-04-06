import inspect
import sys

import src.shapes as shapes

def test_module_has_5_single_arg_funcs():
    funcs = inspect.getmembers(shapes, lambda m: inspect.isfunction(m))

    count = 0
    for [name, f] in funcs:
        if len(inspect.signature(f).parameters) == 1:
            count += 1
    
    assert count >= 5, f"There are only {count} functions that have a single parameter, but there should be at least 5"