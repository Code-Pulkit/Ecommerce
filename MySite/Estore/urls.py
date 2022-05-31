from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from Estore import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MyPasswordChangeForm , MyPasswordResetForm , MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view() , name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='Estore/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/' , auth_views.PasswordChangeView.as_view(template_name='Estore/passwordchangedone.html') , name = 'passwordchangedone'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Estore/login.html', authentication_form=LoginForm), name='login'),
    path('logout' , auth_views.LogoutView.as_view(next_page = "login") , name = 'logout'),

    path('registration/', views.CustomerResigrationView.as_view(), name='customerregistration'),
   
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='Estore/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='Estore/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='Estore/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='Estore/password_reset_complete.html'), name="password_reset_complete"),
   
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

