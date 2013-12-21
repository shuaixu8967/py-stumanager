#coding=utf-8

from django.db import models

class Department(models.Model):
    name = models.CharField('department name',max_length=30)

    
class Major(models.Model):
    name = models.CharField('major name',max_length=30)
    department = models.ForeignKey(Department)
    
#班级
class SchoolClass(models.Model):
    name = models.CharField('class name',max_length=30)
    major = models.ForeignKey(Major)

    
# Create your models here.
class Student(models.Model):
    name = models.CharField('student name',max_length=30)
    tel = models.CharField('student telephone number',max_length=20)
    exam_year = models.DateTimeField()
    code = models.CharField('student code',max_length=50)
    school_class = models.ForeignKey(SchoolClass)


class Website(models.Model):
    name = models.CharField('website name',max_length=30)

class Seller(models.Model):
    name = models.CharField('seller name ',max_length=30)
    tel = models.CharField('seller tel',max_length=20)

class Items(models.Model):
    date = models.DateTimeField()
    #出售时的价格
    total_price = models.FloatField()
    #挣了多少钱
    earn_price = models.FloatField()
    student = models.ForeignKey(Student)
    seller = models.ForeignKey(Seller)
    website = models.ForeignKey(Website)