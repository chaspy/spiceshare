#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource, reqparse

from . import recipe as rp

rps = rp.Recipes()

# type is not specified for now
#recipes_resource_fields = {
#    'recipe_id' : fields.Integer
#}

class RecipesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('abstract', type=str, required=True)
    parser.add_argument('category', type=str, required=True)
    parser.add_argument('stuffs', type=dict, required=True)

    def get(self):
        return rps.marshal()

    def post(self):
        args = self.parser.copy().parse_args()
        recipe = rp.Recipe(title=args['title'])
        recipe.abstract = args['abstract']
        recipe.category = args['category']
        recipe.stuffs = args['stuffs']
        rps.add(recipe)
        return


class RecipeResource(Resource):

    def get(self, recipe_id):
        if recipe_id in rps.recipes:
            return rps.recipes[recipe_id].marshal()
        else:
            return 3

    def delete(self, recipe_id):
        rps.delete(recipe_id)
        return

    def patch(self):
        return 4
