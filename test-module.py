import sys

from absolute_value import absolute_value

def test(did_pass):
    """Print the result of a test. """
    linenum = sys._getframe(1).f_lineno #Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at lne {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """
    Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite()