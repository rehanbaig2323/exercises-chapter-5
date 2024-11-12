"""Implement a deque using the python list."""


class Deque:
    """Class implementing a deque using a list."""

    def __init__(self, n):
        """Initialise the deque as a python list of size n."""
        self.deque = [None] * n
        self.size = n
        self.lpt = 0
        self.rpt = 0
        self.current = 0

    def __repr__(self):
        """Represent the deque as a string for user."""
        return f"{self.deque}"

    def append(self, x):
        """Append an item to the end of deque."""
        actuals = self.deque[self.lpt:self.rpt]
        self.deque = actuals + [x]
        while len(self.deque) < self.size:
            self.deque.append(None)
        self.rpt += 1
        if self.rpt > self.size:
            self.rpt = self.rpt % self.size

    def appendleft(self, x):
        """Append an item to the start of deque."""
        actuals = self.deque[self.lpt:self.rpt]
        self.deque = [x] + actuals
        while len(self.deque) < self.size:
            self.deque.append(None)
        self.rpt += 1
        if self.rpt > self.size:
            self.rpt = self.rpt % self.size

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

    def __iter__(self):
        """Allow for iteration."""
        return self

    def __next__(self):
        """Rules for iteration."""
        self.current += 1
        return self.deque[self.current]
