from django.shortcuts import render
from django.http import HttpResponse
from appTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html')


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR form invalid")

    return render(request, 'appTwo/users.html', {'form':form})







    users_list = User.objects.order_by('last_name')
    ren_dict = {'all_users':users_list}

    #my_mark = {'mark_m1':'HELP ME'}
    # return render(request, 'appTwo/index.html', context= my_mark)
    return render(request, 'appTwo/users.html', context = ren_dict)
