from pickletools import markobject
from django.db import models

# Create your models here.
from email.mime import image
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Student_detail(models.Model):
    name = models.CharField(max_length=200, null=True)
    roll_number = models.CharField(max_length=200, null=True)
    upload = models.ImageField(upload_to='image')
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.roll_number


class Mark(models.Model):
    roll_no = models.ForeignKey(
        Student_detail, null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    mark = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Modified_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=20, null=True)
    created_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} , {}".format(self.roll_no, self.id)


class bag(models.Model):
    brand = models.CharField(max_length=50)
    capacity = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.brand)


class buyer(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    bags_purchased = models.ManyToManyField(bag)

    def __str__(self):
        return "%s" % (self.name)
