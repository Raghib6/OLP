from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student_name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
