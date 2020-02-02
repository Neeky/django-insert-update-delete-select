from django.db import models
from django.urls import reverse
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=24)
    age = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("person-detail-view", args=[str(self.id)])

    def __str__(self):
        return f"Person Instance id={self.id} name={self.name} age={self.age}"


class Article(models.Model):
    """
    """
    title = models.CharField(max_length=24)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("person-detail-view", args=[str(self.id)])

    def __str__(self):
        return f"Article Instance id={self.id} title={self.title}"
