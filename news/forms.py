from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm


from .models import Post

class PostForm(forms.ModelForm):
    required_css_class = 'my-custom-class'
    title = forms.CharField(max_length=40)

    class Meta:
        model = Post
        fields = ['author', 'content_type', 'posts', 'header', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control"})
        self.fields['header'].label = "Заголовок публикации"
        self.fields['header'].widget.attrs.update({'placeholder': "Введите название"})
        self.fields['header'].label = "Текст публикации"
        self.fields['header'].widget.attrs.update({'placeholder': "Введите текст здесь"})

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get("header")
        text = cleaned_data.get("text")

        if header == text:
            raise ValidationError(
                "Текст статьи не должен быть идентичен заголовку."
            )
        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user