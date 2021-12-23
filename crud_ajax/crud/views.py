from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .forms import user_register





def home(request):
    form = user_register
    user = User.objects.all()
    return render(request,'home.html',{'form':form , 'user':user})


# the logic behinde of data save and show without refresh
def save_data(request):
    if request.method == 'POST':
        form = user_register(request.POST)
        if form.is_valid():
            uid = request.POST.get('userid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if(uid == ''):
                usr = User(name = name, email= email, password = password)
            else:
                usr = User( id = uid ,name = name, email= email, password = password)
                
            usr.save()
            us = User.objects.values()
            # print(us)
            user_data = list(us)
            return JsonResponse({'status':'save','user':user_data})
        else:
            return JsonResponse({"status":0})    

# this is for delete the user data
def delete_data(request):
    if request.method =='POST':
        id = request.POST.get('sid')
        # print(id)
        pi = User.objects.get(pk = id)
        pi.delete()
        return JsonResponse({'status' :1})
    else:
        return JsonResponse({'status' :0})


# this is for edit the user data 
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        user = User.objects.get( pk = id)
        user_data = {'id': user.id, 'name':user.name,'email':user.email,'password':user.password}
        return JsonResponse(user_data)


            
    