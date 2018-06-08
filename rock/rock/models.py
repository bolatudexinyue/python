from django.db import models

class userinfo(models.Model):
    username = models.CharField(max_length=32,null = True)
    password = models.CharField(max_length=64,null = True)
    email = models.CharField(max_length = 32,null = True)
    class Meta:
        db_table = 'userinfo'

class movies(models.Model):
    name = models.CharField(max_length=64,null = True)
    detail = models.CharField(max_length=64,null = True)
    Img = models.CharField(max_length = 256,null = True)
    time = models.CharField(max_length=16,null=True)
    class Meta:
        db_table = 'movies'

class collected(models.Model):
    user_list = models.ForeignKey(to='userinfo',db_column='uid')
    movie_list = models.ForeignKey(to='movies',db_column='mid')
    class Meta:
        db_table = 'collexted'

