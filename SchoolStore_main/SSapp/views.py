from django.shortcuts import render,redirect,get_object_or_404
from .forms import SForm
from .models import Courses,Review
from django.contrib import messages
from ProductApp.models import Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request):
    return render(request,"home1.html")
def Allproduct(request):
    products = Product.objects.all()

        # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(name__icontains=item_name)

        # pagination code

        # paginator = Paginator(products, 8)
        # page = request.GET.get('page')
        # products = paginator.get_page(page)

        # or

    paginator = Paginator(products, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "home.html", {'products': products})


def Student(request):
    form = SForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        form = SForm(request.POST)
        if form.is_valid():
            form.save();
            messages.info(request,"Your Order Confirmed")
            return redirect('SSapp:student')

    return render(request,"student.html",{'form':form})
# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id=department_id).all()
    return render(request, 'course_list.html', {'courses': courses })
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def Newpage(request):
    return render(request,"buttonpage.html")

def prodetail(request,id):

    try:
        product=Product.objects.get(id=id)
    except Exception as e:
        raise e

    return render(request,'product.html',{'product':product})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def BookRent(request):
    if request.method == 'POST':
        messages.info(request,"Order Confirmed,You Have Rented This Book")
        return redirect('SSapp:bookrent')

    return render(request,"bookrent.html",)
def reviews(request):
    reviews = Review.objects.all()
    return render(request,"Reviews.html",{'reviews':reviews})
def add_reviews(request):
    if request.method == 'POST':
        name = request.POST['username']
        review = request.POST['review']
        if review != name:
            messages.info(request, "Please Add A Review")
            return redirect('SSapp:add_reviews')
        else:
            comment = Review.objects.create(name=name, review=review)
            comment.save()
            messages.info(request, "Added Your Review....Thanks For The Feedback ")
            return redirect('SSapp:add_reviews')
    return render(request,"Add_Review.html")


