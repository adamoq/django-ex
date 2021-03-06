"""cookster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from . import settings
from django.conf import settings
from django.conf.urls.static import static
from cook.views import main, products, administration, employers, menu, orders, login_user, dish, orders_waiter, login_mobile
from cook.views import changepassword,resetpassword,changephone, changeproduct, login_mobile_status, menu_chart, checknotif
from cook.views import orders_cook, cookorders_chart, waiterorders_chart, products_chart, employers_chart, changeimg
from cook.charts import category_chart_json,category_chart_json2, dish_chart_json,category_chart_json1, cookorders_chart_json, cookorders_chart_json2, cookorders_chart_json3, cookorders_chart_json4
from cook.charts import waiterorders_chart_json, waiterorders_chart_json2, waiterorders_chart_json3, waiterorders_chart_json4, products_chart_json, products_chart_json2
from cook.charts import employers_chart_json
from cook.pdfs import Pdf, render_pdf_view
from django.contrib import admin
from cook.api import ProductResource, EmployeeResource, DishResource, CategoryResource, OrderResource, OrderCookResource, CookTaskResource, DishPriceResource, LanguageResource, DishProductResource, RestaurantDetailResource
from cook.api import ProductranslationResource, DishTranslationResource, CategoryTranslationResource, WaiterOrderDetailsResource, WaiterCookResource, OrderResourceGet,OrderResourceGet1,OrderResourceGet2, CurrencyResource, ReservationResourceGet
from django.contrib.auth import views as auth_views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, {'template_name': 'login.html','redirect_authenticated_user': True}),
	url(r'^accounts/profile/$', products),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}),
	url(r'^products/$', products, name = 'products'),
	url(r'^administration/$', administration, name = 'administration'),
	url(r'^employers/$', employers, name = 'employers'),
	url(r'^menu/$', menu, name = 'menu'),
	url(r'^orders-waiter/$', orders_waiter),
	url(r'^orders/$', orders, name = 'orders'),
	url(r'^orders-cook/$', orders_cook, name = 'orderscook'),
	url(r'^dish/$', dish),
	#pdf
	url(r'^render_pdf_view/$', render_pdf_view),
	
	url(r'^pdf/product/$', Pdf.as_view()),
	#api
	url(r'^api/', include(ProductResource().urls)),
	url(r'^api/', include(EmployeeResource().urls)),
	url(r'^api/', include(DishResource().urls)),
	url(r'^api/', include(CategoryResource().urls)),
	url(r'^api/', include(OrderResource().urls)),
	url(r'^api/', include(OrderCookResource().urls)),
	url(r'^api/', include(CookTaskResource().urls)),
	url(r'^api/', include(WaiterOrderDetailsResource().urls)),
	url(r'^api/', include(WaiterCookResource().urls)),
	url(r'^api/', include(OrderResourceGet().urls)),
	url(r'^api/', include(OrderResourceGet1().urls)),
	url(r'^api/', include(DishTranslationResource().urls)),
	url(r'^api/', include(ProductranslationResource().urls)),
	url(r'^api/', include(CategoryTranslationResource().urls)),
	url(r'^api/', include(DishPriceResource().urls)),
	url(r'^api/', include(LanguageResource().urls)),
	url(r'^api/', include(ReservationResourceGet().urls)),
	url(r'^api/', include(RestaurantDetailResource().urls)),

	url(r'^api/', include(OrderResourceGet2().urls)),
	url(r'^api/', include(CurrencyResource().urls)),
	url(r'^api/', include(DishProductResource().urls)),
# mobile interaction
	url(r'^mobileapi/$', login_mobile),
	url(r'^mobileapistatus/$', login_mobile_status),
	url(r'^mobilereset/password/$', changepassword),
	url(r'^reset/password/$', resetpassword),
	url(r'^mobilereset/phone/$', changephone),
	url(r'^mobilereset/product/$', changeproduct),
	url(r'^mobileapi/img/$', changeimg),
	url(r'^mobileapi/notif/$', checknotif),

#raporty - menu
	url(r'^menu/raport/$', menu_chart, name='menu_chart'),
	url(r'^products/raport-json/$', dish_chart_json, name='dish_chart_json'),
	url(r'^category/raport-json/$', category_chart_json, name='category_chart_json'),
	url(r'^category/raport-json1/$', category_chart_json1, name='category_chart_json1'),
	url(r'^category/raport-json2/$', category_chart_json2, name='category_chart_json2'),
#raporty - zamówienia kucharzy
	url(r'^orders-cook/raport/$', cookorders_chart, name='cookorders_chart'),
	url(r'^orders-cook/raport-json/$', cookorders_chart_json, name='cookorders_chart_json'),
	url(r'^orders-cook2/raport-json/$', cookorders_chart_json2, name='cookorders_chart_json2'),
	url(r'^orders-cook3/raport-json/$', cookorders_chart_json3, name='cookorders_chart_json3'),
	url(r'^orders-cook4/raport-json/$', cookorders_chart_json4, name='cookorders_chart_json4'),

#raporty - zamówienia kelnerów
	url(r'^orders-waiter/raport/$', waiterorders_chart, name='waiterorders_chart'),
	url(r'^orders-waiter/raport-json/$', waiterorders_chart_json, name='waiterorders_chart_json'),
	url(r'^orders-waiter2/raport-json/$', waiterorders_chart_json2, name='waiterorders_chart_json2'),
	url(r'^orders-waiter3/raport-json/$', waiterorders_chart_json3, name='waiterorders_chart_json3'),
	url(r'^orders-waiter4/raport-json/$', waiterorders_chart_json4, name='waiterorders_chart_json4'),
#raporty - produkty
	url(r'^products/raport/$', products_chart, name='products_chart'),
	url(r'^products1/raport-json/$', products_chart_json, name='products_chart_json'),
	url(r'^products2/raport-json/$', products_chart_json2, name='products_chart_json2'),
#raporty - pracownicy
	url(r'^employers/raport/$', employers_chart, name='employers_chart'),
	url(r'^employers/raport-json/$', employers_chart_json, name='employers_chart_json'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]