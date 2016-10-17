from django.shortcuts import render
from .models import TaichiMove
# Create your views here.
# def style13(request):
#     # if not request.user.is_authenticated:
#     #      return redirect('/')
#
#     # f04 机台吨位
#     # f07 f08 f09 f10 订单数量	已生产数量	未生产数量 	合计工时(小时）
#     # subtotal=Item012.objects.values('f03').annotate(sumf08=Sum('f08'),sumf09=Sum('f09'),sumf10=Sum('f10'),sumf11=Sum('f11'),sumf11v2=Sum('f11')/24)
#
#
#     item_list = TaichiMove.objects.order_by('taichiset', 'num')[:400]
#     # context = {'current_user':request.user,'page_title':'xxx','item_list': item_list,'subtotal':subtotal}
#     context = {'current_user':request.user,'page_title':'xxx','item_list': item_list}
#
#     #使用ITEM005  template
#     return render(request, 'itaiching/style19.html', context)

def style19(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = TaichiMove.objects.filter(stylenum=19).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'十九式','item_list': item_list}
    return render(request, 'itaiching/style19.html', context)

def route38(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = TaichiMove.objects.filter(stylenum=38).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'三十八式','item_list': item_list}
    return render(request, 'itaiching/route38.html', context)

def style19detail(request, setnum):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = TaichiMove.objects.filter(stylenum=19,setnum=setnum).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'十九式','item_list': item_list}
    return render(request, 'itaiching/style19detail.html', context)

def style19detail2(request, setnum, movenum):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = TaichiMove.objects.filter(stylenum=19,setnum=setnum,movenum=movenum).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'十九式','item_list': item_list}
    return render(request, 'itaiching/style19detail2.html', context)

def style13(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = TaichiMove.objects.filter(stylenum=13).order_by('setnum', 'movenum')[:3000]
    context = {'current_user':request.user,'page_title':'十三式','item_list': item_list}
    return render(request, 'itaiching/style13.html', context)
