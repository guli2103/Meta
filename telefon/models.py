from django.db import models

class Infinix(models.Model):
    turi = models.CharField(max_length=30)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi

class Samsung(models.Model):
    turi = models.CharField(max_length=30)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi

class Apple(models.Model):
    turi = models.CharField(max_length=30)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi

class Redme(models.Model):
    turi = models.CharField(max_length=30)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi

class Vivo(models.Model):
    turi = models.CharField(max_length=30)
    rasmi = models.CharField(max_length=255)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return self.turi












