from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm,CreateUserForm
from .filters import OrderFilter
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=CreateUserForm()

    if(request.method=='POST'):
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

        
            

    context={
        'form':form
    }
    return render(request,'accounts/register_user.html',context)




def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
       
        if user is not None:
            
            login(request,user)
            return redirect('home')
        else:
            print("2")
            render("login")
        
    return render(request,'accounts/login_user.html')
def logoutUser(request):
    logout(request)
    return render(request,'accounts/login_user.html')





@login_required(login_url='login')
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    products=Product.objects.all()
    context={
        "customers":customers,'orders':orders,'products':products
    }
    
   
    return render(request,'accounts/dashboard.html',context)


@login_required(login_url='login')
def product(request):
    return render(request,'accounts/products.html')



@login_required(login_url='login')
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_filter=OrderFilter(request.GET,queryset=orders)
    orders=order_filter.qs
    context={
        'customer':customer,'orders':orders,'order_filter':order_filter
    }
    return render(request,'accounts/customer.html',context)



@login_required(login_url='login') 
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



@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)

    if(request.method=="POST"):
        order.delete()
        return redirect('/')
    context={
        'item':order
    }
    return render(request,'accounts/delete_order.html',context)