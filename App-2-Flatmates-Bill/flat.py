class Bill:
    """
    Object that contains data about a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about a flatmate
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return bill.amount * weight
