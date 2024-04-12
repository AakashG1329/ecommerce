from django.db import models

from ..category import models as categorModel
# Create your models here.

   
class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    item_number = models.IntegerField()
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    # role_data = models.ManyToManyField(Role)
    Category = models.ForeignKey(categorModel.Category, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_products'

    def __str__(self):
        return self.itemNumber
