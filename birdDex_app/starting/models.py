from django.db import models

# Create your models here.
class Bird (models.Model):
    name = models.CharField("Bird Name", max_length=120)
    description = models.TextField("Bird Description", max_length=120)
    point_value = models.BigIntegerField(blank=True)
    picture = models.ImageField()
    def __str__(self):
        return self.name

class User (models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name
    #needs for passwords and usernames?

class BirdFound (models.Model):
    #name = models.CharField("Bird Name", max_length=120)
    picture = models.ImageField()
    #varible to verify if it is a bird or not?? should establish a specific model for somehting that was not found or unable to be verified
    birdfound = models.ForeignKey(Bird, blank = True, null = True, on_delete=models.CASCADE)
    finders = models.ManyToManyField(User, blank=True)
    models.field
    def __str__(self):
        return self.name
