from django.db import models

import os

# 데이터베이스 관련된 정보를 적는곳.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
