from django.shortcuts import render

# Create your views here.

from .models import Message

def contact(request):
    
    if 'cuName' in request.POST:
        cuName=request.POST['cuName']
        email=request.POST['email']
        question=request.POST['question']
        content=request.POST['content']
        
        #將資料新增至資料表中
        obj=Message.objects.create(name=cuName,email=email,subject=question,content=content)
        obj.save()
        
    return render(request,'contact.html')