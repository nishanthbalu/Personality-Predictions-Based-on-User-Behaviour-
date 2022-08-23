"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_settings', views.admin_settings, name='admin_settings'),
    path('admin_settings_404', views.admin_settings_404, name='admin_settings_404'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),

    path('admin_category_master_add', views.admin_category_master_add, name='admin_category_master_add'),
    path('admin_category_master_view', views.admin_category_master_view, name='admin_category_master_view'),
    path('admin_category_master_delete', views.admin_category_master_delete, name='admin_category_master_delete'),

    path('admin_category_map_add', views.admin_category_map_add, name='admin_category_map_add'),
    path('admin_category_map_view', views.admin_category_map_view, name='admin_category_map_view'),
    path('admin_category_map_delete', views.admin_category_map_delete, name='admin_category_map_delete'),

    path('admin_label_master_add', views.admin_label_master_add, name='admin_label_master_add'),
    path('admin_label_master_view', views.admin_label_master_view, name='admin_label_master_view'),
    path('admin_label_master_delete', views.admin_label_master_delete, name='admin_label_master_delete'),

    path('admin_data_set_add', views.admin_data_set_add, name='admin_data_set_add'),
    path('admin_data_set_view', views.admin_data_set_view, name='admin_data_set_view'),
    path('admin_data_set_delete', views.admin_data_set_delete, name='admin_data_set_delete'),

    path('admin_user_details_view', views.admin_user_details_view, name='admin_user_details_view'),
    path('admin_user_posts_analyse', views.admin_user_posts_analyse, name='admin_user_posts_analyse'),

    path('admin_doctor_details_view', views.admin_doctor_details_view, name='admin_doctor_details_view'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_settings', views.user_settings, name='user_settings'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_posts_add', views.user_posts_add, name='user_posts_add'),
    path('user_posts_view', views.user_posts_view, name='user_posts_view'),
    path('user_posts_delete', views.user_posts_delete, name='user_posts_delete'),

    path('user_pic_add', views.user_pic_add, name='user_pic_add'),
    path('user_pic_view', views.user_pic_view, name='user_pic_view'),
    path('user_pic_delete', views.user_pic_delete, name='user_pic_delete'),

    path('user_question_add', views.user_question_add, name='user_question_add'),
    path('user_question_view', views.user_question_view, name='user_question_view'),
    path('user_question_delete', views.user_question_delete, name='user_question_delete'),

    path('doctor_login', views.doctor_login_check, name='doctor_login'),
    path('doctor_home', views.doctor_home, name='doctor_home'),
    path('doctor_details_add', views.doctor_details_add, name='doctor_details_add'),
    path('doctor_settings', views.doctor_settings, name='doctor_settings'),
    path('doctor_changepassword', views.doctor_changepassword, name='doctor_changepassword'),

    path('doctor_question_view', views.doctor_question_view, name='doctor_question_view'),
    path('doctor_reply_add', views.doctor_reply_add, name='doctor_reply_add'),
    path('doctor_reply_view', views.doctor_reply_view, name='doctor_reply_view'),

]
