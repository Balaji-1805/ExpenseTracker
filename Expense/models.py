from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    # category name should be unique
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_categories",null=True,blank=True)
    
    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return f"{self.name}"
    

# One category have many expenses
class Expense(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="expenses")
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_expenses",blank=True,null=True)

    def __str__(self):
        return f"{self.title}-{self.amount}"