from django.shortcuts import render
from django.db import connection
from .models import Customer
# Create your views here.
def customer_view(request):
    if request.method == 'POST':
        query=request.POST.get('my_sql',None)
        search=request.POST.get('s_name',None)
        name=request.POST.get('name',None)
        sex=request.POST.get('sex',None)
        tel=request.POST.get('tel',None)
        email=request.POST.get('email',None)
        if(search!=None):
            try:
                customer=Customer.objects.get(name=search)
                print('hi')
            except:
                customer=None
            print(search)
            print(type(customer))
            context = {
            's_customer': customer
            }
            return render(request, 'customer/customer.html',context)
        
        elif(query!=None):
            print('query',query)
            with connection.cursor() as cursor:
                cursor.execute(query)
                items=list(cursor.fetchall())
                context = {'items': items}
            return render(request, 'customer/customer.html',context)
        else:
            c=Customer.objects.create(name=name,sex=sex,tell=tel,mail=email)
            c.save()
            context = {
            'customers': list(Customer.objects.all())
            }
            return render(request, 'customer/customer.html',context)
    else:
        context = {
        'customers': list(Customer.objects.all())
        }
        return render(request, 'customer/customer.html',context)