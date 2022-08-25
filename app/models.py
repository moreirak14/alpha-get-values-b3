from django.db import models

from users.models import UserAccount


class Action(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol

    class Meta:
        db_table = "Action"
        verbose_name = "Action"
        verbose_name_plural = "Actions"
