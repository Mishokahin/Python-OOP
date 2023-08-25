from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        valid_services = {"MainService": MainService,  "SecondaryService": SecondaryService}

        if service_type not in valid_services:
            raise Exception("Invalid service type!")

        service = valid_services[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robots = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

        if robot_type not in valid_robots:
            raise Exception("Invalid robot type!")

        robot = valid_robots[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        valid_combinations = [["MaleRobot", "MainService"], ["FemaleRobot", "SecondaryService"]]

        if [robot.__class__.__name__, service.__class__.__name__] not in valid_combinations:
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in service.robots if r.name == robot_name]

        if len(robot) == 0:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot[0])
        self.robots.append(robot[0])
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        number_of_robots_fed = len([r.eating() for r in service.robots])

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = 0.0

        for r in service.robots:
            total_price += r.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""

        for s in self.services:
            result += f"{s.details()}\n"

        return result[:-1]