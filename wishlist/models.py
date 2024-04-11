from django.db import models
from users import models as userModel1  
from products import models as productModelss

# Create your models here.class User(models.Model):
    # id = models.AutoField(primary_key=True)
class WishList(models.Model):
    # id = models.AutoField(primary_key=True)
    notification = models.BooleanField()
    isAddToWishList=models.BooleanField()
   
    userId = models.ForeignKey(userModel1.User, on_delete=models.CASCADE)
    productId = models.ForeignKey(productModelss.Product, on_delete=models.CASCADE)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    # role_data = models.ManyToManyField(Role)

    class Meta:
        db_table = 'tbl_wishlist'

    def __str__(self):
        return self.productId
   
