from django.db import models


class KeySkill(models.Model):

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tech-icons', default=None, null=True)
    activeColor = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class KeySubSkill(models.Model):
    key_skill = models.ForeignKey(KeySkill, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tech-icons', default=None, null=True)

    def __str__(self):
        return self.name + " (" + str(self.key_skill) + ")"

