from django.urls import reverse
from rest_framework import status

from server.notes.models import Category
from server.users.tests.base import BaseTestCase


class CategoryListTestCase(BaseTestCase):
    url = reverse('note:category-list')
    queryset = Category.objects.all()

    def setUp(self):
        super(CategoryListTestCase, self).setUp()
        self.initial_objects_count = Category.objects.count()

    def test_category_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.count, self.queryset.count())

    def test_category_create(self):
        data = {
            'name': 't',
            'description': '1',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            self.initial_objects_count + 1, Category.objects.count(),
        )


class CategoryDetailTestCase(BaseTestCase):

    def setUp(self):
        super(CategoryDetailTestCase, self).setUp()
        category_object_data = {
            'name': 'test',
            'description': 'test',
        }
        self.test_object = Category.objects.create(**category_object_data)
        self.url = reverse('note:category-detail', kwargs={
            'pk': self.test_object.id,
        })

    def test_category_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_put(self):
        data = {
            'name': '123',
            'description': '123',
        }
        response = self.client.put(self.url, data)
        category = Category.objects.get(pk=self.test_object.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for key in data.keys():
            self.assertEqual(response.get(key), getattr(category, key))

    def test_category_patch(self):
        data = {
            'name': 'vest',
        }
        response = self.client.patch(self.url, data)
        category = Category.objects.get(pk=self.test_object.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), category.name)

    def test_category_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        objects_count = Category.objects.filter(id=self.test_object.id).count()
        self.assertEqual(0, objects_count)
