from django.db import models


class Authors(models.Model):
    id_author = models.IntegerField(db_column='ID_author', primary_key=True)
    author = models.TextField(unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AUTHORS'

    def __str__(self):
        return self.author


class Books(models.Model):
    id_book = models.IntegerField(db_column='ID_book', primary_key=True)
    author = models.TextField(blank=True, null=True)
    book_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BOOKS'

    def __str__(self):
        return str(self.book_name) + '  -  ' + str(self.author)