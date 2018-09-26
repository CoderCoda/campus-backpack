from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.core.validators import RegexValidator

from django.views import generic
from django.views.generic import View
from django.views.generic.edit import DeleteView

from django import forms
from django.contrib.auth.models import User
from .models import Course, Textbook

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer


class IndexView(generic.ListView):
    template_name = 'exchange/index.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all()


def about(request):
    return render(request, 'exchange/about.html')


class ListingsView(generic.DetailView):
    model = Course
    template_name = 'exchange/course_listings.html'


class DetailView(generic.DetailView):
    model = Textbook
    template_name = 'exchange/book_details.html'


class TextbookForm(forms.ModelForm):
    ISBN = forms.CharField(required=False, label='ISBN', validators=[RegexValidator(r'^\d{13}$', 'ISBN must be 13 digits')])
    notes = forms.CharField(required=False)
    author = forms.CharField(label='Author(s)')

    class Meta:
        model = Textbook
        exclude = ('seller', )


class TextbookCreateInd(View):
    form_class = TextbookForm
    template_name = 'exchange/textbook_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        seller = request.user

        if form.is_valid():
            textbook = form.save(commit=False)
            textbook.seller = seller
            textbook.save()
            return redirect('exchange:course_listings', pk=textbook.course.id)

        return render(request, self.template_name, {'form': form})


class TextbookUpdate(View):
    form_class = TextbookForm
    template_name = 'exchange/textbook_form.html'

    def get(self, request, book_id):
        instance = get_object_or_404(Textbook, pk=book_id)
        form = self.form_class(instance=instance)
        return render(request, 'exchange/textbook_form.html', {'form': form})

    def post(self, request, book_id):
        instance = get_object_or_404(Textbook, pk=book_id)
        form = self.form_class(request.POST, instance=instance)
        seller = request.user

        if form.is_valid():
            textbook = form.save(commit=False)
            textbook.seller = seller
            textbook.save()
            return redirect('exchange:my_profile', pk=seller.id)
            # redirect to MyProfile

        return render(request, self.template_name, {'form': form})


class TextbookDelete(DeleteView):
    model = Textbook

    def get_success_url(self):
        return reverse('exchange:my_profile', kwargs={'pk': self.request.user.id})
    # once MyListings is implemented, redirect there instead


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserFormView(View):
    form_class = UserForm
    template_name = 'exchange/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # authentication
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('exchange:index')

        return render(request, self.template_name, {'form': form})


class UserView(generic.DetailView):
    model = User
    template_name = 'exchange/my_profile.html'


class BookList(APIView):

    def get(self, request):
        listings = Textbook.objects.all()
        serializer = BookSerializer(listings, many=True)
        return Response(serializer.data)