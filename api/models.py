# from django.db import models
from tastypie.resources import ModelResource
from shop.models import Category, Course
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'cources'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['created_at', 'reviews_qty']
        authentication = CustomAuthentication()
        authorization = Authorization()

# post hydrate, change data to be incuded in post

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        bundle.obj.reviews_qty = bundle.data['reviews_qty']
        return bundle

# get dehydrate, all resonses from the server

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
