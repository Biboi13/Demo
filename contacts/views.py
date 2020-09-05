from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactA00Form, ContactA01Form, ContactA02Form, ContactA03Form, ContactA04Form, GroupA00Form, GroupA01Form
import requests
# Create your views here.
def contact(request):
    return render(request, 'contacts/contact.html')
def add_contact(request):
    form = ContactA00Form()
    
    if request.method == 'POST':
        form = ContactA00Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully created a contact!')
            return redirect('contact-contact')
            # first_name = form.cleaned_data.get('first_name')
            # middle_initial = form.cleaned_data.get('middle_initial')
            # last_name = form.cleaned_data.get('last_name')
            # address_1 = form.cleaned_data.get('address_1')
            # barangay_district = form.cleaned_data.get('barangay_district')
            # city_municipality = form.cleaned_data.get('city_municipality')
            # postal_code = form.cleaned_data.get('email')
            # province = form.cleaned_data.get('province')
            # phone_1 = form.cleaned_data.get('phone_1')
            # phone_2 = form.cleaned_data.get('phone_2')
            # email = form.cleaned_data.get('phone_2')
            
            # data = {
            #     "first_name": first_name,
            #     "middle_inital": middle_initial,
            #     "last_name": last_name,
            #     "address_1": address_1,
            #     "barangay_district": barangay_district,
            #     "city_municipality": city_municipality,
            #     "postal_code":postal_code,
            #     "province":province,
            #     "phone_1":phone_1,
            #     "phone_2":phone_2,
            #     "email":email
            # }
            # r = requests.post('https://contact-dot-heroic-climber-277222.df.r.appspot.com/api/contact/', json=data)

    else:
        form = ContactA00Form()
    context = {
        "form":form
    }
    return render(request, 'contacts/add_contact.html', context)

def add_skill(request):
    form = ContactA01Form()
    if request.method == 'POST':
        form = ContactA01Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully added a skill!')
            return redirect('contact-contact') 
    else:
        form = ContactA01Form()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_skill.html', context)

def add_endorsement(request):
    form = ContactA02Form()
    if request.method == 'POST':
        form = ContactA02Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully added a skill!')
            return redirect('contact-contact') 
    else:
        form = ContactA02Form()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_endorsement.html', context)

def add_sample_work(request):
    form = ContactA03Form()
    if request.method == 'POST':
        form = ContactA03Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully added a sample work!')
            return redirect('contact-contact') 
    else:
        form = ContactA03Form()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_sample_work.html', context)

def add_deductions(request):
    form = ContactA04Form()
    if request.method == 'POST':
        form = ContactA04Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully added a deduction!')
            return redirect('contact-contact') 
    else:
        form = ContactA04Form()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_deduction.html', context)


def group(request):
    context = {

    }
    return render(request, 'contacts/group.html', context)

def add_group(request):
    form = GroupA00Form()
    if request.method == 'POST':
        form = GroupA00Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully created a group!')
            return redirect('contact-group') 
    else:
        form = GroupA00Form()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_group.html', context)

def add_group_role(request):
    form = GroupA01Form()
    if request.method == 'POST':
        form = GroupA01Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully created a group!')
            return redirect('contact-group') 
    else:
        form = GroupA01Form()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_group_role.html', context)