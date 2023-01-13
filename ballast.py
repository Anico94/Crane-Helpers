import math
import pandas as pd

class CalculateBallast:
    #moment in kNm , vetical load in kN, size is length of one side of the static base
    def __init__(self, moment, vertical, centres):
        self.moment = moment
        self.vertical = vertical
        self.centres = centres

    def leg_actions(self):
        compression45 = self.moment/(math.sqrt(2)*self.centres) + self.vertical/4
        tension45 = self.moment/(math.sqrt(2)*self.centres) - self.vertical/4
        neutral45 = self.vertical/4
        compression90 = self.moment/(2*self.centres) + self.vertical/4
        tension90 = self.moment/(2*self.centres) - self.vertical/4

        leg_actions = [compression45, tension45,neutral45, compression90, tension90]


        return leg_actions

crane_1 = CalculateBallast(14100, 2360, 5)

df = pd.DataFrame({"A": [crane_1.leg_actions()[3],crane_1.leg_actions()[2]],
"B": [crane_1.leg_actions()[3],crane_1.leg_actions()[0]],
"C": [crane_1.leg_actions()[1],crane_1.leg_actions()[2]],
"D": [crane_1.leg_actions()[1],crane_1.leg_actions()[4]]
}, index = [0,45])

print(df)

class ReactionTable:
    def __init__(self, compression, tension, neutral):
        compression = self.compression
        tension = self.tension
        neutral = self.neutral

    

