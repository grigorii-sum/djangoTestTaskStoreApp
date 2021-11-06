from django.db import models


class StoreOrder(models.Model):
    order_number = models.CharField(max_length=100)
    STATUS_TYPES = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Stored', 'Stored'),
        ('Send', 'Send')
    )
    order_status = models.CharField(max_length=11, choices=STATUS_TYPES)

    def __str__(self):
        return 'WAREHOUSE HAS ORDER "{0}" WITH STATUS = {1}'.format(self.order_number, self.order_status)

