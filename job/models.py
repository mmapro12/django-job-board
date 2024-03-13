from django.db import models

# Create your models here.

JOB_TYPES = (
    ("Full-Time","Full-Time"),
    ("Part-Time","Part-Time"),

)

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPES)
    description = models.TextField(max_length=1000)
    publish_date = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
