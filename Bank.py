class Bank:
    accounts = {}
    loan_amount = 0
    available_balence = 0
    isBankrupt = False

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address