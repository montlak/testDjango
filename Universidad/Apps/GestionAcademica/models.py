# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	lastName1 = models.CharField(max_length=35)
	lastName2 = models.CharField(max_length=35)
	names = models.CharField(max_length=35)
	DNI = models.CharField(max_length=8)
	birthDate = models.DateField()
	GENDERS=(('F', 'Femenino'), ('M', 'Masculino'))
	gender = models.CharField(max_length=1, choices=GENDERS, default='M')

	def completeName(self):
		cadena = "{0} {1}, {2}"
		return cadena.format(self.lastName1, self.lastName2, self.names)

	def __str__(self):
		return self.completeName()

class Course(models.Model):
	name = models.CharField(max_length=50)
	credits = models.PositiveSmallIntegerField()
	isActive = models.BooleanField(default=True)

	def __str__(self):
		return "{0} ({1})".format(self.name, self.credits)

class Register(models.Model):
	student = models.ForeignKey(Student, null=False, blank=False, on_delete= models.CASCADE)
	course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0} => {1}".format(self.student, self.course.name)