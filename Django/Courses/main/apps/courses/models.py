from __future__ import unicode_literals

from django.db import models
from django import forms

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        


class Course(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.ForeignKey(User, related_name = "courses")
    comments = models.ManyToManyField(User, through="Comment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CourseForm(forms.ModelForm):

    desc = forms.CharField()
    class Meta:
        model = Course
        fields = ['name', 'instructor']

        def __str__(self):
            return "{} {}".format(self.first_name, self.last_name)

    def save(self, id=None, **kwargs):
        course = super(CourseForm, self).save()
        if id:
            description = Description.objects.get(course=id)
            description.desc = self.cleaned_data['desc']
            description.save()
        else:
            Description.objects.create(course=course, desc=self.cleaned_data['desc'])
        return course

class Description(models.Model):
    course = models.OneToOneField(Course, related_name="description")
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    comment = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



