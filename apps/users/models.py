from django.db import models
from  ..role import models as roleModel

    
class User(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone_no = models.CharField(null=True,max_length=255)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    # role_data = models.ManyToManyField(Role)
    role = models.ForeignKey(roleModel.Role, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_users'

    def __str__(self):
        return self.name
