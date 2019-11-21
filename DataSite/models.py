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


class Roles(models.Model):
    """角色"""
    Name = models.CharField(max_length=40)
    User = models.ManyToManyField(Users)

    def __unicode__(self):
        return self.Name


class Departments(models.Model):
    """部门"""
    Name = models.CharField(max_length=40)
    Abbreviation = models.CharField(max_length=40)
    Parent = models.CharField(max_length=40, null=True)
    User = models.ManyToManyField(Users)
    Remark = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.Name


class Premissions(models.Model):
    """权限"""
    Name = models.CharField(max_length=40)
    Department = models.ForeignKey(Departments)
    Role = models.ManyToManyField(Roles)

    def __unicode__(self):
        return self.Name

