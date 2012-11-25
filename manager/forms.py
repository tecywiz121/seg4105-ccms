from django import forms
import calendar
from datetime import datetime

class ReportForm(forms.Form):
    MONTH = 0
    WEEK = 1
    DAY = 2

    PERIOD_CHOICES = ((MONTH, 'Month'),
                        (WEEK, 'Week'),
                        (DAY, 'Day'))

    ALL_DAY = 0
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3

    TIME_OF_DAY_CHOICES = ((ALL_DAY, 'All Day'),
                            (BREAKFAST, 'Breakfast'),
                            (LUNCH, 'Lunch'),
                            (DINNER, 'Dinner'))

    DAY_CHOICES = tuple((x, x) for x in range(1, 32))
    MONTH_CHOICES = list(zip((x.lower() for x in calendar.month_abbr), calendar.month_name))[1:]
    YEAR_CHOICES = tuple((x, x) for x in range(2000, 2100))

    period = forms.ChoiceField(widget=forms.RadioSelect, choices=PERIOD_CHOICES, initial=DAY)
    time_of_day = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=TIME_OF_DAY_CHOICES, initial=[ALL_DAY])
    day = forms.ChoiceField(choices=DAY_CHOICES, initial=1, required=False)
    month = forms.ChoiceField(choices=MONTH_CHOICES, initial=datetime.now().strftime('%b'))
    year = forms.ChoiceField(choices=YEAR_CHOICES, initial=datetime.now().year)
