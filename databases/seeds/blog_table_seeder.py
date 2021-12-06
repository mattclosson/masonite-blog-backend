"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Tutorial", "body": "How to build a robot"})
        Blog.create({"title": "Vacation", "body": "My trip to Paris"})
        Blog.create({"title": "Politics", "body": "Everyone is wrong but me"})