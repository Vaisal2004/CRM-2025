from django.db import models

from students.models import BaseClass

# Create your models here.

class Course(BaseClass):

    name = models.CharField(max_length=25)

    class Meta:

        verbose_name = 'Courses'

        verbose_name_plural = 'Courses'

    def __str__(self):
        
        return self.name