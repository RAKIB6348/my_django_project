from django.db import models


class AcademicYear(models.Model):
    year = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.year


class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"