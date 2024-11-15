"""Fibonacci module in order to generate examples of adt."""


class Fib:
    """Class to generate fibonacci numbers."""

    def __init__(self):
        """Initialise the class."""
        self.a = 1
        self.b = 1

    def __iter__(self):
        """Allow for iteration with native python commands."""
        return self

    def __next__(self):
        """Generate the next fibo number."""
        temp = self.b
        self.a, self.b = self.b, self.a + self.b
        return temp
