from numbers import Number # noqa f401
import math # noqa f401

"""Implement a Reverse Polish calculator."""


class RPCalc:
    """Reverse Polish calculator."""

    def __init__(self):
        """Initialise the calculator."""
        self.stack = []

    def __repr__(self):
        """Represent stack as string to user."""
        return f"{self.stack}"

    def push(self, n):
        """Push a number or operator onto the stack."""
        if isinstance(n, Number):
            self.stack.append(n)
        elif n == "+":
            a = self.stack[-1]
            b = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            self.stack.append(a + b)
        elif n == "-":
            a = self.stack[-1]
            b = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            self.stack.append(b - a)
        elif n == "*":
            a = self.stack[-1]
            b = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            self.stack.append(a * b)
        elif n == "/":
            a = self.stack[-1]
            b = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            self.stack.append(b / a)
        elif n == "sin":
            a = self.stack[-1]
            self.stack.pop()
            self.stack.append(math.sin(a))
        elif n == "cos":
            a = self.stack[-1]
            self.stack.pop()
            self.stack.append(math.cos(a))

    def pop(self):
        """Remove top element in stack."""
        return self.stack.pop()

    def peek(self):
        """Return top element in stack."""
        return self.stack[-1]

    def len(self):
        """Return length of stack."""
        return len(self.stack)
