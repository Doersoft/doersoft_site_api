from django.db import models

''' Doers Client Model : Includes data for the client who have been served by DoerSoft '''

class DoersClients(models.Model):
    client_name = models.CharField(max_length=200)
    client_logo = models.ImageField(upload_to = 'client_logo')
    industry_type = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.client_name

''' Doers Products Model : Includes data for the product developed by/from DoerSoft'''

class DoersProduct(models.Model):
    product_name = models.CharField(max_length=250)
    client_id = models.ForeignKey(DoersClients, on_delete = models.CASCADE)
    product_link = models.URLField(max_length = 128, unique = True, blank = True)
    product_image = models.ImageField(upload_to = 'product_image')
    product_description = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return self.product_name