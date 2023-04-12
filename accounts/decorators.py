from django.shortcuts import redirect
from django.http import HttpResponse



def unAutehnticated(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:

             return view_func(request,*args,**kwargs)
    return wrapper_func 


def adminOnly(roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group=None
            
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                if group in roles:
                    return view_func(request,*args, **kwargs)
                    
                else:
                    return HttpResponse('You Are not authorized')
            else:
               return HttpResponse("Please check your group")
        return wrapper_func
    return decorator
    
    
  