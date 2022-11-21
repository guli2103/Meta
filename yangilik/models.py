from django.db import models

class Yangilik1(models.Model):
    mavzusi = models.CharField(max_length=255)
    mazmuni = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzusi

class Yangilik2(models.Model):
    mavzusi = models.CharField(max_length=255)
    mazmuni = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzusi

class Yangilik3(models.Model):
    mavzusi = models.CharField(max_length=255)
    mazmuni = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzusi

class Yangilik4(models.Model):
    mavzusi = models.CharField(max_length=255)
    mazmuni = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzusi

class Yangilik5(models.Model):
    mavzusi = models.CharField(max_length=255)
    mazmuni = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzusi









