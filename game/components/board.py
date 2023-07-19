import numpy as np

class Board:
    def __init__(self) -> None:
        self.size = 8*10
        self.state = np.zeros(shape=(6,),dtype=np.int64)

    def update(self):
        pass

    def draw(self):
        pass
