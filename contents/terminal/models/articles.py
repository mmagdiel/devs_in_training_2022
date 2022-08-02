from functools import reduce 
from operator import concat


class Article:
    name = "articulos"
    attributes = ["id", "name", "description", "price"]
    types_attr = [" integer primary key autoincrement,", " text,", " text,", " real,"]

    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.decription = description
        self.price = price

    @staticmethod
    def create_schema():
        return Article.name, reduce(concat, reduce(concat, zip(Article.attributes, Article.types_attr)))

