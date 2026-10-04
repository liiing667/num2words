# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from unittest import TestCase

from num2words import CONVERTES_TYPES, num2words


class DurationTest(TestCase):
    def test_type_is_registered(self):
        self.assertIn('duration', CONVERTES_TYPES)

    def test_english(self):
        self.assertEqual(num2words(0, to='duration'), 'zero seconds')
        self.assertEqual(num2words(1, to='duration'), 'one second')
        self.assertEqual(num2words(2, to='duration'), 'two seconds')
        self.assertEqual(num2words(60, to='duration'), 'one minute')
        self.assertEqual(num2words(120, to='duration'), 'two minutes')
        self.assertEqual(num2words(3661, to='duration'),
                         'one hour, one minute and one second')
        self.assertEqual(num2words(5400, to='duration'),
                         'one hour and thirty minutes')

    def test_zero_segments_are_skipped(self):
        self.assertEqual(num2words(31536000 + 86400 + 5, to='duration'),
                         'one year, one day and five seconds')

    def test_subsecond_defaults_to_milliseconds(self):
        self.assertEqual(num2words(0.5, to='duration'),
                         'five hundred milliseconds')
        self.assertEqual(num2words(1.25, to='duration'),
                         'one second and two hundred and fifty milliseconds')
        self.assertEqual(num2words(Decimal('0.001'), to='duration'),
                         'one millisecond')

    def test_negative(self):
        self.assertEqual(num2words(-5400, to='duration'),
                         'minus one hour and thirty minutes')

    def test_string_and_decimal_input(self):
        self.assertEqual(num2words('5400', to='duration'),
                         'one hour and thirty minutes')
        self.assertEqual(num2words(Decimal('60'), to='duration'),
                         'one minute')

    def test_russian(self):
        self.assertEqual(num2words(0, to='duration', lang='ru'),
                         'ноль секунд')
        self.assertEqual(num2words(5400, to='duration', lang='ru'),
                         'один час тридцать минут')
        self.assertEqual(num2words(60, to='duration', lang='ru'),
                         'одна минута')
        self.assertEqual(num2words(2, to='duration', lang='ru'),
                         'две секунды')
        self.assertEqual(num2words(5, to='duration', lang='ru'),
                         'пять секунд')
        self.assertEqual(num2words(2 * 31536000, to='duration', lang='ru'),
                         'два года')
        self.assertEqual(num2words(5 * 31536000, to='duration', lang='ru'),
                         'пять лет')
        self.assertEqual(num2words(-3, to='duration', lang='ru'),
                         'минус три секунды')
        self.assertEqual(num2words(0.5, to='duration', lang='ru'),
                         'пятьсот миллисекунд')

    def test_unsupported_language_keeps_error_type(self):
        with self.assertRaises(NotImplementedError):
            num2words(1, to='duration', lang='xx')

    def test_cardinal_output_unchanged(self):
        self.assertEqual(num2words(5400),
                         'five thousand, four hundred')
        self.assertEqual(num2words(5400, lang='ru'),
                         'пять тысяч четыреста')
