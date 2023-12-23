from django.shortcuts import render
def fees_django(request):
    return render(request, 'fees/info.html', {'Name': 'Fees Course'})
