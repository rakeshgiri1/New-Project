from django.shortcuts import render
def learn_django(request):
    return render(request, 'course/courseone.html', {'title':'Fees Django', 'cname':'Django'})
