import math
import pandas as pd

class CalculateBallast:
    #stab_moment in kNm , vetical load in kN, size is length of one side of the static base
    def __init__(self, stab_moment, vertical, size):
        self.stab_moment = stab_moment
        self.vertical = vertical
        self.size = size

    def actions(self):
        compression = self.stab_moment/(math.sqrt(2)*self.size) + self.vertical/4
        tension = self.stab_moment/(math.sqrt(2)*self.size) - self.vertical/4
        return [compression,tension]

crane_1 = CalculateBallast(14100, 2360, 5)

print(crane_1.actions())

class ReactionTable:
    def __init__(self, compression, tension, netural):
        compression = self.compression
        tension = self.tension
        netural = self.netural

    

