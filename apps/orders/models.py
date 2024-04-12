from django.db import models
from ..users import models as userModel1  
from ..products import models as productModelss
# Create your models here.
class Orders(models.Model):
    # id = models.AutoField(primary_key=True)
    address=models.CharField(max_length=500)
    user = models.ForeignKey(userModel1.User, on_delete=models.CASCADE)
    product = models.ForeignKey(productModelss.Product, on_delete=models.CASCADE)
    order_status=models.CharField(max_length=250)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'tbl_orders'

    def __str__(self):
        return self.productId