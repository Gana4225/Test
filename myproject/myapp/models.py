from django.db import models

class pdata(models.Model):
    patient_name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()
    bed_no = models.IntegerField()
    problem = models.TextField(max_length=500)
    doa = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient_name} {self.bed_no}"

class hiraaa(models.Model):
    name = models.CharField(max_length=50)
    age=models.ForeignKey('pdata',related_name='pdata',on_delete=models.CASCADE,default='')