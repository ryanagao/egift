# from . import login_view, LogoutView, \
#     MerchantSignupView, MerchantSignupSuccessView, DashboardView, \
#     ProfileView, UpdateProfileView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('merchant-signup/', views.MerchantSignupView.as_view(), name='merchant_signup'),
    path('merchant-signup-success/', views.MerchantSignupSuccessView.as_view(), name='signup_success'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('user/update-profile/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('credential/', views.UpdateCredentialView.as_view(), name='credential'),
    path('user', views.UserIndexView.as_view(), name='user_index'),
    path('about/view/', views.AboutView.as_view(), name='about'),
    path('branches/', views.BranchesIndexView.as_view(), name='branches'),
    path('branches/create/', views.BranchesCreateView.as_view(), name='branches_create'),
    path('follower/', views.FollowerIndexView.as_view(), name='follower'),
    path('nature-of-business/', views.NatureOfBusinessView.as_view(), name='nature_of_business'),
    path('freebies/', views.FreebiesIndexView.as_view(), name='freebies'),
    path('freebies/create/', views.FreebiesCreateView.as_view(), name='freebies_create'),
    path('egift/statistics/', views.StatisticsView.as_view(), name='statistics'),
    path('wishlist/', views.WishlistsIndexView.as_view(), name='wishlists'),
    path('egift-usage/', views.UsageIndexView.as_view(), name='usage'),
    path('egift/for-approval/', views.ForApprovalView.as_view(), name='for_approval'),
    path('egift/', views.EgiftIndexView.as_view(), name='egift'),
    path('egift/create/', views.EgiftCreateView.as_view(), name='egift_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
