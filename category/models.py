from django.db import models

# Create your models here.
class Category(models.Model):
    # id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=500)
    DisplayOrder = models.IntegerField()
    Code = models.CharField(max_length=250)
    ImgUrl = models.CharField(max_length=250)
    Width = models.IntegerField(null=True)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    class Meta:
        db_table = 'tbl_categorys'

    def __str__(self):
        return self.Name
