from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title


class Album(models.Model):

    class Meta:

        db_table = 'album'

    title = models.CharField(max_length=200)
    quantidade_musica = models.IntegerField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title