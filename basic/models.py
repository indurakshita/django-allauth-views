from django.db import models


class PersonModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.name




    