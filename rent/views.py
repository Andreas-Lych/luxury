import logging
from django.core.paginator import Paginator
from django.shortcuts import render

from rent.models import Product

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.order_by("-created_at")
    paginator = Paginator(products, 30)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(request, "index.html", {"products": products})


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_details.html", {"product": product})