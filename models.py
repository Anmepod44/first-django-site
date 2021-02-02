from django.db import models
import uuid
# Create your models here.
class Genre(models.Model):
    #The Genre Entity
    name=models.CharField(max_length=200,help_text="Enter a Book Genre i.e Science Fiction ,Horror etc")
    def __str__(self):
        return self.name

class Book(models.Model):
    #The Book Entity
     

    title=models.CharField(max_length=200,help_text="The Title Of The Book")

    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary=models.TextField(max_length=1000,help_text="enter a brief description of the book")
    isbn=models.CharField('ISBN',max_length=13,unique=True,help_text='13 character <h><a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a></h>')
    genre=models.ManyToManyField('Genre',help_text="select a genre for this book")

    def __str__(self):
        #string for representing the object model
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", args=[str(self.id)])
    

class BookInstance(models.Model):
     
    #the book instance represents a specific copy of a book that someone might borrow and includes information about whether the book is available or not
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="unique id for this book across the whole library")

    #ON_DELETE SET TO RESTRICT TO ENSURE A BOOK CANNOT BE DELETED WHEN REFERENCED BY A BOOK INSTANCE
    book=models.ForeignKey('Book',on_delete=models.RESTRICT)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)
    language=models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)

    LOAN_STATUS=(
        ('m','Maintainance'),
        ('o','On Loan'),
        ('a','Available'),
        ('r','Reserved')
    )



    status=models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text="Book Availability")
    class meta:
        ordering=['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
     
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

    

    def get_absolute_url(self):
         return reverse('Author_detail',args=[str(self.id)])


    def __str__(self):

        return f'{self.first_name},{self.last_name}'
    
    class Meta:
        ordering=['last_name','first_name']


class Language(models.Model):
    
     
    name=models.CharField(max_length=100,help_text="Enter Language The Book is Written In")

    def __str__(self):
        return f'{self.language}'
     