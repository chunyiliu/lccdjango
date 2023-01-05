from django.shortcuts import render

# Create your views here.
from .models import News #將models.py中的class匯入

#分頁要用的函式庫
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def news(request):
    # 抓資料庫中的所有資料 objects => 資料
    # order_by 排序 依欄位名稱 id 來做排序
    # - 遞減 若沒有加 - 號時,則為遞增
    data = News.objects.all().order_by('-id')
    
    paginator=Paginator(data,25) #25筆為一頁
    page=request.GET.get('page') #要從網址上的參數抓取資料回來   
    try:
        pageData=paginator.page(page)
    except PageNotAnInteger:
        pageData=paginator.page(1) # 若參數不是整數時,則顯示第一頁資料
    except EmptyPage:
        pageData=paginator.page(paginator.num_pages)# num_pages 總頁數

    #先採用字典方式傳送至網頁
    content={"newslist":pageData}    
    
    # render(request,網頁名稱,參數內容)
    return render(request,'news.html',content)

def index(request):
    return render(request,'index.html')