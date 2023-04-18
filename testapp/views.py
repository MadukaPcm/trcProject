from django.shortcuts import render

# Create your views here.
def TestView(request):
    
    context = {}
    return render(request, 'test/test.html', context)
