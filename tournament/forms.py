from django import forms
from .models import Makep

class MakeForm(forms.ModelForm):
    class Meta:
        model = Makep
        fields = ['name', 'contact', 'city', 'zip', 'amount', 'card']



    #tour_img = forms.ImageField(required=False)


class Participate(forms.Form) :
       name = forms.CharField(max_length=100)
       age = forms.IntegerField()
       gender = forms.CheckboxSelectMultiple()
       add = forms.CharField(widget=forms.Textarea)
       ph_no = forms.IntegerField()
