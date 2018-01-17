from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from server.notes.models import Note

User = get_user_model()


class NoteListTestCase(APITestCase):
    url = reverse('note:note-list')
    queryset = Note.objects.all()

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.initial_objects_count = Note.objects.count()
        self.client.force_authenticate(user=self.user)

    def test_note_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_create(self):
        data = {
            'title': 't',
            'body': '1',
            'user': self.user.id,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            self.initial_objects_count + 1, Note.objects.count(),
        )


class NoteDetailTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')
        data = {
            'title': 't',
            'body': '1',
            'user': self.user,
        }
        self.note = Note.objects.create(**data)
        self.url = reverse('note:note-detail', kwargs={
            'pk': self.note.id,
        })
        self.client.force_authenticate(user=self.user)

    def test_note_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_put(self):
        data = {
            'title': '123',
            'body': '123',
            'is_favourite': True,
        }
        response = self.client.put(self.url, data)
        note = Note.objects.get(pk=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for key in data.keys():
            self.assertEqual(response.data.get(key), getattr(note, key))

    def test_note_patch(self):
        data = {
            'title': 'vest',
        }
        response = self.client.patch(self.url, data)
        note = Note.objects.get(pk=self.note.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), note.title)

    def test_note_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        objects_count = Note.objects.filter(id=self.note.id).count()
        self.assertEqual(0, objects_count)

    def test_note_access(self):
        """
            Test private access to note
        """
        another_user = User.objects.create(username='test1')
        self.client.force_authenticate(user=another_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class NoteReadOnlyFieldsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')
        data = {
            'title': 't',
            'body': '1',
            'user': self.user,
        }
        self.note = Note.objects.create(**data)
        self.url = reverse('note:note-detail', kwargs={
            'pk': self.note.id,
        })
        self.client.force_authenticate(user=self.user)

    def test_uuid_field(self):
        data = {
            'uuid': 12356,
        }
        note = Note.objects.get(pk=self.note.id)
        self.client.patch(self.url, data)
        self.assertEqual(note.uuid, self.note.uuid)

    def test_user_field(self):
        data = {
            'user': 12356,
        }
        note = Note.objects.get(pk=self.note.id)
        self.client.patch(self.url, data)
        self.assertEqual(note.user, self.note.user)
