from django import forms
from shop.models import Product

qty_s=Product.objects.get(id=7)
qty=qty_s.stock
PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,qty+1)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
