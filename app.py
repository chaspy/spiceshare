#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api

import recipes as rp

BASE_URL = "/curry/v1"
RECIPES_URL = "/recipes"
RECIPE_URL_PATTERN = "/<string:recipe_id>"

app = Flask(__name__)
api = Api(app)

api.add_resource(rp.RecipesResource, BASE_URL + RECIPES_URL)
api.add_resource(rp.RecipeResource, BASE_URL + RECIPES_URL + RECIPE_URL_PATTERN)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
