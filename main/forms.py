from django.forms import ModelForm
from .models import Gear


class GearForm(ModelForm):
    class Meta:
        model = Gear
        fields = ['name', 'use', 'size', 'brand', 'model', 'necessary']
