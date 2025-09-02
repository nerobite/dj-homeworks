from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # students = Student.objects.order_by('name', 'group').prefetch_related() #время выполнения примерно 1 мс
    students = Student.objects.all().prefetch_related()  # время выполнения примерно 0.64 мс
    context = {
        'object_list': students
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
