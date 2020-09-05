from django import forms
from .models import ContactContactA00, ContactContactA01, ContactContactA02, ContactContactA03,ContactContactA04,ContactGroupA00, ContactGroupA01


class ContactA00Form(forms.ModelForm):

    class Meta:
        model = ContactContactA00
        fields = ['first_name', 'middle_initial', 'last_name', 'email', 'address_1', 'barangay_district', 'city_municipality','postal_code','province','phone_1', 'phone_2']

class ContactA01Form(forms.ModelForm):
    class Meta:
        model = ContactContactA01
        fields = '__all__'

class ContactA02Form(forms.ModelForm):
    class Meta:
        model = ContactContactA02
        fields = '__all__'

class ContactA03Form(forms.ModelForm):
    class Meta:
        model = ContactContactA03
        fields = '__all__'

class ContactA04Form(forms.ModelForm):
    class Meta:
        model = ContactContactA04
        fields = '__all__'

class GroupA00Form(forms.ModelForm):
    class Meta:
        model = ContactGroupA00
        fields = '__all__'

class GroupA01Form(forms.ModelForm):
    class Meta:
        model = ContactGroupA01
        fields = '__all__'