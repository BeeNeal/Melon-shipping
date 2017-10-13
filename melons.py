"""Classes for melon orders."""


# class DomesticMelonOrder(object):
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder(object):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
            """Initialize melon order attributes."""

            self.species = species
            self.qty = qty
            self.shipped = False
            self.tax = None
            self.order_type = None


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """For Domestic Melon orders"""

    def __init__(self, species, qty):

        super(DomesticMelonOrder, self).__init__(species, qty)
        self.tax = 0.08
        self.order_type = "Domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """ For international melon orders"""


    def __init__(self, species, qty, country_code):

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.tax = 0.17
        self.order_type = "International"


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """ Adds three dollar flat fee to less than ten melons"""
        
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total = total + 3
        return total
