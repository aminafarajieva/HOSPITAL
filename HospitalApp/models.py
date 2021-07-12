from random import randrange
from django.db import models
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    name = models.CharField('Название',max_length=100)
    Chui = 'Chui'
    IK = 'IK'
    Talas = 'Talas'
    Naryn = 'Naryn'
    Osh = 'Osh'
    Batken = 'Batken'
    REGION = [
        (Chui, 'Чуйская'),
        (IK, 'Иссык-Кульская'),
        (Talas, 'Таласская'),
        (Naryn, 'Нарынская'),
        (Osh, 'Ошская'),
        (Batken, 'Баткенская'), ]
    region = models.CharField('Область',max_length=9,choices=REGION,default=Chui,)
    ocpo = models.CharField('ОКПО',max_length=4,unique=True)
    gov = models.BooleanField('Государственное',default=False)
    doctors = models.OneToOneField('MainDoctor',on_delete=models.PROTECT,verbose_name='Главрач')
    maxn = models.IntegerField(verbose_name='Макс.количество сотрудников',default=100)


# Hospital:
# name
# region
# ocpo
# gov
# maindoctor
# maxnum

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'


class MainDoctor(models.Model):
    name = models.CharField('ФИО',max_length=100)
    pin = models.CharField('ПИН',max_length=14)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона',max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Главрач'
        verbose_name_plural = 'Главрачи'

    def get_absolute_url(self):
        return reverse('main')

# Main doctor:
# name
# pin
# birthdate
# phone

class Nurses(models.Model):
    name = models.CharField('ФИО',max_length=100)
    pin = models.CharField('ПИН',max_length=14)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона',max_length=10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'

def random_nurse():
    n = Nurses.objects.count()
    return Nurses.objects.all()[randrange(n)]

    def get_absolute_url(self):
        return reverse('main')


# Nurses:
# name
# pin
# birthdate
# phone


class Doctor(models.Model):
    therapist = 'Терапевт'
    surgeon = 'Хирург'
    POSITION = [
        (therapist,'Терапевт'),
        (surgeon,'Хирург')
    ]
    position = models.CharField('Терапевт/Хирург',max_length=9,choices=POSITION,default=therapist,)
    name = models.CharField('ФИО',max_length=100)
    pin = models.CharField('ПИН',max_length=14)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона',max_length=10)
    hospitals = models.ForeignKey('Hospital',on_delete=models.PROTECT,verbose_name='Больница',default=1)
    nurse = models.ForeignKey('Nurses',on_delete=models.PROTECT,verbose_name='Медсестра',default=random_nurse)

    def __str__(self):
        return f"{self.name} - Медсестра: {self.nurse}"
    
    class Meta:
        verbose_name = 'Лечащий врач'
        verbose_name_plural = 'Лечащие врачи'

    def get_absolute_url(self):
        return reverse('main')
        
        

# Doctor:
# position
# name
# pin
# birthdate
# phone


class Patients(models.Model):
    name = models.CharField('ФИО',max_length=100)
    pin = models.CharField('ПИН',max_length=14)
    birthdate = models.DateField('Дата рождения')
    phone = models.CharField('Номер телефона',max_length=10)
    why = models.CharField('Причина обращения в больницу',max_length=200)
    hospital = models.ForeignKey('Hospital',on_delete=models.PROTECT,verbose_name='Больница')
    doctor = models.ForeignKey('Doctor',on_delete=models.PROTECT,verbose_name='Лечащий врач',related_name="counts")
    nurse = models.ForeignKey('Nurses',on_delete=models.PROTECT,verbose_name='Медсестра')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def get_absolute_url(self):
        return reverse('main')
# Patients:
# name
# pin
# birthdate
# phone
# why
# hospital
# doctor
# nurse

