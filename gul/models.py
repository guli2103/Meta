from django.db import models

class Moychechak(models.Model):
    turi = models.CharField(max_length=20)
    rasm = models.CharField(max_length=255)
    malumot = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turi


class Lola(models.Model):
    turi = models.CharField(max_length=20)
    rasm = models.CharField(max_length=255)
    malumot = models.TextField()
    rangi = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turi        


class Atirgul(models.Model):
    turi = models.CharField(max_length=20)
    rasm = models.CharField(max_length=255)
    malumot = models.TextField()
    rangi = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turi


class Kaktus(models.Model):
    turi = models.CharField(max_length=20)
    rasm = models.CharField(max_length=255)
    malumot = models.TextField()
    rangi = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turi

class Binafsha(models.Model):
    turi = models.CharField(max_length=20)
    rasm = models.CharField(max_length=255)
    malumot = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turi