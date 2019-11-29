from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from django.conf import settings
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User
from .models import Product
from posts.models import Post
from django.utils import timezone

import datetime


def all_products(request):
    products = Product.objects.all()
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "products.html", {"products": products, 'posts': posts})


def all_products2(request):
    products = Product.objects.all()
    return render(request, "allproducts.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(Product=product)
    return render(request, "productdetail.html", {'product': product, 'reviews': reviews})


def get_posts2(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "products.html", {'posts': posts})


def product_review(request, id):
    products = get_object_or_404(Product, pk=id)
    reviews = Review.objects.filter(product=id).order_by('-pub_date')[:5]
    return render(request, "productdetail.html", {'reviews': reviews, "product": product})


def add_review(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.Product = product
            review.user_name = request.user
            form.save()
        return redirect('all_products2')
    else:
        form = ReviewForm()
        return render(request, "create_review.html", {'form': form})
