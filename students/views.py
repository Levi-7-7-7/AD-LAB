from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Student
from students.forms import StudentForm

# View to list all students
def students(request):
    students_list = Student.objects.all().values()
    template = loader.get_template('all_students.html')
    context = {'students': students_list}
    return HttpResponse(template.render(context, request))

# View to show student details
def details(request, id):
    student = Student.objects.get(id=id)
    template = loader.get_template('student_details.html')
    context = {'student': student}
    return HttpResponse(template.render(context, request))

# View to handle student entry (form submission)
def student_entry(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()

    template = loader.get_template('student_entry.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

# Success page after form submission
def success_page(request):
    return render(request, 'success.html')
