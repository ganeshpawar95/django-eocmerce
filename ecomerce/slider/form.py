from django import forms  
from .models import Slider  
  
class sliderForm(forms.ModelForm):  
    class Meta:  
        model = Slider  
        fields = "__all__"  
    