from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0
    ADVANTAGE_INCREASE = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_INCREASE
        self.wins += 1
