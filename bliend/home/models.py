from django.db import models


class resume(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField()
    age =models.IntegerField(max_length=2)
    email =models.EmailField()
    phone = models.CharField(max_length=10)
    skill1 =models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 =  models.CharField(max_length=50)
    skill4 = models.CharField(max_length=50)
    skill5 = models.CharField(max_length=50)
    degree1 =models.CharField(max_length=50)
    college1 =  models.CharField(max_length=100)
    year1 = models.DateField(null=True)
    degree2 =models.CharField(max_length=50)
    college2 =models.CharField(max_length=100)
    year2 =models.DateField(null=True)
    college3 =models.CharField(max_length=100)
    year3 =models.DateField(null=True)
    degree3 = models.CharField(max_length=100)
    lang1 = models.CharField(max_length=50)
    lang2 = models.CharField(max_length=50)
    lang3 =  models.CharField(max_length=50)	 
    project1=  models.CharField(max_length=50)
    durat1 = models.CharField(max_length=50) 
    desc1 = models.CharField(max_length=100000)
    project2 = models.CharField(max_length=50)
    durat2 = models.CharField(max_length=50)
    desc2 =  models.CharField(max_length=10000)
    company1 = models.CharField(max_length=50)
    post1 =  models.CharField(max_length=50)
    duration1 = models.CharField(max_length=50) 
    lin11 =  models.CharField(max_length=1000)
    company2 = models.CharField(max_length=1000)
    post2 = models.CharField(max_length=50)
    duration2 = models.CharField(max_length=50)
    lin21 =  models.CharField(max_length=1000)
    ach1 = models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.name}'


class login(models.Model):
    email=models.EmailField(max_length=50,null=True)
    passwrd=models.CharField(max_length=15,null=True)

    def __str__(self):
        return f'{self.email}'


