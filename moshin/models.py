from django.db import models

class Bmw(models.Model):
    turi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=20)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi


class Kia(models.Model):
    turi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=20)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi


class Ferrari(models.Model):
    turi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=20)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi


class Chevrolet(models.Model):
    turi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=20)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi


class Honda(models.Model):
    turi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=20)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi










