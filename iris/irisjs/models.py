from django.db import models

# Create your models here.

class File(models.Model):
    id = models.CharField(primary_key=True, max_length=6) #criamos um campo do tipo Caractere que será a primary key, com tamanho máximo 6
    sepal_length = models.FloatField() #criamos um campo do tipo Float (permite decimal)
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.CharField(max_length=20)
    def __str__(self):
        return self.id
