from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=100, null=False)
    sex = models.CharField(max_length=100)
    exp = models.IntegerField(null=True)
    resume = models.FileField(null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name
