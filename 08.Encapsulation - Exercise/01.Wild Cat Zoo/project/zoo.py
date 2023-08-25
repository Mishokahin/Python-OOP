from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        elif price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker_to_remove = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker_to_remove)
            return f"{worker_name} fired successfully"

        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([s.salary for s in self.workers])
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = sum([a.money_for_care for a in self.animals])
        if total_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        first_sting = f"You have {len(self.animals)} animals"
        lion_string = f"\n----- {len(lions)} Lions:"
        for lion in lions:
            lion_string += f"\n{lion}"
        tiger_string = f"\n----- {len(tigers)} Tigers:"
        for tiger in tigers:
            tiger_string += f"\n{tiger}"
        cheetah_string = f"\n----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            cheetah_string += f"\n{cheetah}"

        return first_sting + lion_string + tiger_string + cheetah_string

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        first_string = f"You have {len(self.workers)} workers"
        keepers_string = f"\n----- {len(keepers)} Keepers:"
        for keeper in keepers:
            keepers_string += f"\n{keeper}"
        caretakers_string = f"\n----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            caretakers_string += f"\n{caretaker}"
        vets_string = f"\n----- {len(vets)} Vets:"
        for vet in vets:
            vets_string += f"\n{vet}"

        return first_string + keepers_string + caretakers_string + vets_string










