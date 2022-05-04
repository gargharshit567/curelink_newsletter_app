from django.db import models

# Create your models here.
class Subscriber(models.Model):

    email = models.EmailField( max_length=254)
    topic  = models.ManyToManyField("Topic")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Subscriber_detail", kwargs={"pk": self.pk})


class Topic(models.Model):

    topic  = models.CharField(primary_key=True, max_length=255)    
    

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("Topic_detail", kwargs={"pk": self.pk})


class Content(models.Model):

    content_text = models.TextField()
    content_desc = models.TextField()
    time = models.DateTimeField()
    topic = models.ForeignKey("Topic",null=False, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.content_desc

    def get_absolute_url(self):
        return reverse("Content_detail", kwargs={"pk": self.pk})
