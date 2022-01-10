import logging
import math
from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse
from .models import  Product, Contact, Orders, OrderUpdate
from django.shortcuts import render

def index(request):
    products=Product.objects.all()
    # print(products)
    allProds=[]
    catprods=Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = (n + 3) // 4
        allProds.append([prod, range(1,nSlides), nSlides])

    params={'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    # product=Product.objects.all()
    # print(product.product_id)
    # logging.info('message')
    # logging.debug('message')
    # params={'products': product}
    return render(request,'shop/about.html')

def searchMatch(query,item):
    if len(query)<4: return False
    query=query.lower()
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query=request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category')
    print('The products are',catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = (n + 3) // 4
        if prod: allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds': allProds, "msg": ""}
    if not allProds or len(query)<4:
        params={'msg': "Please make sure to enter relevant search query"}
    return render(request,'shop/search.html',params)

def contact(request):
    if request.method=="POST":
        # print(request)
        name=request.POST.get('name','default')
        email=request.POST.get('email','default')
        phone=request.POST.get('phone','default')
        desc=request.POST.get('email','default')
        # print(name,email,phone,desc)
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
        print('for contact',thank)
        return render(request,'shop/contact.html',{'thank':thank})
    return render(request, 'shop/contact.html')

def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodView.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        print(request)
        items_json=request.POST.get('itemsJson','default')
        name=request.POST.get('name','default')
        amount=request.POST.get('amount','default')
        email=request.POST. get('email','default')
        address=request.POST.get('address1','default') + " "+ request.POST.get('address2', 'default')
        city=request.POST.get('city','default')
        state=request.POST.get('state','default')
        zip=request.POST.get('zip_code','default')
        phone=request.POST.get('phone','default')
        # print(name,email,phone,desc)
        order=Orders(items_json=items_json, name=name, email=email, address=address,city=city,zip_code=zip,\
                     state=state, phone=phone, amount=amount)
        order.save()

        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save() 
        print(update)
        thank=True
        id=order.order_id
        print(thank)
        return render(request,'shop/checkout.html',{'thank': thank, 'id': id })
    return render(request, 'shop/checkout.html')

def tracker(request):
    if request.method=='POST':
        order_id=request.POST.get('OrderID','')
        email=request.POST.get('email')
        print(order_id,email)
        try:
            order=Orders.objects.filter(order_id=order_id, email=email)
            if order:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                response=json.dumps({"status":"success","updates": updates, "itemsJson": order[0].items_json}, default=str)
                print('print of response',response)
                return HttpResponse(response)

            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request,'shop/tracker.html')