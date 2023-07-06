from decimal import Decimal

from django.db import models

COLOR_CHOICES = (
    ("RED", "Red"),
    ("GREEN", "Green"),
    ("BLUE", "Blue"),
    ("WHITE", "White"),
)

GEARBOX_CHOICES = (
    ("AT", "Automatic transmission"),
    ("MT", "Manual transmission"),
)

FUEL_CHOICES = (
    ("GAS", "Gas"),
    ("DISEL", "Disel"),
    ("ELECTRO", "Electro"),
)

class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    color = models.CharField(max_length=32, choices=COLOR_CHOICES, default="WHITE")
    gearbox = models.CharField(max_length=32, choices=GEARBOX_CHOICES, default="AT")
    fuel = models.CharField(max_length=32, choices=FUEL_CHOICES, default="GAS")
    price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f"Product: {self.title} - {self.price}"