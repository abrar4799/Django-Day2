from django.db import models


class register(models.Model):
    userName = models.Field(null=False)
    password =  models.Field()
    email = models.EmailField(null=False)


