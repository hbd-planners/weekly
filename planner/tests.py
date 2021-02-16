from django.test import TestCase
from .utils import get_current_week_range
from datetime import date


class TestHomePage(TestCase):
    def test_get_current_week_range1(self):
        res = get_current_week_range(day=date(2021, 2, 16))
        self.assertEqual(res, "Mon, 15-02-2021 - Sun, 21-02-2021")
    
    def test_get_current_week_range2(self):
        res = get_current_week_range(day=date(2021, 4, 1))
        self.assertEqual(res, "Mon, 29-03-2021 - Sun, 04-04-2021")
    
    def test_get_current_week_range3(self):
        res = get_current_week_range(day=date(2021, 5, 31))
        self.assertEqual(res, "Mon, 31-05-2021 - Sun, 06-06-2021")
    
    def test_get_current_week_range4(self):
        res = get_current_week_range(day=date(2021, 6, 6))
        self.assertEqual(res, "Mon, 31-05-2021 - Sun, 06-06-2021")
    
    def test_get_current_week_range5(self):
        res = get_current_week_range(day=date(2020, 12, 29))
        self.assertEqual(res, "Mon, 28-12-2020 - Sun, 03-01-2021")
