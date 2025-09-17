from django.urls import path
from inoviteapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('careers/internship', views.internship),
    path('careers/jobs/tech', views.tech),
    path('careers/jobs/nontech', views.nontech),
    path('about-us', views.aboutus),
    path('contact', views.contact),
    path('blog', views.blog),
    # path('register',views.register),
    # path('login',views.user_login),
    # path('logout',views.user_logout),
    # path('book',views.book),

    # path('html',views.html),
    # path('css',views.css),
    # path('bootstrap',views.bootstrap),
    # path('javascript',views.javascript),
    # path('python',views.python),

    # path('que',views.que),
    # path('notes',views.notes),
    # path('search',views.search),
    # path('productdetail/<pid>',views.productdetail),
    # path('addtocart/<pid>',views.addtocart),
    # path('viewcart',views.viewcart),
    # path('updateqty/<x>/<cid>',views.updateqty),
    # path('remove/<cid>',views.remove),
    # path('placeorder',views.placeorder),
    # path('fetchorder',views.fetchorder),
    # path('makepayment',views.makepayment),
    # path('paymentsuccess',views.paymentsuccess),

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
