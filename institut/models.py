from django.db import models

class Navoiy(models.Model):
    fakulteti = models.CharField(max_length=50)
    yonalishlarisoni = models.IntegerField(default=1)
    malumot = models.TextField()
    rasm = models.CharField(max_length=255)

    def __str__(self):
        return self.fakulteti


class Buxoro(models.Model):
    fakulteti = models.CharField(max_length=50)
    yonalishlarisoni = models.IntegerField(default=1)
    malumot = models.TextField()
    rasm = models.CharField(max_length=255)

    def __str__(self):
        return self.fakulteti


class Navoiy1(models.Model):
    fakulteti = models.CharField(max_length=50)
    yonalishlarisoni = models.IntegerField(default=1)
    malumot = models.TextField()
    rasm = models.CharField(max_length=255)

    def __str__(self):
        return self.fakulteti 


class Toshkent(models.Model):
    fakulteti = models.CharField(max_length=50)
    yonalishlarisoni = models.IntegerField(default=1)
    malumot = models.TextField()
    rasm = models.CharField(max_length=255)

    def __str__(self):
        return self.fakulteti


class Toshkent1(models.Model):
    fakulteti = models.CharField(max_length=50)
    yonalishlarisoni = models.IntegerField(default=1)
    malumot = models.TextField()
    rasm = models.CharField(max_length=255)

    def __str__(self):
        return self.fakulteti

