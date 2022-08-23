from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    addr = models.CharField(max_length=1500)
    pin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

class category_master(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class label_master(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label

class label_category_map(models.Model):
    label_id = models.IntegerField()
    category_id = models.IntegerField()


class data_set(models.Model):
    label_id = models.IntegerField()
    fpath = models.CharField(max_length=150)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.fpath

class user_pic(models.Model):
    user_id = models.IntegerField()
    pic_path = models.CharField(max_length=150)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.pic_path

class user_post(models.Model):
    user_id = models.IntegerField()
    msg = models.CharField(max_length=1500)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.msg

class user_question(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    msg = models.CharField(max_length=1500)
    reply = models.CharField(max_length=1500)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)
    rdt = models.CharField(max_length=150)
    rtm = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.msg
