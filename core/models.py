from django.db import models

# Create your models here.
class Contact(models.Model):
  your_email = models.CharField(max_length=300)
  message_for_me = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.your_email