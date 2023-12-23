from django.shortcuts import render
def learn_django(request):
    return render(request, 'course/info.html', {'Name': 'Django Course'})
