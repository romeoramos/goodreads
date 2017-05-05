from django.db import models

# Create your models here.

class Books(models.Model):
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
    idBook = models.AutoField(primary_key=True)
    name = models.CharField(max_lenght=50)
    author = models.ForeignKey(Authors,on_delete=models.CASCADE)
    ISBN = models.CharField(max_lenght=10)
    publication_date = models.DateField()
    cover = models.URLField()
    description = models.TextField()
    rating = models.IntegerField()
    category = models.CharField(max_length=30,choices=CATEGORIES)

class Comments(models.Model):
    idComment = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    comment = models.TextField()
