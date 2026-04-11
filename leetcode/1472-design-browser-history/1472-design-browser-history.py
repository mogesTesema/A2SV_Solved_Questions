class BrowserHistory:

    class Node:
        def __init__(self, url):
            self.val = url
            self.prev = None
            self.next = None

    def __init__(self, homepage: str):
        self.home = self.Node(homepage)
        self.curr = self.home

    def visit(self, url: str) -> None:
        node = self.Node(url)
        self.curr.next = node
        node.prev = self.curr
        
        self.curr = node
        self.curr.next = None

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val