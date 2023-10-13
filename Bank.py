class Bank:
    accounts = {}
    loan_amount = 0
    available_balence = 100000
    isBankrupt = False
    giving_loan = True

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address