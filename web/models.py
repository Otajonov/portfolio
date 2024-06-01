from django.db import models


class Testimonial(models.Model):
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to='clients/')
    message = models.TextField()
    link = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to='clients/')
    link = models.URLField()
    index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telegram = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name} on {self.date}"



class PortfolioCategory(models.Model):

    name = models.CharField(max_length=50)
    index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title


class Skill(models.Model):

    name = models.CharField(max_length=50)
    percentage = models.IntegerField()
    index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
        
        
class Language(models.Model):

    name = models.CharField(max_length=50)
    percentage = models.IntegerField()
    index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class PostCategory(models.Model):

    name = models.CharField(max_length=50)
    index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class PostItem(models.Model):
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='post/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title