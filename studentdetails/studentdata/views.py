from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentDetail

# Create your views here.
def index(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'index.html',{'form':form})

def show(request):
    students=StudentDetail.objects.all()
    return render(request,'show.html',{'students':students})

def edit(request,sid):
    student_data=StudentDetail.objects.get(stu_id=sid)
    return render(request,'update.html',{'sdata':student_data})

def update(request,sid):
    student_data = StudentDetail.objects.get(stu_id=sid)
    form=StudentForm(request.POST,instance=student_data)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'update.html',{'sdata':student_data})
def delete(request,sid):
    student_data = StudentDetail.objects.get(stu_id=sid)
    student_data.delete()
    return redirect('/show')


