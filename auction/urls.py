from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # 회원가입/로그인/인증
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('join/', views.CreateUserView.as_view(), name='join'),
    path('join-done/', views.CreateUserView.as_view(), name='join_done'),

    path('auction/create/', login_required(views.create_auction_view)),
    path('auction/modify/<int:auction_id>/', login_required(views.modify_auction_view)),
    path('auction/detail/<int:auction_id>/', login_required(views.auction_detail_view)),

    path('admin/auction/', login_required(views.auction_admin_view)),
    path('admin/auction/update-state/<int:auction_id>/<state>', login_required(views.update_auction_state)),

    path('api/auction/create/', views.create_auction),
    path('api/auction/modify/', views.modify_auction),
]
