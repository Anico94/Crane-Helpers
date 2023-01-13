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

class TableData:
    def __init__(self, list_actions):
        self.list_actions = list_actions

    def buildTable(self):
        df = pd.DataFrame({"A": [self.list_actions[3],self.list_actions[2]],
        "B": [self.list_actions[3],self.list_actions[0]],
        "C": [self.list_actions[1],self.list_actions[2]],
        "D": [self.list_actions[1],self.list_actions[4]]
        }, index = [0,45])
        return df



reaction_table = TableData(crane_1.leg_actions()).buildTable()

print(reaction_table)

class ReactionTable:
    def __init__(self, compression, tension, neutral):
        compression = self.compression
        tension = self.tension
        neutral = self.neutral

    

