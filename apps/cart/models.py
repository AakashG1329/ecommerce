from django.db import models
from ..users import models as userModel1  
from ..products import models as productModelss
# Create your models here.
class Cart(models.Model):
    # id = models.AutoField(primary_key=True)
    notification = models.BooleanField()
    is_add_to_cart_list=models.BooleanField()
    user_id = models.ForeignKey(userModel1.User, on_delete=models.CASCADE)
    product = models.ForeignKey(productModelss.Product, on_delete=models.CASCADE)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'tbl_cart'

    def __str__(self):
        return self.productId
   