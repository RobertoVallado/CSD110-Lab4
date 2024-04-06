import pytest
import traceback
from types import TracebackType


def red(s):
    return "\033[0;91m" + s + "\033[39m\033[49m" #"\033[0m"
def green(s):
    return "\033[0;92m" + s + "\033[39m\033[49m" #"\033[0m"
def purple(s):
    return "\033[0;95m" + s + "\033[39m\033[49m" #"\033[0m"

def trimlines(str):
    """Remove empty rows and columns at end of text, and pad out right end of short lines
       with spaces so that each line is the same length"""
    lines = str.split("\n")
    lines.reverse()
    out = []
    first_non_empty_line_idx = 0
    for line in lines:
        if line.strip() != "":
            break
        first_non_empty_line_idx += 1
    lines = lines[first_non_empty_line_idx:]
    lines.reverse()

    longest_line = 0
    for line in lines:
        length = len(line.rstrip())
        if length > longest_line:
            longest_line = length
    
    out = []
    for line in lines:
        out.append(line[:longest_line] + " " * (longest_line - len(line)))

    return "\n".join(out)

def output_is_equivalent(truth, test, trim=False):
    if trim:
        truth = trimlines(truth)
        test = trimlines(test)
    return truth == test

def diff(truth, test):
    truth = trimlines(truth)
    test = trimlines(test)

    test = test.split("\n")
    d = ""
    y = 0
    for line in truth.split("\n"):

        # Truth drawing has more rows than test drawing
        if y >= len(test):
            d += purple(line + "↵")
        else:
            x = 0
            for expected in line:
                # truth line continues beyond end of test line
                if x >= len(test[y]):
                    d += red("↵") + purple(line[x+1:] + "↵")
                    x = len(line)
                    break
                else:
                    yours = test[y][x]
                    if yours == expected:
                        d += green(expected)
                    else:
                        if expected != ' ':
                            d += purple(expected)
                        else:
                            d += red(yours)
                x += 1

            # test line continues beyond end of truth line
            if x < len(test[y]):
                d += purple("↵") + red(test[y][(x+1):] + "↵")
            elif x == len(test[y]):
                d += green("↵")

        d += "\n"

        y += 1

    # Test drawing has more rows than truth drawing
    if y < len(test):
        d += red("↵\n".join(test[y:]) + "↵\n")

    return d

def format_message(msg, expected, yours):
    theDiff = ""
    try:
        theDiff = diff(expected, yours)
    except:
        print(traceback.format_exc())

    return f"{msg}\nExpected: (↵ represents end of line)\n" + expected.replace('\n', '↵\n') + f"\nBut got:\n" + yours.replace("\n", "↵\n") + (f"\nDifference: ({green('green')}=correct; {purple('purple')}=expected but missing; {red('red')}=unexpected)\n{theDiff}" if theDiff else "")

def mock_input_func(answers):
    i = 0
    def _in(p):
        nonlocal i
        try:
            r = answers[i]
            print(p + r)
        except IndexError:
            raise IOError("Test expected program to be done but it is still awaiting input")
        i += 1
        return r
    return _in

def expect_assertion_error(f, fname, argnum, argtypestr):
    try:
        f()
    except AssertionError as e:
        pass
    except:
        assert False, f"The {fname} function must raise an AssertionError if the {argnum} argument {argtypestr}"

def assert_assertion_message_equals(f, msg, argnum, argtypestr):
    with pytest.raises(AssertionError) as err:
        f()

    assert msg == str(err.value), f"The raised error must have the message '{msg}' when the {argnum} argument {argtypestr}"
