from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField

class PasswordMixin(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

class State(models.Model):
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state
    
    class Meta:
        verbose_name = "State"

class City(models.Model):
    city = models.CharField(max_length=30)
    state = models.ForeignKey('State', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.state}"
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

class Area(models.Model):
    area = models.CharField(max_length=30)
    pincode = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.area}, {self.city}, {self.city.state}"
    
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

class Employee(PasswordMixin, models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_no = PhoneNumberField(blank=True)
    dob = models.DateField()
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    area = models.CharField(max_length=30, null=True)
    prof_pic = models.ImageField(upload_to='media/photos')

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    
class Seller(PasswordMixin, models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=True)
    mobile_no = PhoneNumberField(blank=True)
    dob = models.DateField()
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    area = models.CharField(max_length=30, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    prof_pic = models.ImageField(upload_to='media/photos', null=False, default='')
    document = models.ImageField(upload_to='media/docs', null=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

class Buyer(PasswordMixin, models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_no = PhoneNumberField(blank=True)
    dob = models.DateField()
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    area = models.CharField(max_length=30, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    prof_pic = models.ImageField(upload_to='media/photos', null=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"
    
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Property(models.Model):
    title = models.CharField(max_length=70, null=True)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.BigIntegerField(null=True)
    desc = models.TextField(null=True)
    bedroom = models.IntegerField(null=True, default=0)
    hall = models.IntegerField(null=True, default=0)
    bathroom = models.IntegerField(null=True, default=0)
    kitchen = models.IntegerField(null=True, default=0)
    balcony = models.IntegerField(null=True, default=0)
    floor = models.IntegerField(null=True, default=0)
    total_floor = models.IntegerField(null=True, default=0)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)
    address = models.TextField()
    docs = models.ImageField(upload_to='media/docs', null=True)

    def __str__(self):
        return f"Property ID: {self.id}"
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

class PropertyImage(models.Model):
    property = models.ForeignKey('Property', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/property')

    def __str__(self):
        return f"Image for Property ID: {self.property_id}"
    
    class Meta:
        verbose_name = "PropertyImage"
        verbose_name_plural = "PropertyImages"

class Wishlist(models.Model):
    property_id = models.ForeignKey('Property', on_delete=models.CASCADE)
    buyer_id = models.ForeignKey('Buyer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"

class Verification(models.Model):
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    property_id = models.ForeignKey('Property', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    desc = models.TextField(null=True)
    verification_date = models.DateField(null=True)

    class Meta:
        verbose_name = "Verification"
        verbose_name_plural = "Verifications"

class Payment(models.Model):
    buyer_id = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    seller_id = models.ForeignKey('Seller', on_delete=models.CASCADE)
    pay_date = models.DateField(null=True)
    pay_amount = models.BigIntegerField(null=True)
    transaction_id = models.CharField(max_length=70, null=True)
    status = models.CharField(max_length=30, null=True)
    property_id = models.ForeignKey('Property', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

class Seller_Ac(models.Model):
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    acc_no = models.CharField(max_length=30, null=True, unique=True)
    ifsc_code = models.CharField(max_length=20, null=True)
    bank_name = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = "Seller_Ac"
        verbose_name_plural = "Seller_Acs"

class Feedback(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    desc = models.TextField(null=True)
    rate = models.IntegerField(null=True)
    date = models.DateField(null=True)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"