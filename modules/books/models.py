from django.db import models
from modules.authors.models import Author
from django.conf import settings
# Create your models here.

class Book(models.Model):
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
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_books')
    ISBN = models.CharField(max_length=100,unique=True)
    publication_date = models.DateField(null=True)
    cover = models.URLField(blank=True,null=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3,decimal_places=2)
    category = models.CharField(max_length=100,choices=CATEGORIES)

    def __str__(self):
        return "Book: %s" % (self.name)

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='book_comments')
    comment = models.TextField()
