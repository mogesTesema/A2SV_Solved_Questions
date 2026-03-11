class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.count = 0  # consecutive occurrences counter

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k