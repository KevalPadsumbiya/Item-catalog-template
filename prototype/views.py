from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html')

def pay(request):
	if request.method == "POST":
		urls = ["https://i.postimg.cc/PJ7b589G/Component-11-1-1-X.png",
		"https://i.postimg.cc/1RrZV3Yx/Component-3-1-1-X.png",
		"https://i.postimg.cc/L83RdkGb/Group-250-1-X.png",
		"https://i.postimg.cc/qqBX5qG6/Group-285-1-X.png",
		"https://i.postimg.cc/W3vTxW1C/Component-5-1-1-X.png",
		"https://i.postimg.cc/bYV4tVjP/Component-4-1-1-X.png",
		"https://i.postimg.cc/qMCDCkLc/Component-14-1-1-X.png",
		"https://i.postimg.cc/76K3RqGb/Group-273-1-X-1.png",
		"https://i.postimg.cc/XXSKT1JZ/Group-272-1-X.png",
		"https://i.postimg.cc/prxzCh18/Group-273-1-X.png",
		"https://i.postimg.cc/G2yMByZ1/Component-13-2-1-X-1.png",
		"https://i.postimg.cc/MHbXp95f/Component-10-2-1-X.png"]
		if request.POST['from'] == "cart_button":
			items_urls = [urls[int(i)-1] for i in request.POST['item_list1'].split(",")]
		else:
			if(request.POST['item_list'][0]=='0'):
				items_urls = "Your cart is empty!"
			else:
				items_urls = [urls[int(i)-1] for i in request.POST['item_list'].split(",")]
		a={'item':items_urls}
		return render(request,'pay.html',a)

def last(request):
	return render(request,'last.html')