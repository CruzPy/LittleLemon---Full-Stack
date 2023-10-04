from django.test import TestCase
from .models import Booking, Menu
from datetime import date

class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.booking = Booking.objects.create(
            first_name="John",
            reservation_date=date(2023, 10, 15),
            reservation_slot=2
        )

    def test_first_name_label(self):
        booking = Booking.objects.get(id=1)
        field_label = booking._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_reservation_date_label(self):
        booking = Booking.objects.get(id=1)
        field_label = booking._meta.get_field('reservation_date').verbose_name
        self.assertEqual(field_label, 'reservation date')

    def test_reservation_slot_label(self):
        booking = Booking.objects.get(id=1)
        field_label = booking._meta.get_field('reservation_slot').verbose_name
        self.assertEqual(field_label, 'reservation slot')

    def test_first_name_max_length(self):
        booking = Booking.objects.get(id=1)
        max_length = booking._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_first_name(self):
        booking = Booking.objects.get(id=1)
        expected_object_name = f"{booking.first_name}"
        self.assertEqual(expected_object_name, str(booking))

class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu_item = Menu.objects.create(
            name="Lemonade",
            price=2.99,
            menu_item_description="Refreshing lemonade made with fresh lemons."
        )

    def test_name_label(self):
        menu_item = Menu.objects.get(id=1)
        field_label = menu_item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_price_label(self):
        menu_item = Menu.objects.get(id=1)
        field_label = menu_item._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_menu_item_description_label(self):
        menu_item = Menu.objects.get(id=1)
        field_label = menu_item._meta.get_field('menu_item_description').verbose_name
        self.assertEqual(field_label, 'menu item description')

    def test_price_not_null(self):
        menu_item = Menu.objects.get(id=1)
        null = menu_item._meta.get_field('price').null
        self.assertFalse(null)

    def test_name_max_length(self):
        menu_item = Menu.objects.get(id=1)
        max_length = menu_item._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name(self):
        menu_item = Menu.objects.get(id=1)
        expected_object_name = f"{menu_item.name}"
        self.assertEqual(expected_object_name, str(menu_item))
