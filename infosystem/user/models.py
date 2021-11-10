from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PoliceStation(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=30)
    post_code=models.PositiveIntegerField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    policstation = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

