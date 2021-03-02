from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    stu_id=models.IntegerField()
    stu_name=models.CharField(max_length=50)
    stu_city=models.CharField(max_length=150)
    stu_contactno=models.IntegerField()
    stu_email=models.EmailField()

    class Meta:
        db_table="tbl_student"

    def __str__(self):
        return self.stu_name
