from django.db import models

# Create your models here.
class Subscriber(models.Model):

    email = models.EmailField( max_length=254)
    topics  = models.ManyToManyField("content.Topic")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Subscriber_detail", kwargs={"pk": self.pk})