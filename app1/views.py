from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *


# Create your views here.

def smms(request):
    return render(request,'master.html')

def insert_employee(request):
    context={}
    ob_form=EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return redirect('view_employee')
    context['form']=ob_form
    return render(request,"insert_employee.html",context)
def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    temp=loader.get_template("view_employee.html")
    context={
        'data':ob
    }
    return HttpResponse(temp.render(context,request))
def delete_employee(request,pk):
    EmployeeModel.objects.get(id=pk).delete()
    return render(request,"delete_employee.html")
def del_employee(request):
    ob=EmployeeModel.objects.all().values()
    temp=loader.get_template("del_employee.html")
    context={
        'data':ob
    }
    return HttpResponse(temp.render(context,request))
def update_employee(request,pk):
    obe=get_object_or_404(EmployeeModel,id=pk)
    if request.method=='POST':
        obf=EmployeeForm(request.POST,instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('updat_employee')
    else:
        formdata=EmployeeForm(instance=obe)
    return render(request,"update_employee.html", {'form':formdata})
def updat_employee(request):
    ob=EmployeeModel.objects.all().values()
    temp=loader.get_template("updat_employee.html")
    context={
        'data':ob
    }
    return HttpResponse(temp.render(context,request))
def search_employee(request):
    if request.method=='GET':
        form=EmployeeSearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data.get('query')
            results=EmployeeModel.objects.filter(first_name=query)
        else:
            results=None
    else:
        form=EmployeeSearchForm()
        results=None
    return render(request,'search_employee.html',{'form':form,'results':results})

def batch_edit(request, id):
    obj=get_object_or_404(BatchMaster,pk=id)
    if request.method == 'POST':
        form = BatchForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('batch_all_details')
    else:
        form = BatchForm(instance=obj)
    return render(request,'batch_edit.html',{'form':form})
def batch_detail(request,id):
    obj=get_object_or_404(BatchMaster,pk=id)
    return render(request,'batch_detail.html',{'batch':batch})
def batch_all_details(request):
    ob=BatchMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('batch_all_details.html')
    return HttpResponse(temp.render(context,request))
def batch_search(request):
    if request.method == 'GET':
        form = BatchMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = BatchMaster.objects.filter(batchid=query)  
        else:
            results = None
    else:
        form = BatchMasterForm()
        results = None
    
    return render(request, 'batch_search.html', {'form': form, 'results': results})
def display_batch(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template("batch_master.html")
    context={
        'data':allbatch
    }
    return HttpResponse(temp.render(context,request))
def batch_insert(request):
    context={}
    context['form']=BatchForm()
    return render(request,"batch_insert.html",context)
def process_batch_entry(request):
    if request.method=='POST':
        batchid_inp=request.POST.get('batchid')
        batchno_inp=request.POST.get('batchno')
        ob=BatchMaster(batchid=batchid_inp,batchno=batchno_inp,)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displaybatchinput(request):
    return render(request,"batch_entry.html")
def delete(request,pk):
    BatchMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_batch/")
def batch_delete(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template("batch_delete.html")
    context ={
        'data':allbatch
        }
    return HttpResponse(temp.render(context,request))
    

def course_edit(request, id):
    obj=get_object_or_404(CourseMaster,pk=id)
    if request.method == 'POST':
        form = CourseForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('course_all_details')
    else:
        form = CourseForm(instance=obj)
    return render(request,'course_edit.html',{'form':form})
def course_detail(request,id):
    obj=get_object_or_404(CourseMaster,pk=id)
    return render(request,'course_detail.html',{'course':course})
def course_all_details(request):
    ob=CourseMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('course_all_details.html')
    return HttpResponse(temp.render(context,request))
def course_search(request):
    if request.method == 'GET':
        form = CourseMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = CourseMaster.objects.filter(course=query)  
        else:
            results = None
    else:
        form = CourseMasterForm()
        results = None
    
    return render(request, 'course_search.html', {'form': form, 'results': results})
def display_course(request):
    allcourse=CourseMaster.objects.all().values()
    temp=loader.get_template("course_master.html")
    context={
        'data':allcourse
    }
    return HttpResponse(temp.render(context,request))
def course_insert(request):
    context={}
    context['form']=CourseForm()
    return render(request,"course_insert.html",context)
def process_course_entry(request):
    if request.method=='POST':
        course_inp=request.POST.get('course')
        courseid_inp=int(request.POST.get('courseid'))
        ob=CourseMaster(course=course_inp,courseid=courseid_inp)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displaycourseinput(request):
    return render(request,"course_entry.html")
def delete1(request,pk):
    CourseMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_course/")
def course_delete(request):
    allcourse=CourseMaster.objects.all().values()
    temp=loader.get_template("course_delete.html")
    context ={
        'data':allcourse
        }
    return HttpResponse(temp.render(context,request))

def sem_edit(request, id):
    obj=get_object_or_404(SemMaster,pk=id)
    if request.method == 'POST':
        form = SemForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('sem_all_details')
    else:
        form = SemForm(instance=obj)
    return render(request,'sem_edit.html',{'form':form})
def sem_detail(request,id):
    obj=get_object_or_404(SemMaster,pk=id)
    return render(request,'sem_detail.html',{'sem':sem})
def sem_all_details(request):
    ob=SemMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('sem_all_details.html')
    return HttpResponse(temp.render(context,request))
def sem_search(request):
    if request.method == 'GET':
        form = SemMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = SemMaster.objects.filter(sem=query)  
        else:
            results = None
    else:
        form = SemMasterForm()
        results = None
    
    return render(request, 'sem_search.html', {'form': form, 'results': results})
def display_sem(request):
    allsem=SemMaster.objects.all().values()
    temp=loader.get_template("sem_master.html")
    context={
        'data':allsem
    }
    return HttpResponse(temp.render(context,request))
def sem_insert(request):
    context={}
    context['form']=SemForm()
    return render(request,"sem_insert.html",context)
def process_sem_entry(request):
    if request.method=='POST':
        sem_inp=request.POST.get('sem')
        semid_inp=int(request.POST.get('semid'))        
        ob=SemMaster(sem=sem_inp,semid=semid_inp)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displayseminput(request):
    return render(request,"sem_entry.html")
def delete4(request,pk):
    SemMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_sem/")
def sem_delete(request):
    allsem=SemMaster.objects.all().values()
    temp=loader.get_template("sem_delete.html")
    context ={
        'data':allsem
        }
    return HttpResponse(temp.render(context,request))

def paper_edit(request, id):
    obj=get_object_or_404(PaperMaster,pk=id)
    if request.method == 'POST':
        form = PaperForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('paper_all_details')
    else:
        form = PaperForm(instance=obj)
    return render(request,'paper_edit.html',{'form':form})
def paper_detail(request,id):
    obj=get_object_or_404(PaperMaster,pk=id)
    return render(request,'paper_detail.html',{'paper':paper})
def paper_all_details(request):
    ob=PaperMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('paper_all_details.html')
    return HttpResponse(temp.render(context,request))
def paper_search(request):
    if request.method == 'GET':
        form = PaperMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = PaperMaster.objects.filter(papercode=query)  
        else:
            results = None
    else:
        form = PaperMasterForm()
        results = None
    
    return render(request, 'paper_search.html', {'form': form, 'results': results})
def display_paper(request):
    allpaper=PaperMaster.objects.all().values()
    temp=loader.get_template("paper_master.html")
    context={
        'data':allpaper
    }
    return HttpResponse(temp.render(context,request))
def paper_insert(request):
    context={}
    context['form']=PaperForm()
    return render(request,"paper_insert.html",context)
def process_paper_entry(request):
    if request.method=='POST':
        papername_inp=request.POST.get('papername')
        papercode_inp=request.POST.get('papercode')
        papertype_inp=request.POST.get('papertype')
        papersheetname_inp=request.POST.get('papersheetname')
        ob=PaperMaster(papername=papername_inp,papercode=papercode_inp,papertype=papertype_inp,papersheetname=papersheetname_inp)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displaypaperinput(request):
    return render(request,"paper_entry.html")
def delete5(request,pk):
    PaperMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_paper/")
def paper_delete(request):
    allpaper=PaperMaster.objects.all().values()
    temp=loader.get_template("paper_delete.html")
    context ={
        'data':allpaper
        }
    return HttpResponse(temp.render(context,request))

def exam_edit(request, id):
    obj=get_object_or_404(ExamMaster,pk=id)
    if request.method == 'POST':
        form = ExamForm(request.POST ,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('exam_all_details')
    else:
        form = ExamForm(instance=obj)
    return render(request,'exam_edit.html',{'form':form})
def exam_detail(request,id):
    obj=get_object_or_404(ExamMaster,pk=id)
    return render(request,'exam_detail.html',{'exam':exam})
def exam_all_details(request):
    ob=ExamMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('exam_all_details.html')
    return HttpResponse(temp.render(context,request))
def exam_search(request):
    if request.method == 'GET':
        form = ExamMasterForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = ExamMaster.objects.filter(examid=query)  
        else:
            results = None
    else:
        form = ExamMasterForm()
        results = None
    
    return render(request, 'exam_search.html', {'form': form, 'results': results})
def display_exam(request):
    allexam=ExamMaster.objects.all().values()
    temp=loader.get_template("exam_master.html")
    context={
        'data':allexam
    }
    return HttpResponse(temp.render(context,request))
def exam_insert(request):
    context={}
    context['form']=ExamForm()
    return render(request,"exam_insert.html",context)
def process_exam_entry(request):
    if request.method=='POST':
        examid_inp=int(request.POST.get('examid'))
        examtype_inp=request.POST.get('examtype')
        ob=ExamMaster(examid=examid_inp,examtype=examtype_inp)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displayexaminput(request):
    return render(request,"exam_entry.html")
def delete6(request,pk):
    ExamMaster.objects.get(id=pk).delete()
    return HttpResponseRedirect("/app1/display_exam/")
def exam_delete(request):
    allexam=ExamMaster.objects.all().values()
    temp=loader.get_template("exam_delete.html")
    context ={
        'data':allexam
        }
    return HttpResponse(temp.render(context,request))

def process_student_entry(request):
    if request.method=='POST':
        studentname_inp=request.POST.get('studentname')
        studentregno_inp=request.POST.get('studentregno')
        ob=StudentMaster(studentname=studentname_inp,studentregno=studentregno_inp)
        ob.save()
        return HttpResponse("DATA SUCCESSFULLY INSERTED")
    else:
        return HttpResponse("INVALID REQUEST")
def displaystudentinput(request):
    return render(request,"student_entry.html")





