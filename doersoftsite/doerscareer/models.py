from django.db import models

''' Career Model : Includes data about the types of career '''


class CareerCategory(models.Model):
    career_choices = [
        ('Job', 'Job'),
        ('Internship', 'Internship')
    ]


    skill_type = [
        ('Web Developer', 'Web Developer'),
        ('Wordpress Developer', 'Wordpress Developer'),
        ('Designer', 'Designer'),
        ('Content Writing', 'Content Writing'),
    ]

    career_type = models.CharField(max_length = 15, choices = career_choices)
    skill_type = models.CharField(max_length = 50, choices = skill_type)

    def __str__(self):
        return self.career_type

class Career(models.Model):
    career_type = models.ForeignKey(CareerCategory, blank = False, on_delete = models.CASCADE)
    job_title = models.CharField(max_length = 125)
    job_description = models.TextField(max_length = 500)
    job_requirements = models.TextField(max_length = 125)
    created_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.job_title

class CareerForm(models.Model):
    job_id = models.ForeignKey(Career, blank = False, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 50)
    email = models.EmailField(blank = False, null = False)
    phone = models.CharField(max_length = 10)
    photo = models.ImageField(upload_to = 'job_form_photo')
    cv = models.FileField(upload_to = 'job_form_cv')
    your_strength_description = models.TextField(max_length = 150)
    how_did_you_know_about_us = models.CharField(max_length = 50)
    referred_by = models.CharField(max_length = 100, blank = True, null = False)

    def __str__(self):
        return self.full_name


