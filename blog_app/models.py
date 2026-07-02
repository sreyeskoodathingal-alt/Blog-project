from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=10)
    content = models.TextField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
    
class Command(models.Model):
    name= models.CharField(max_length=100)
    command = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    blog= models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
       return self.name



