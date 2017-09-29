from django.db import models


# Create your models here.
class Articles(models.Model):
    articleTitle = models.TextField(max_length=20)
    articleContent = models.TextField(max_length=1500)
    articleCreatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Articles"