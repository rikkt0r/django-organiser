from django.forms import forms, CharField, BooleanField, IntegerField, ChoiceField, \
    RadioSelect, DateTimeField, DecimalField
from django.forms.widgets import Textarea, Select, TextInput, DateTimeInput, \
    NumberInput, HiddenInput, CheckboxInput


# Yeah, i know modelForm might be suitable..
# but i'm learning django, so yeah.. let it be for now
class TaskForm(forms.Form):

    REPEAT = (
        (0, 'Do not repeat'),
        (1, 'Daily'),
        (2, 'Weekly'),
        (4, 'Monthly'),
        (8, 'Other (enter days count)'),
    )

    STATUSES = (
        (0, 'Deleted'),
        (1, 'Active'),
        (2, 'Done')
    )

    PRIORITIES = (
        (0, 'No rush'),
        (1, 'Normal'),
        (2, 'Important')
    )

    # id omitted
    # user omitted
    # date_created omitted
    # date_modified omitted
    # status omitted

    name = CharField(
        widget=TextInput(attrs={'placeholder': 'Input task name'}),
        label="Task name",
        max_length="80",
        required=True
    )

    # description = models.TextField(max_length=2000)
    description = CharField(
        widget=Textarea(attrs={'rows': 8})
    )

    priority = ChoiceField(
        widget=RadioSelect,
        label="Priority",
        choices=PRIORITIES,
        initial=1
    )

    date_from = DateTimeField(
        widget=DateTimeInput(attrs={'placeholder': 'Choose date'}),
        label="Date From",
        input_formats=['%Y/%m/%d %H:%M', '%Y-%m-%d %H:%M:%S']
        # or just leave for default https://docs.djangoproject.com/en/1.8/ref/forms/fields/#datetimefield
    )

    date_to = DateTimeField(
        widget=DateTimeInput(attrs={'placeholder': 'Choose date'}),
        label="Date To",
        input_formats=['%Y/%m/%d %H:%M', '%Y-%m-%d %H:%M:%S']
        # or just leave for default https://docs.djangoproject.com/en/1.8/ref/forms/fields/#datetimefield
    )

    repeat = ChoiceField(
        widget=Select(),
        label="Repeat task",
        choices=REPEAT,
        initial=0
    )

    repeat_days = IntegerField(
        widget=NumberInput(),
        label="Repeat days (when chosen other)",
        min_value=1,
        max_value=60,
        initial=1,
        required=False
    )

    lat = DecimalField(
        widget=HiddenInput(),
        label="Latitude",
        min_value=-90.0,
        max_value=90.0,
        max_digits=8,
        decimal_places=6,
        required=False
    )

    lng = DecimalField(
        widget=HiddenInput(),
        label="Longitude",
        min_value=-180.0,
        max_value=180.0,
        max_digits=8,
        decimal_places=6,
        required=False
    )

    place_desc = CharField(
        widget=TextInput(attrs={'placeholder': 'Additional place description? Eg. Room 427, Stanley'}),
        label="Place description",
        min_length=5,
        max_length=250,
        required=False
    )

    public = BooleanField(
        widget=CheckboxInput(attrs={'checked': True}),
        label="Public (should it be available to others by unique url?)",
        required=False
    )
