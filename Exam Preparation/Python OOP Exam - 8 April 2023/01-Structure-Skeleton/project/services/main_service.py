from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        result = f"{self.name} Main Service:\nRobots: "
        if len(self.robots) == 0:
            result += "none"
        else:
            result += f'{" ".join([robot.name for robot in self.robots])}'

        return result
