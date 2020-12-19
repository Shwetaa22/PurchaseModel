from django.db import models


class PurchaseModel(models.Model):
    purchaser_name = models.CharField(max_length=255, default=None, null=False, blank=False)
    quantity = models.IntegerField(default=None)

    class Meta:
        db_table = "purchase"
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return self.purchaser_name


class PurchaseStatusModel(models.Model):
    purchase = models.ForeignKey(PurchaseModel,on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=25,
        choices=(
            ("open", "Open"),
            ("verified", "Verified"),
            ("dispatched", "Dispatched"),
            ("delivered", "Delivered"),)
    )
    created_at = models.DateTimeField(default=None)

    class Meta:
        db_table = "purchase_status"
        verbose_name = 'Purchase Status'
        verbose_name_plural = 'Purchases Status'
