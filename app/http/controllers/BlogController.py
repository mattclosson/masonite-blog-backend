"""A BlogController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Blog import Blog

class BlogController(Controller):
    """BlogController Controller Class."""

    def __init__(self, request: Request):
        """BlogController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self):
        return Blog.all()

    def show(self):
        id = self.request.param("id")
        return Blog.find(id)

    def create(self):
        title = self.request.input("title")
        body = self.request.input("body")
        blog = Blog.create({"title": title, "body": body})
        return blog
    
    def update(self):
        id = self.request.param("id")
        title = self.request.input("title")
        body = self.request.input("body")
        Blog.where("id", id).update({"title": title, "body": body})
        return Blog.where("id", id).get() 

    def destroy(self):
        id = self.request.param("id")
        blog = Blog.where("id", id).get()
        Blog.where("id", id).delete()
        return blog 