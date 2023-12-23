from django.shortcuts import render

def fees_django(request):
    return render(request, 'fees/feesone.html', {'title':'Fees Django', 'cname':'Django','charge':'5000'})

