from django.test import TestCase
from .models import Editor,Article,tags
from django.db import models
import datetime as dt



# Create your tests here.

class EditorTestClass(TestCase):
    
    def setUp(self):
        self.rovine= Editor(first_name = 'Rovine', last_name ='Wanjala', email ='rovinewanjala99@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rovine,Editor))

# Testing Save Method
    def test_save_method(self):
        self.rovine.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.rovine= Editor(first_name = 'Rovine', last_name ='Wanjala', email ='rovinewanjala99@.com')
        self.rovine.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.rovine)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()


    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)



def test_get_news_by_date(self):
        test_date = '2020-12-31'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)