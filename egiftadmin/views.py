from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.views.generic import View

from . import models, forms, params


class IndexView(View):
    def get(self, request):
        return redirect('login')


class LoginView(View):
    """View for login"""

    form_class = forms.LoginForm
    template_name = "egiftadmin/site/login.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            form = self.form_class(request.POST or None)
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
        return redirect('dashboard')

    def post(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('dashboard')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

class LogoutView(View):
    """Logout view"""

    def get(self, request):
        logout(request)
        return redirect('login')


class DashboardView(LoginRequiredMixin, View):
    """View for dashboard"""

    template_name = "egiftadmin/dashboard/index.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            'user': user,
        }
        return render(request, self.template_name, context)


class MerchantSignupView(View):
    """View for merchant signup"""

    form_class = merchant = forms.MerchantSignupForm
    template_name = "egiftadmin/site/merchant-signup.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            merchant = self.form_class(request.POST or None)
            context = {
                'merchant': merchant,
            }
            return render(request, self.template_name, context)
        return redirect('dashboard')

    def post(self, request, *args, **kwargs):
        merchant = forms.MerchantSignupForm(request.POST or None)

        if merchant.is_valid():
            user = models.User
            create_user = user(
                role_id         = user.APP_USER,
                email           = merchant.cleaned_data['email'],
                user_type       = user.USER_TYPE_8,
                username        = merchant.cleaned_data['company_name'],
                status          = user.ACTIVE,
                access_token    = get_random_string(length=10),
                auth_key        = get_random_string(length=10)
            )
            create_user.set_password('test')
            create_user.save()

            user = models.User.objects.filter(email=merchant.cleaned_data['email'])
            if user.exists():
                profile = models.Profile(
                    user                = user.get(),
                    name                = merchant.cleaned_data['company_name'],
                    description         = merchant.cleaned_data['description'],
                    tel_no              = merchant.cleaned_data['contact_no'],
                    address             = merchant.cleaned_data['address'],
                    allowed_egifts      = 100, #params

                    first_name          = 'test',
                    last_name           = 'test',
                    nature_of_business  = 'test',
                    terms_and_condition = 'test',
                    opening_hour        = 'test',
                    closing_hour        = 'test',

                    logo_banner         = params.default_logo, #params
                    logo                = params.default_logo #params
                )
                profile.save()

                profile = models.Profile.objects.filter(user_id=user.get().pk)
                if profile.exists():
                    pass #send email
                    return redirect('signup_success')
                else:
                    user.delete()

        context = {
            'merchant': merchant,
        }
        return render(request, self.template_name, context)


class MerchantSignupSuccessView(View):
    """View for merchant signup success"""

    template_name = "egiftadmin/site/merchant-signup-success.html"

    def get(self, request):
        return render(request, self.template_name, {})


class ProfileView(LoginRequiredMixin, View):
    """View for profile"""
    
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(user.profile.all(), user_id=user.pk)
        context = {
            'user': user,
            'profile': profile
        }
        return render(request, "egiftadmin/user/profile.html", context)


class UpdateProfileView(LoginRequiredMixin, View):
    """View for update profile"""

    form_class = forms.ProfileForm
    template_name = "egiftadmin/user/update-profile.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(user.profile.all(), user_id=user.pk)
        form = self.form_class(initial = {"email": user.email}, instance=profile, request=request)
        context = {
            'form': form,
            'profile': profile,
            'user': user
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None, request.FILES or None, request=request)
        if form.is_valid():
            user = request.user
            profile = get_object_or_404(user.profile.all(), user_id=user.pk)

            profile.name                = form.cleaned_data.get('name')
            profile.description         = form.cleaned_data.get('description')
            profile.tel_no              = form.cleaned_data.get('tel_no')
            profile.address             = form.cleaned_data.get('address')
            profile.terms_and_condition = form.cleaned_data.get('terms_and_condition')
            logo                        = form.cleaned_data.get('logo')
            logo_banner                 = form.cleaned_data.get('logo_banner')
            if logo is not None:
                profile.logo                = logo
            if logo_banner is not None:
                profile.logo_banner         = logo_banner
            profile.save()

            user.email = form.cleaned_data.get('email')
            user.save()

            return redirect('profile')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class UpdateCredentialView(LoginRequiredMixin, View):
    """View for update credential"""

    form_class = forms.CredentialForm
    template_name = "egiftadmin/user/credential.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        initial = {
            'username': user.username,
            'email': user.email
        }
        form = self.form_class(initial=initial, request=request)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST or None, request=request)
        if form.is_valid():

            user.email          = form.cleaned_data.get('email')
            user.username       = form.cleaned_data.get('username')
            user.access_token   = user.set_access_token()
            user.auth_key       = user.set_auth_key()
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)
            login(request, user)

            return redirect('profile')
        context = {
            'form': form,
            'user': user
        }
        return render(request, self.template_name, context)


class AboutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/about/view.html")


class UserIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/user/index.html")


class BranchesIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/branches/index.html")


class BranchesCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/branches/create.html")


class FollowerIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/follower/index.html")


class NatureOfBusinessView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/nature-of-business/index.html")


class FreebiesIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/freebies/index.html")


class FreebiesCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/freebies/create.html")


class StatisticsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/egift/statistics.html")


class WishlistsIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/wishlist/index.html")


class UsageIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/egift-usage/index.html")


class ForApprovalView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/egift/for-approval.html")
        

class EgiftIndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/egift/index.html")


class EgiftCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "egiftadmin/egift/create.html")