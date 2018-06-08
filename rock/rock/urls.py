from django.conf.urls import url
from rock import views
urlpatterns = [
    url(r'^home/', views.Home,name='home'),
    url(r'^home_logined/', views.Home_logined, name='home_logined'),
    url(r'^home_logined_collected/', views.Home_logined_collected, name='home_logined_collected'),
    url(r'^login/', views.Login, name='login'),
    url(r'^register/', views.Register, name='register'),
    url(r'^userinfo_mod/', views.Userinfo_mod, name='userinfo_mod'),
    url(r'^collected/',views.Collected,name="collected"),
    url(r'^delcollected/', views.delCollected, name="delcollected"),
]
