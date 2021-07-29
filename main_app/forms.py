from django.forms import ModelForm
from .models import UserProfile, Elog, Flog

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'height_feet', 'height_inches', 'current_weight', 'goal_weight'] 

class ElogForm(ModelForm):
    class Meta:
        model = Elog
        fields = [
            'distance_miles', 
            'length_of_time', 
            'reps_laps', 
            'weight_pounds', 
            'intensity', 
            'pace_minutes_per_mile', 
            'calories_burned', ]

class FlogForm(ModelForm):
    class Meta:
        model = Flog
        fields = [ 
            'date_time', 
            'meal_type', 
            'name', 
            'servings'
        ]
