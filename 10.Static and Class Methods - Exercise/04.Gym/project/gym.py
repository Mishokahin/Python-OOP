from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""
        for sub in self.subscriptions:
            if sub.id == subscription_id:
                result += f"{str(sub)}\n"
        for cus in self.customers:
            if cus.id == subscription_id:
                result += f"{str(cus)}\n"
        for train in self.trainers:
            if train.id == subscription_id:
                result += f"{str(train)}\n"
        for eq in self.equipment:
            if eq.id == subscription_id:
                result += f"{str(eq)}\n"
        for plan in self.plans:
            if plan.id == subscription_id:
                result += f"{str(plan)}\n"
        return result[:-1]
