from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField(null = True , blank = True)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=120)
	dob = models.DateField(max_length=8)
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
	gender = models.CharField(max_length=8,choices=GENDER_CHOICES)
	exam_grade = models.IntegerField(blank = True , null = True )
	classroom=  models.ForeignKey(Classroom, default=1, on_delete=models.CASCADE , related_name = "students")
