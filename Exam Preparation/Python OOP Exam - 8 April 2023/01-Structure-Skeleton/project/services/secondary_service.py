from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        result = f"{self.name} Secondary Service:\nRobots: "
        if len(self.robots) == 0:
            result += "none"
        else:
            result += f'{" ".join([robot.name for robot in self.robots])}'

        return result
