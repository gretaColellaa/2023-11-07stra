from dataclasses import dataclass

@dataclass
class Team:
    ID:int
    teamCode:str
    name:str
    salaries:float

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"{self.teamCode}–{self.name}"

