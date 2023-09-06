from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms

class News(models.Model):
    name = models.CharField(max_length = 255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)


    def update_rating(self):
        posts_rating = self.posts.aggregate(result=Sum('rating')).get('result')
        comments_rating = self.user.comments.aggregate(result=Sum('rating')).get('result')
        print(f"===== {self.user}: обновляем рейтинг автора =====")
        print(f"Рейтинг постов = {posts_rating}")
        print(f"Рейтинг комментов = {comments_rating}")
        self.rating = 3 * posts_rating + comments_rating
        self.save()
        print(f"Рейтинг = 3 * {posts_rating} + {comments_rating} = {self.rating}")

    def __str__(self):
        return f"{self.user}"

class Category(models.Model):
    category_type = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return f"{self.category_type}"

class CategorySubscriber(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

article = 'AR'
news = 'NE'

POSITIONS = [
    (article, 'Статья'),
    (news, 'Новость'),
]

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content_type = models.CharField(max_length = 2, choices = POSITIONS, default = article)
    date = models.DateTimeField(auto_now_add = True)
    posts = models.ManyToManyField(Category, through = 'PostCategory')
    header = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + "..."

    def get_absolute_url(self):
        """ Вернуть url, зарегистрированный для отображения одиночного товара """
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=700)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )