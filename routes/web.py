"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    ## Blogs Route Group ("/blog")
    RouteGroup([
        Get("/", "BlogController@index").name("index"),
        Get("/@id", "BlogController@show").name("show"),
        Post("/", "BlogController@create").name("create"),
        Put("/@id", "BlogController@update").name("update"),
        Delete("/@id", "BlogController@destroy").name("destroy")

    ], prefix="/blog", name="blog")
]
