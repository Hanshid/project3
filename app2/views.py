from django.shortcuts import render


# Create your views here.
def testfun(request):
    return render(request,'form.html')
