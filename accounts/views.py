from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm
# Create your views here.



def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    products=Product.objects.all()
    context={
        "customers":customers,'orders':orders,'products':products
    }
    
   
    return render(request,'accounts/dashboard.html',context)



def product(request):
    return render(request,'accounts/products.html')




def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()

    context={
        'customer':customer,'orders':orders
    }
    return render(request,'accounts/customer.html',context)



    

def createOrder(request):
    form=OrderForm()
   

    if (request.method=='POST'):
        form=OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context={
        'form':form
    }    
    return  render(request,'accounts/create_order.html',context) 

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if (request.method=='POST'):
        form=OrderForm(request.POST,instance=order)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'accounts/create_order.html',context)


def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)

    if(request.method=="POST"):
        order.delete()
        return redirect('/')
    context={
        'item':order
    }
    return render(request,'accounts/delete_order.html',context)