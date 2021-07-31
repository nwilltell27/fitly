from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MEAL_TYPE = (
      ('B', 'Breakfast'),
      ('L', 'Lunch'),
      ('D', 'Dinner'),
      ('S', 'Snack')
    )

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height_feet = models.IntegerField()  # so they there feet in the height_feet field and the remaining inches in the height_inches
    height_inches = models.IntegerField()  
    current_weight = models.DecimalField(max_digits=5, decimal_places=2)
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2)  
    current_BMI = models.IntegerField()
    goal_BMI = models.IntegerField()
    current_blood_pressure_sys = models.IntegerField()
    current_blood_pressure_dia = models.IntegerField()
    current_blood_pressure_sys = models.IntegerField()
    goal_blood_pressure_dia = models.IntegerField()
    goal_blood_pressure_sys = models.IntegerField()
    cureent_blood_sugar = models.IntegerField()
    goal_blood_sugar = models.IntegerField()
    goal_daily_calories = models.IntegerField()
    goal_carbs_grams = models.IntegerField()
    goal_proteins_grams = models.IntegerField()
    goal_fats_grams = models.IntegerField()

    def __str__(self):
      return self.user_id
    def get_absolute_url(self):
      return reverse('detail', kwargs={'user_id': self.id})

'''      
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    time_minutes = models.IntegerField()
    distance_miles = models.DecimalField(max_digits=4, decimal_places=2) 
    reps_laps = models.IntegerField()  
    weight_pounds = models.IntegerField() # for resistant training
    intensity = models.IntegerField() # 1 - 5
    pace_per_mile = models.IntegerField()
    calories_burned = models.IntegerField()
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
      return self.user
    def get_absolute_url(self):
      return reverse('exercise_detail', kwargs={'name': self.id})
'''
class Elog(models.Model):
    date_time = models.DateTimeField()
    name = models.CharField(max_length=50)
    distance_miles = models.DecimalField(max_digits=5, decimal_places=2) 
    length_of_time = models.IntegerField(default=0)
    reps_laps = models.IntegerField()  
    weight_pounds = models.DecimalField(max_digits=5, decimal_places=2) # for resistant training
    intensity = models.IntegerField() # 1 - 5
    pace_minutes_per_mile = models.IntegerField()
    calories_burned = models.IntegerField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('elogs/detail', args={'user_id': self.request.user})

'''
class Food(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    serving_size = models.DecimalField(max_digits=4, decimal_places=2) 
    serving_size_units = models.CharField(
        max_length=3,
        choices=SERVING_SIZE_UNITS,
        default=SERVING_SIZE_UNITS[0][0]
    )  
    carbs_grams = models.IntegerField() # for resistant training
    proteins_grams = models.IntegerField() # 1 - 5
    fats_grams = models.IntegerField()
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
      return self.name
    def get_absolute_url(self):
      return reverse('food_detail', kwargs={'name': self.id})
'''
class Flog(models.Model):
    date_time = models.DateTimeField('meal date')
    meal_type = models.CharField(
      max_length=1,
      choices=MEAL_TYPE,
      default=MEAL_TYPE[0][0]
    )
    name = models.CharField(max_length=50)
    servings = models.DecimalField(max_digits=5, decimal_places=2) 
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
      return f"Had {self.name} for {self.get_meal_type_display()} on {self.date_time}"
'''
    def get_absolute_url(self):
      return reverse('flog_detail', kwargs={'date_time': self.id})
'''

