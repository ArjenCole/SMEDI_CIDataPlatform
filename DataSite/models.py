from django.db import models

# Create your models here.


class Users(models.Model):
    """用户"""
    Account = models.EmailField()
    Password = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Major = models.CharField(max_length=50, null=True)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Account


class Departments(models.Model):
    """部门"""
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=40)
    parent = models.CharField(max_length=40, null=True)
    users = models.ManyToManyField(Users)
    remark = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.name

