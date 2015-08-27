from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)
    # What is blank = True and null = True ?
    def __unicode__(self) :
        return self.title
    # Why there is a Meta here ?
    class Meta:
        ordering = ['-date_time']
