import unittest

def pairtest(*pair_args):
    """https://stackoverflow.com/questions/18084476/is-there-a-way-to-use-python-unit-test-assertions-outside-of-a-testcase"""
    
    trial = pair_args[::2]
    expected = pair_args[1::2]
    tc = unittest.TestCase('__init__')
    tc.assertEqual(trial, expected)
    print("\n\n* All tests passed \\(^o^)/ \n")
