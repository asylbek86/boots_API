from django.db import models




class Boots(models.Model):
    title = models.CharField('Названия', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    image = models.ImageField('Фотография', upload_to='')
    description = models.TextField('Описание')
    
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    
    def  __str__(self):
        return self.name
        