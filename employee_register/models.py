"""from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)"""
    
    
    
    
    
    
    
    
    
    
    
    
    
""" class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname"""
        
        
        
        
from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Role(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title   
    

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3 )
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname






class Emp(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile=models.CharField(max_length=15)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



