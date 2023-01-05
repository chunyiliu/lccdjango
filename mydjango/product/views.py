from django.shortcuts import render

# Create your views here.

from .models import Goods

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def shop(request):
    
    goodsName=''
    sprice=''
    eprice=''
    
    if 'p' in request.GET:
        goodsName=request.GET['p']
        sprice=request.GET['priceS']
        eprice=request.GET['priceE']
        
        #只有產品名稱,但沒有價格範圍
        if (len(goodsName) >0 and len(sprice) ==0 and len(eprice)==0):
            allGoods=Goods.objects.filter(name__icontains=goodsName).order_by('-id')
        #沒有產品名稱,但有價格範圍
        elif (len(goodsName) ==0 and len(sprice) >0 and len(eprice)>0):
            allGoods=Goods.objects.filter(price__gte=sprice,price__lte=eprice).order_by('-id')
        #三個都有
        elif (len(goodsName) >0 and len(sprice) >0 and len(eprice)>0):
            allGoods=Goods.objects.filter(name__icontains=goodsName,price__gte=sprice,price__lte=eprice).order_by('-id')
            
        #三個都沒有    
        else:
            allGoods=Goods.objects.all().order_by('-id')
        
    else:
        #抓取全部的資料,並以id欄位做遞減排序
        allGoods=Goods.objects.all().order_by('-id')
    
    paginator=Paginator(allGoods,20)
    page=request.GET.get('page')
    try:
        allGoods=paginator.page(page)
    except PageNotAnInteger:
        allGoods=paginator.page(1)
    except EmptyPage:
        allGoods=paginator.page(paginator.num_pages)
    
    
    return render(request,'product.html',locals())