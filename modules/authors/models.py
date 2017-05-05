from django.db import models

# Create your models here.
class Author(models.Model):
    CATEGORIES = {
        ("ACC","Action"),
        ("ADV","Adventure"),
        ("COM","Comic"),
        ("CRM","Crime"),
        ("FIC","Fiction"),
        ("FAN","Fantasy"),
        ("GOT","Gothic"),
        ("HIS","Historical"),
        ("HOR","Horror"),
        ("POL","Political"),
        ("PYS","Psychological"),
        ("ROM","Romance"),
        ("SAG","Saga"),
        ("SCI","Science"),
        ("THR","Thriller"),
            }
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    bio = models.TextField()
    sex = models.CharField(choices=(('F','Female'),('M','Male')), max_length=16,blank=True)
    category = category = models.CharField(max_length=100,choices=CATEGORIES)
    age = models.IntegerField()
    alive = models.BooleanField(default=True)

    def __str__(self):
        return "Author: %s %s" % (self.name,self.lastname)
