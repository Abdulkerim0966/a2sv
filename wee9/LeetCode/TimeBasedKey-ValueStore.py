class TimeMap:

    def __init__(self):
        self.dect=defaultdict(list)
        self.dect2=defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dect[key].append(value)
        self.dect2[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        idx=bisect_right(self.dect2[key],timestamp)
        if idx ==0:
            return ""
        return self.dect[key][idx-1]