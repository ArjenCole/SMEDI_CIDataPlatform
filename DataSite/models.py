from django.db import models

# Create your models here.


class Departments(models.Model):
    """部门"""
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=40)
    parent = models.CharField(max_length=40)
    remark = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Users(models.Model):
    """用户"""
    Account = models.EmailField()
    Password = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Department = models.ForeignKey(Departments)
    Major = models.CharField(max_length=50)
    Remark = models.CharField(max_length=50)

    def __unicode__(self):
        return self.Account

