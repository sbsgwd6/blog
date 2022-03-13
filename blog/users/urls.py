#进行users 子应用的视图路由

from django.urls import path
from users.views import RegisterView,ImageCodeView
from users.views import SmsCodeView
urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/',RegisterView.as_view(),name='register'),

    #图片验证码路由
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),
    #短信发送
    path('smscode/', SmsCodeView.as_view(), name='smscode'),
]