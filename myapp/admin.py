from django.contrib import admin
from .models import user_login,user_post,data_set,label_master,user_details,category_master,user_pic,label_category_map
# Register your models here.
admin.site.register(user_login)
admin.site.register(user_post)
admin.site.register(data_set)
admin.site.register(label_master)
admin.site.register(user_details)
admin.site.register(category_master)
admin.site.register(user_pic)
admin.site.register(label_category_map)
