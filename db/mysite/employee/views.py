from django.shortcuts import render
from django.db.models import Avg,Max,Min,Count,Sum
from django.db import connection
from .models import Employee
# Create your views here.
def employee_view(request):
    if request.method == 'POST':
        context = {
                'employees': list(Employee.objects.all()),
                'data': []
                }
        if(request.POST.get('count',None)):
            print(Employee.objects.aggregate(Count('job_title',distinct=True)))
            job_count=Employee.objects.aggregate(Count('job_title',distinct=True))
            context['data'].append(job_count)
        if(request.POST.get('max',None)):
            print(Employee.objects.aggregate(Max('salary')))
            max_salary=Employee.objects.aggregate(Max('salary'))
            context['data'].append(max_salary)
        if(request.POST.get('min',None)):
            print(Employee.objects.aggregate(Min('salary')))
            min_salary=Employee.objects.aggregate(Min('salary'))
            context['data'].append(min_salary)
        if(request.POST.get('avg',None)):
            print(Employee.objects.aggregate(Avg('salary')))
            avg_salary=Employee.objects.aggregate(Avg('salary'))
            context['data'].append(avg_salary)
        if(request.POST.get('sum',None)):
            print(Employee.objects.aggregate(Sum('salary')))
            sum_salary=Employee.objects.aggregate(Sum('salary'))
            context['data'].append(sum_salary)
        query=request.POST.get('my_sql',None)
        print(type(context['data']))
        print(query)
        if(query!=None):
            print('query',query)
            with connection.cursor() as cursor:
                cursor.execute(query)
                items=list(cursor.fetchall())
                context = {'items': items,
                       'employees': list(Employee.objects.all())
                }
            return render(request, 'employee/employee.html',context)
        return render(request, 'employee/employee.html',context)
    context = {
                'employees': list(Employee.objects.all())
            }
    return render(request, 'employee/employee.html',context)