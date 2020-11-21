from atm_card import ATMCard


class Customer:
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def withdrawBalance(self, nominal):
        debet = self.custBalance - nominal
        return debet

    def depositBalance(self, nominal):
        simpan = self.custBalance + nominal
        return simpan

    def checkPin(self):
        return self.custPin

    def checkBalance(self):
        return self.custBalance