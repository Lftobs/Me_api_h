from django.db import models

# Create your models here.

operator = (
        ('ad', 'addition'),
        ('multiplication', 'mutiply'),
        ('subtraction', 'sub')
    )

class Name(models.Model):
    add = 'addition'
    multi = 'multiplication'
    sub = 'subtraction'
    operator = (
        (add, 'addition'),
        (multi, 'mutiply'),
        (sub, 'sub')
    )
    #operation_type = models.CharField(max_length=100, choices=operator, default=add)
    operation_type = models.CharField(max_length=100, choices=operator)
    x = models.IntegerField()
    y= models.IntegerField()
    

    def __str__(self):
        return self.operation_type

    
