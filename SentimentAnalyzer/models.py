from django.db import models


class ProductReview(models.Model):
    score = models.IntegerField()
    product_id = models.CharField(max_length=20)
    label = models.CharField(max_length=10)
    review = models.TextField()

    def __str__(self):
        return f'{self.product_id} - {self.label}'
