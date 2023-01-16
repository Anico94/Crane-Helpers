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

crane_1 = CalculateBallast(4200, 955, 1.98)

class TableData:
    def __init__(self, list_actions):
        self.list_actions = list_actions

    ## attempted getting mutliple heading in the dataframe but haven't worked it out yet. 
    
    def buildTable(self):
        header = pd.MultiIndex.from_product([['Fz','Fz','Fz','Fz']])
        df = pd.DataFrame([self.list_actions[3],self.list_actions[2]],
        [self.list_actions[3],self.list_actions[0]],
        [self.list_actions[1],self.list_actions[2]],
        [self.list_actions[1],self.list_actions[4]]
        , index = [0,45], columns = header)
        return df




reaction_table = TableData(crane_1.leg_actions()).buildTable()

print(reaction_table)

class ReactionTable:
    def __init__(self, compression, tension, neutral):
        compression = self.compression
        tension = self.tension
        neutral = self.neutral

    

