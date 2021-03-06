"""
module doc
"""
from django.db import models


class Customer(models.Model):
    """ CUSTOMER MODEL"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"""name : {self.first_name} {self.last_name} email: {self.email} balance: {self.balance}"""


class Transfer(models.Model):
    t_from = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="creditor")
    t_to = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="debitor")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"""from : {self.t_from} to: {self.t_to} amount: {self.amount}"""
