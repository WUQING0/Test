from django.db import models

# Create your models here.
class userRegister(models.Model):
    username=models.CharField(max_length=20)
    useremail=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class ardiunoData(models.Model):
    Humidity=models.FloatField(default=0)
    Temperature=models.FloatField(default=0)
    Soil_1=models.FloatField(default=0)
    Soil_2=models.FloatField(default=0)
    Soil_3=models.FloatField(default=0)
    Soil_4=models.FloatField(default=0)
    Avg_soil=models.FloatField(default=0)

#
class personal_information(models.Model):
    username=models.CharField(default='小明',max_length=30)
    usersex=models.CharField(default='男',max_length=4)
    userNation=models.CharField(default='汉',max_length=50)
    userbirthday=models.DateField(verbose_name="出生日期")
    userage=models.IntegerField()
    user_cai_type=models.CharField(default="黄豆",max_length=20)
    userIdCard=models.CharField(max_length=18)
    userFaith=models.CharField(max_length=20)
    userRemarks=models.CharField(max_length=100)
    userphone=models.CharField(max_length=11)
    userAddress=models.CharField(max_length=200)
    userImage=models.ImageField()

class pipei(models.Model):
    testbox=models.CharField(max_length=3)
    plant_type=models.CharField(max_length=20)