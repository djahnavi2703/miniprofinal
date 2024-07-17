from django.core.validators import RegexValidator
from django.db import models
import datetime


# Create your models here.
alpha_validator = RegexValidator(
    regex=r'^[a-zA-Z]*$',
    message='Only alphabetic characters are allowed.'
)
integer_validator = RegexValidator(
    regex=r'^[0-9]+$',
    message='Enter only integer.'
)
special_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9]+$',
    message='Enter proper PaperCode.'
)
            #EmployeeMaster table-------->>>>>>>>
class EmployeeModel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10,unique=True)
    email=models.EmailField()
    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)

            #BatchMaster table-------->>>>>>>>>
batch=((" ","Select_Batch"),("2020-2022","2020-2022"),
       ("2021-2023","2021-2023"),("2022-2024","2022-2024"),
       ("2023-2025","2023-2025"),("2024-2025","2024-2025"),
       ("2025-2027","2025-2027"),("2026-2028","2026-2028"),
       ("2027-2029","2027-2029"),("2028-2030","2028-2030"))
class BatchMaster(models.Model):
    batchno=models.CharField(max_length=2,validators=[integer_validator])
    batchid= models.CharField(max_length=10,choices=batch,default=" ")     
    def __str__(self):
        return self.batchid
                #PaperMaster table-------->>>>>>>
papertype=((" ","select PaperType"),
           ("CompulFoundation","CompulFoundation"),("Core","Core"),
           ("Generic Elective","Generic Elective"),("lab","lab"),
           ("open Elective","open Elective"),("compulsory","compulsory"))
class PaperMaster(models.Model):
    papername=models.CharField(max_length=25, validators=[special_validator])
    papercode=models.CharField(max_length=8,validators=[special_validator])
    papertype=models.CharField(max_length=20,choices=papertype,default=" ")
    papersheetname=models.CharField(max_length=10, validators=[alpha_validator])
    def __str__(self):
        return self.papername
                #Course Master Table ---------->>>>>>>
class CourseMaster(models.Model):
    course=models.CharField(max_length=6,validators=[alpha_validator])      
    courseid=models.CharField(max_length=5,validators=[integer_validator]) 
    def __str__(self):
        return self.course
                 #Sem Master Table------->>>>>
sem=((" ","select_semister"),
     ("First","First"),
     ("Second","Second"),
     ("Third","Third"),
     ("Fourth","Fourth"))
class SemMaster(models.Model):
    sem=models.CharField(max_length=15,choices=sem,default=" ")
    semid=models.CharField(max_length=6, validators=[integer_validator])  
    def __str__(self):
        return self.sem
                 #Exam Master table--------->>>>>
type=((" ","select-ExamType"),
     ("Internal-I","Internal-I"),
     ("Internal-II","Internal-II"),
     ("External","External"))
class ExamMaster(models.Model):
    examid=models.CharField(max_length=6, validators=[integer_validator])
    examtype=models.CharField(max_length=15, choices=type,default=" ")
    def __str__(self):
        return self.examtype
                #Student Master Table---------->>>>>
class StudentMaster(models.Model):
    studentname=models.CharField(max_length=40, validators=[alpha_validator])
    course=models.ForeignKey(CourseMaster, on_delete=models.CASCADE, default=1)
    sem=models.ForeignKey(SemMaster, on_delete=models.CASCADE, default=1)
    studentregno=models.CharField(max_length=6, validators=[integer_validator])
    batchid=models.ForeignKey(BatchMaster, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.studentname

                 #StudentInternalTrans-------->>>>>>>


       

