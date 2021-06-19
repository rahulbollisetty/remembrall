from django.db import models

class PhoneNumber(models.Model):
    phn_no = models.CharField(max_length=12)

    def __str__(self):
        return self.phn_no