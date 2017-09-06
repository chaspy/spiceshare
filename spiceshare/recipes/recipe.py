#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson import objectid


class Recipe:
    __slots__  = ['__recipe_id', '__title', '__abstract', '__category', '__stuffs']

    @property
    def recipe_id(self):
        return self.__recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        self.__recipe_id = recipe_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract):
        self.__abstract = abstract

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def stuffs(self):
        return self.__stuffs

    @stuffs.setter
    def stuffs(self, stuffs):
        self.__stuffs = stuffs

    def __init__(self, title, recipe_id = None, abstract = None, category = None,
                 stuffs = dict()):
        self.recipe_id = recipe_id
        self.title = title
        self.abstract = abstract
        self.category = category
        self.stuffs = stuffs

    def marshal(self):
        return {
            'recipe_id' : self.recipe_id,
            'title' : self.title,
            'abstract' : self.abstract,
            'category' : self.category,
            'stuffs' : self.stuffs
        }

    def marshal_overview(self):
        return {
            'recipe_id' : self.recipe_id,
            'title' : self.title,
            'abstract' : self.abstract
        }


class Recipes:
    __slots__ = ['__cl', '__db', '__co',
                 '__recipes']

    @property
    def recipes(self):
        return self.__recipes

    def __init__(self):
        self.__cl = MongoClient()
        self.__db = self.__cl.CurryDB
        self.__co = self.__db.recipes_collection
        self.__recipes = dict()
        self.get()

    def get(self):
        for recipe in self.__co.find():
            self.recipes[str(recipe['_id'])] = \
                Recipe(recipe_id=str(recipe['_id']), title=recipe['title'],
                       abstract=recipe['abstract'], category=recipe['category'],
                       stuffs=recipe['stuffs']
                       )

    def add(self, recipe):
        result = self.__co.insert_one({
            'title': recipe.title,
            'abstract': recipe.abstract,
            'category': recipe.category,
            'stuffs': recipe.stuffs
        })
        recipe.recipe_id = str(result.inserted_id)
        self.__recipes[recipe.recipe_id] = recipe

    def delete(self, recipe_id):
        self.__co.remove(objectid.ObjectId(recipe_id))
        del self.__recipes[recipe_id]

    def marshal(self):
        marshaled = {
            'recipes' : []
        }
        # sort sample
        for v in (sorted(self.__recipes.values(), key=lambda recipe: recipe.recipe_id)):
            marshaled['recipes'].append(v.marshal_overview())
        return marshaled

