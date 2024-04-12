from django.db import models

# Create your models here.
class Role(models.Model):
    # id = models.AutoField(primary_key=True)/
    role_name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    class Meta:
        db_table = 'tbl_roles'

    def __str__(self):
        return self.role_name