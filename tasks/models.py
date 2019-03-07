from django.db import models
import datetime 
from django.contrib.auth import get_user_model
User=get_user_model()

# class List(models.Model): 
#   title = models.CharField(maxlength=250, unique=True) 
#   def __str__(self): 
#     return self.title 



# PRIORITY_CHOICES = ( 
#   (1, 'Low'), 
#   (2, 'Normal'), 
#   (3, 'High'), 
# ) 
# class Item(models.Model): 
#   title = models.CharField(maxlength=250) 
#   created_date = models.DateTimeField(default=datetime.datetime.now) 
#   priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
#   completed = models.BooleanField(default=False) 
#   todo_list = models.ForeignKey(List) 
#   def __str__(self): 
#     return self.title 


from django.utils import timezone

class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.name #name to be shown when called

class TodoList(models.Model): #Todolist able name that inherits models.Model
	created_by=models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True) # a text field 
	created = models.DateField(auto_now_add=True)
	due_date = models.DateField() # a date
	completed = models.BooleanField(default=False)
	category = models.ForeignKey(Category, default=1,on_delete=models.CASCADE) 

	class Meta:
		ordering = ["-created"]
	
	def __str__(self):
		return self.title #name to be shown when called