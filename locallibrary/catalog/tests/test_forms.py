from django.test import TestCase
from django.utils import timezone
from catalog.forms import RenewBookForm
import datetime


class RenewBookFormTest(TestCase):

    def test_renew_form_date_filed_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label == None or form.fileds['renewal_date'].label == 'renewal date')

    def test_renew_from_date_field_help_text(self):
        form = RenewBookForm()

        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks')

    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_today(self):
        date = datetime.date.today()
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = timezone.now() + datetime.timedelta(weeks=4)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())