from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

from . import recipe

rps = recipe.Recipes()

# とりあえず、型の指定はなし
#recipes_resource_fields = {
#    'recipe_id' : fields.Integer
#}

class RecipesResource(Resource):

    decorators = [auth.login_required]

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('abstract', type=str, required=True)
    parser.add_argument('category', type=str, required=True)
    parser.add_argument('stuffs', type=dict, required=True)

    def get(self):
        return rps.marshal()

    def post(self):
        args = self.parser.copy().parse_args()
        rcp = recipe.Recipe(title=args['title'])
        rcp.abstract = args['abstract']
        rcp.category = args['category']
        rcp.stuffs = args['stuffs']
        rps.add(rcp)
        return


class RecipeResource(Resource):

    decorators = [auth.login_required]

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
