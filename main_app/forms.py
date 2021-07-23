from django.forms import ModelForm
from .models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'height_feet', 'height_inches', 'current_weight', 'goal_weight'] 
    
