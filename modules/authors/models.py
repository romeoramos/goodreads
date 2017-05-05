from django.db import models

# Create your models here.
class Authors(models.Model):
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
    idAuthor = models.AutoField(primary_key=True)
    name = models.CharField(max_lenght=50)
    lastname = models.CharField(max_lenght=50)
    nationality = models.CharField(max_lenght=50)
    bio = models.TextField()
    sex = models.CharField(max_lenght=10)
    category = category = models.CharField(max_length=30,choices=CATEGORIES)
    age = models.IntegerField()
    alive = models.BooleanField()
