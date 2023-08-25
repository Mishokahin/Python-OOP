from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        valid_equipment_types = {"KneePad": KneePad, "ElbowPad": ElbowPad}
        if equipment_type not in valid_equipment_types:
            raise Exception("Invalid equipment type!")

        equipment = valid_equipment_types[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        valid_team_types = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}
        if team_type not in valid_team_types:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team = valid_team_types[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]
        team = [t for t in self.teams if t.name == team_name][0]

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = [t for t in self.teams if t.name == team_name]

        if len(team) == 0:
            raise Exception("No such team!")

        if team[0].wins > 0:
            raise Exception(f"The team has {team[0].wins} wins! Removal is impossible!")

        self.teams.remove(team[0])
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_equipment = [e.increase_price() for e in self.equipment if e.__class__.__name__ == equipment_type]
        return f"Successfully changed {len(changed_equipment)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = [t for t in self.teams if t.name == team_name1][0]
        team_2 = [t for t in self.teams if t.name == team_name2][0]

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_score = team_1.advantage + sum([e.protection for e in team_1.equipment])
        team_2_score = team_2.advantage + sum([e.protection for e in team_2.equipment])

        if team_1_score == team_2_score:
            return "No winner in this game."

        elif team_1_score > team_2_score:
            team_1.win()
            return f"The winner is {team_1.name}."

        elif team_1_score < team_2_score:
            team_2.win()
            return f"The winner is {team_2.name}."

    def get_statistics(self):
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  f"Teams:",
                  ]

        for team in sorted(self.teams, key=lambda x: -x.wins):
            result.append(str(team.get_statistics()))

        return "\n".join(result)