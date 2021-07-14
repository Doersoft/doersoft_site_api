from django.db import models

''' Contact Form Model : Includes data to be recieved when someone want to contact with the team '''

class Contact(models.Model):
    your_name = models.CharField(max_length = 125)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length = 500)
    created_date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.your_name
