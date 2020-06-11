from django.shortcuts import render
from .forms import CommodityForm
from .models import Commodity
from customer.models import Customer
from distributor.models import Distributor,Sales
from django.db import connection
# Create your views here.
def test(request):
    # 表示會載入 templates/shop/index.html
    return render(request, 'shop/index.html')
def commodity_sql_view(request):
    if request.method == 'POST':
        try:
            query=request.POST['my_sql']
        except:
            query=None
        print('query',query)
        if("UPDATE" in query):
            with connection.cursor() as cursor:
                 cursor.execute(query)

        else:
            items=list( Commodity.objects.raw(query))
            context = {
            'items': items
            }
        return render(request, 'shop/commodity_sql_search.html', context)
    else:
        return render(request, 'shop/commodity_sql_search.html')
def commodity_create_view(request):
    form = CommodityForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'shop/commodity_create.html', context)

def shop_view(request):
    context = {
        'products': list(Commodity.objects.all())
    }
    return render(request, 'shop/shop.html', context)
    # 現在還沒有資料要從 model 傳給頁面
  # 所以 context 留空
def about_view(request):
    return render(request, 'shop/about.html')
def order_view(request):
    if request.method == 'POST':
        customers=[c.name for c in list(Customer.objects.all())]
        distributors=[d.name for d in list(Distributor.objects.all())]
        cname=request.POST.get('cname',None)
        dname=request.POST.get('dname',None)
        print(cname,dname)
        print(customers,distributors)
        for p in list(Commodity.objects.all()):
            quantity=int(request.POST.get(p.name))
            if quantity>0:
                print(quantity)
                if cname in  customers and dname in distributors:
                    print('hi')
                    price=Commodity.objects.get(name=p.name).price
                    seller=Distributor.objects.get(name=dname)
                    commodity=Commodity.objects.get(name=p.name)
                    customer=Customer.objects.get(name=cname)
                    s=Sales.objects.create(seller=seller,commodity=commodity,profit=price*quantity,customer=customer)
                    s.save()
        context = {
            'products': list(Commodity.objects.all())
        }
        return render(request, 'shop/order.html', context)

    else:
        context = {
            'products': list(Commodity.objects.all())
        }
        return render(request, 'shop/order.html', context)