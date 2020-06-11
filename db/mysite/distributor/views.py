from django.shortcuts import render
from django.db import connection
from .models import Distributor,Sales
# Create your views here.
def distributor_view(request):
    if request.method == 'POST':
        query=request.POST.get('my_sql',None)
        search=request.POST.get('s_name',None)
        name=request.POST.get('name',None)
        margin=request.POST.get('margin',None)
        tel=request.POST.get('tel',None)
        email=request.POST.get('email',None)
        if(search!=None):
            try:
                distributor=Distributor.objects.get(name=search)
            except:
                distributor=None
            context = {
            's_distributor': distributor
            }
            return render(request, 'distributor/distributor.html',context)
        
        elif(query!=None):
            print('query',query)
            with connection.cursor() as cursor:
                cursor.execute(query)
                items=list(cursor.fetchall())
                context = {'items': items}
            return render(request, 'distributor/distributor.html',context)
        else:
            d=Distributor.objects.create(name=name,margin=margin,tell=tel,mail=email)
            d.save()
            context = {
            'distributors': list(Distributor.objects.all())
            }
            return render(request, 'distributor/distributor.html',context)
    else:
        context = {
        'distributors': list(Distributor.objects.all())
        }
        return render(request, 'distributor/distributor.html',context)


def d_detail_view(request,id,name):
    d_name=name
    dis_id=Distributor.objects.get(name=d_name).id
    context = {
        'distributor': d_name,
        'sales':list(Sales.objects.filter(seller=dis_id))
        }
    return render(request, 'distributor/dis_detail.html',context)