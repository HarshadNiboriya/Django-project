from django.shortcuts import render

def welcome(request):
    return render(request,'welcome.html')

def sign_up(request):
    # print(request.GET.get('firstName'))
    # print(request.GET.get('lastName'))
    # print(request.GET.get('loginID'))
    # print(request.GET.get('Password'))
    # print(request.GET.get('Address'))
    # print(request.GET.get('DOB'))

    print(request.POST.get('firstName'))
    print(request.POST.get('lastName'))
    print(request.POST.get('loginID'))
    print(request.POST.get('Password'))
    print(request.POST.get('Address'))
    print(request.POST.get('DOB'))

    return  render(request, 'registration.html')

def sign_in(request):
    print(request.POST.get('loginID'))
    print(request.POST.get('Password'))

    return  render(request, 'login.html')