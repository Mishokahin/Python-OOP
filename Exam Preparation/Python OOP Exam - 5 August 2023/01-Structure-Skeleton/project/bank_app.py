from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        valid_loans = {"StudentLoan": StudentLoan,  "MortgageLoan": MortgageLoan}

        if loan_type not in valid_loans:
            raise Exception("Invalid loan type!")

        loan = valid_loans[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        valid_clients = {"Student": Student, "Adult": Adult}

        if client_type not in valid_clients:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        client = valid_clients[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id][0]
        available_loans = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
        if client.__class__.__name__ == "Student" and loan_type != "StudentLoan" or \
                client.__class__.__name__ == "Adult" and loan_type != "MortgageLoan":
            raise Exception("Inappropriate loan type!")

        client.loans.append(available_loans)
        self.loans.remove(available_loans)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = [loan.increase_interest_rate() for loan in self.loans if loan.__class__.__name__ == loan_type]

        return f"Successfully changed {len(changed_loans)} loans."

    def remove_client(self, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id]
        if len(client) == 0:
            raise Exception("No such client!")
        elif len(client[0].loans) != 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client[0])
        return f"Successfully removed {client[0].name} with ID {client_id}."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = [c.increase_clients_interest() for c in self.clients if c.interest < min_rate]

        return f"Number of clients affected: {len(affected_clients)}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = 0
        for c in self.clients:
            for loan in c.loans:
                granted_sum += loan.amount

        loans_count_not_granted = len(self.loans)

        not_granted_sum = sum([loan.amount for loan in self.loans])

        avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients) \
            if len(self.clients) != 0 else 0

        return f"Active Clients: {total_clients_count}" + \
            f"\nTotal Income: {total_clients_income:.2f}" + \
            f"\nGranted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}" + \
            f"\nAvailable Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}" + \
            f"\nAverage Client Interest Rate: {avg_client_interest_rate:.2f}"


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())