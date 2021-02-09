from typing import List
from enum import Enum
from operator import attrgetter

SEP = ';'

class Outcome(Enum):
    LOSS = 0
    DRAW = 1
    WIN = 3

    #
    # Internal Helpers
    #
    @staticmethod
    def convert(res: str):
        if res == "win":
            return Outcome.WIN

        elif res == "loss" :
            return Outcome.LOSS

        elif res== "draw":
            return Outcome.DRAW

        else:
            raise ValueError("must be: win xor loss xor draw")

    @staticmethod
    def reverse(res):
        if res == Outcome.WIN:
            return Outcome.LOSS

        elif res == Outcome.LOSS:
            return Outcome.WIN

        else:
            return Outcome.DRAW

class Team:
    THEADER = "Team                           | MP |  W |  D |  L |  P"

    def __init__(self, name: str, res: Outcome):
        self.name = name
        self.m_played = 1
        self.m_won   = 1 if res == Outcome.WIN  else 0
        self.m_drawn = 1 if res == Outcome.DRAW else 0
        self.m_loss  = 1 if res == Outcome.LOSS else 0
        self.pts = 3 * self.m_won + 1 * self.m_drawn

    def update(self, res: Outcome):
        self.m_played += 1

        if res == Outcome.WIN:
            self.m_won += 1
            self.pts += 3

        elif res == Outcome.DRAW:
            self.pts += 1
            self.m_drawn += 1

        else:
            self.m_loss += 1

def tally(rows: List[str]) -> List[str]:
    if len(rows) == 0:
        return [ Team.THEADER ]

    dteams = {}
    for r in rows:
        (lt, rt, sres) = r.split(SEP)
        res = Outcome.convert(sres)

        for t in (lt, rt):
            if t == rt:
                res = Outcome.reverse(res)

            if dteams.get(t, None) == None:
                dteams[t] = Team(t, res)
            else:
                dteams[t].update(res)
        #
        teams = [vt for (_, vt) in dteams.items()]
        table = [ Team.THEADER ]
        for t in sorted(sorted(teams, key=attrgetter('name')),
                        key=attrgetter('pts'), reverse=True):
            table.append(
                f"{t.name:31}|{t.m_played:3} |{t.m_won:3} |{t.m_drawn:3} |{t.m_loss:3} |{t.pts:3d}"
            )
        #
    return table
