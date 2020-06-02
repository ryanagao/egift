from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            access_token=User.set_access_token(self),
            auth_key=User.set_auth_key(self),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves a new super user"""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    ROLE_1 = 1
    MERCHANT = 2
    ROLE_3 = 3
    APP_USER = 4

    ROLE_CHOICES = (
        (ROLE_1, 'Role 1'),
        (MERCHANT, 'Merchant'),
        (ROLE_3, 'Role 3'),
        (APP_USER, 'App User'),
    )

    ACTIVE = 1
    STATUS_2 = 2
    STATUS_3 = 3
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (STATUS_2, 'Status 2'),
        (STATUS_3, 'Status 3'),
    )

    USER_TYPE_6 = 6
    USER_TYPE_7 = 7
    USER_TYPE_8 = 8
    USER_TYPE_9 = 9
    USER_TYPE_CHOICES = (
        (USER_TYPE_6, 'User type 6'),
        (USER_TYPE_7, 'User type 7'),
        (USER_TYPE_8, 'User type 8'),
        (USER_TYPE_9, 'User type 9'),
    )

    role_id = models.IntegerField(choices=ROLE_CHOICES, default=APP_USER)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=256)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=USER_TYPE_6)
    access_token = models.CharField(max_length=256)
    auth_key = models.CharField(max_length=256)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        unique_together = (('email', 'access_token', 'auth_key'),)

    def __str__(self):
        return self.email

    def set_access_token(self):
        self.access_token = get_random_string(length=10)
        return self.access_token

    def set_auth_key(self):
        self.auth_key = get_random_string(length=10)
        return self.auth_key


class Profile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    description = models.TextField()
    tel_no = models.CharField(max_length=64)
    address = models.TextField()
    logo = models.ImageField(upload_to='uploads', blank=True)
    logo_banner = models.ImageField(upload_to='uploads', blank=True)
    allowed_egifts = models.IntegerField()
    nature_of_business = models.TextField()
    terms_and_condition = models.TextField()
    opening_hour = models.CharField(max_length=32)
    closing_hour = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class About(models.Model):
    logo = models.TextField()
    description = models.TextField()
    address = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    history = models.TextField()
    email = models.CharField(max_length=191)
    contact_no = models.CharField(max_length=191)
    facebook = models.CharField(max_length=191)
    twitter = models.CharField(max_length=191)
    instagram = models.CharField(max_length=191)
    yahoo = models.CharField(max_length=191)
    terms_and_condition = models.TextField()
    privacy_policy = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.email


class AccountRequest(models.Model):
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    telephone_no = models.CharField(max_length=20)
    description = models.TextField()
    address = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Branches(models.Model):
    merchant_id = models.IntegerField()
    name = models.CharField(max_length=191)
    description = models.TextField()
    latitude = models.CharField(max_length=32)
    longitude = models.CharField(max_length=32)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name


class EgiftFreebies(models.Model):
    user_id = models.IntegerField()
    egift_id = models.IntegerField()
    freebies_id = models.IntegerField()
    qty = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()


class EgiftTemplates(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()
    content = models.TextField()
    css = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class EgiftTransaction(models.Model):
    egift_id = models.IntegerField()
    transaction_id = models.IntegerField()
    quantity = models.IntegerField()
    orig_price = models.FloatField()
    sale_price = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class EgiftUsage(models.Model):
    egift_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class EgiftUser(models.Model):
    user_id = models.IntegerField()
    egift_id = models.IntegerField()
    orig_price = models.FloatField()
    sale_price = models.FloatField()
    to = models.IntegerField()
    status = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()


class Faq(models.Model):
    question = models.CharField(max_length=191)
    answer = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Follower(models.Model):
    merchant_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Freebies(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    category_id = models.IntegerField()
    supplier_id = models.IntegerField()
    unit_id = models.IntegerField()
    price = models.FloatField()
    qty = models.FloatField()
    image = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Group(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=256)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Icon(models.Model):
    name = models.CharField(max_length=191)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Measurement(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)


class Month(models.Model):
    name = models.CharField(max_length=20)


class NatureOfBusiness(models.Model):
    user_id = models.IntegerField()
    icon_id = models.IntegerField()
    name = models.CharField(max_length=128)
    image = models.TextField(blank=True, null=True)
    description = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Newspeed(models.Model):
    egift_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.TextField()
    link = models.CharField(max_length=128)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Order(models.Model):
    user_id = models.IntegerField()
    egift_id = models.IntegerField()
    quantity = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Personnel(models.Model):
    fullname = models.CharField(max_length=191)
    company_name = models.CharField(max_length=191)
    position = models.CharField(max_length=191)
    self_description = models.TextField()
    inspiring_message = models.TextField()
    logo = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PointManagement(models.Model):
    point = models.IntegerField()
    benchmark = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PriceVariety(models.Model):
    user_id = models.IntegerField()
    egift_id = models.IntegerField()
    orig_price = models.FloatField()
    sale_price = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Rating(models.Model):
    merchant_id = models.IntegerField()
    user_id = models.IntegerField()
    rate = models.IntegerField()
    message = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class ReferralPoint(models.Model):
    user_id = models.IntegerField()
    points = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Role(models.Model):
    name = models.CharField(max_length=191)
    access = models.TextField()
    actions = models.TextField()
    navigation = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Sales(models.Model):
    merchant_id = models.IntegerField()
    branch_id = models.IntegerField()
    transaction_id = models.IntegerField()
    amount = models.FloatField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Setting(models.Model):
    referral_point_referrer = models.IntegerField()
    referral_point_referred = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Supplier(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    address = models.TextField()
    contact_no = models.CharField(max_length=32)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Transaction(models.Model):
    transaction_no = models.CharField(max_length=128)
    user_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class UserFriend(models.Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class UserGroup(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class UserPoint(models.Model):
    user_id = models.IntegerField()
    points = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Wishlist(models.Model):
    user_id = models.IntegerField()
    egift_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Commentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)


class Comments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()


class Links(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)


class Options(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)


class Postmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)


class Posts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()


class SmushDirImages(models.Model):
    # id = models.AutoField(unique=True)
    path = models.TextField()
    path_hash = models.CharField(unique=True, max_length=32, blank=True, null=True)
    resize = models.CharField(max_length=55, blank=True, null=True)
    lossy = models.CharField(max_length=55, blank=True, null=True)
    error = models.CharField(max_length=55, blank=True, null=True)
    image_size = models.PositiveIntegerField(blank=True, null=True)
    orig_size = models.PositiveIntegerField(blank=True, null=True)
    file_time = models.PositiveIntegerField(blank=True, null=True)
    last_scan = models.DateTimeField()
    meta = models.TextField(blank=True, null=True)


class TermRelationships(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        unique_together = (('object_id', 'term_taxonomy_id'),)


class TermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        unique_together = (('term_id', 'taxonomy'),)


class Termmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)


class Terms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()


class Usermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)


class Users(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

 
class YoastSeoLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    post_id = models.BigIntegerField()
    target_post_id = models.BigIntegerField()
    type = models.CharField(max_length=8)


class YoastSeoMeta(models.Model):
    object_id = models.BigIntegerField(unique=True)
    internal_link_count = models.PositiveIntegerField(blank=True, null=True)
    incoming_link_count = models.PositiveIntegerField(blank=True, null=True)
