"""Implement a deque using the python list."""


class Deque:
    """Class implementing a deque using a list."""

    def __init__(self, n):
        """Initialise the deque as a python list of size n."""
        self.deque = [None] * n
        self.size = n
        self.lpt = 0
        self.rpt = 0

    def __repr__(self):
        """Represent the deque as a string for user."""
        return f"{self.deque}"

    def append(self, x):
        """Append an item to the end of deque."""
        actuals = self.deque[self.lpt:self.rpt]
        self.deque = actuals + [x]
        while len(self.deque) < self.size:
            self.deque.appendleft(None)
        self.rpt += 1

    def appendleft(self, x):
        """Append an item to the start of deque."""
        actuals = self.deque[self.lpt:self.rpt]
        self.deque = [x] + actuals
        while len(self.deque) < self.size:
            self.deque.append(None)
        self.rpt += 1

    def pop(self):
        """Pop the last item in the deque and return it."""
        item_to_pop = self.deque[self.rpt-1]
        self.deque[self.rpt - 1] = None
        self.rpt -= 1
        return item_to_pop

    def popleft(self):
        """Pop the first item in the deque and return it."""
        item_to_pop = self.deque[self.lpt]
        self.deque[self.lpt] = None
        self.lpt += 1
        return item_to_pop

    def peek(self):
        """Peek at last item."""
        return self.deque[self.rpt - 1]

    def peekleft(self):
        """Peek at the first item."""
        return self.deque[self.lpt]

    def __len__(self):
        """Get the length of the deque."""
        return len(self.deque)


e = Deque(4)
e.append(5)
e.append(10)
e.append(15)
e.append(25)
e.popleft()
e.popleft()
print(e)
print(e.lpt)
print(e.rpt)
