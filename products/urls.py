from django.conf.urls import url, include
from .views import all_products, product_detail, all_products2, product_review, add_review


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', all_products2, name='all_products2'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^product_review/(?P<id>\d+)', product_review, name='product_review'),
    url(r'^add_review/(?P<id>\d+)', add_review, name='add_review'),
]
