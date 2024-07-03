from django import forms
from app.models import Product, Comment, Order



class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'image', 'rating', 'discount']
        exclude = ()

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'message']

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ()
