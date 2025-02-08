from django.db import models


# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    due_date  = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} {self.description} {self.due_date} {self.status}"