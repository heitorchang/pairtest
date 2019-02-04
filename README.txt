Suppose there is a function sq(x) that squares numbers

def sq(x):
    return x * x

The odd-indexed arguments to pairtest are the ones we wish to test, and
even-indexed arguments are the expected values.

In the example below, the first, third and fourth tests pass.

pairtest(
    sq(9), 81,
    sq(3), 33,
    sq(7), 49,
    sq(1), 1,
    sq(0), 10,
)
