"""
    tests.test_recipe
"""
import pytest
import spiceshare

def test_recipe_marshal_fullparam():
    expect = {
        'recipe_id' : "bbb",
        'title': "aaa",
        'abstract': "ccc",
        'category': "ddd",
        'stuffs': {"a": "a", "b": "b"}
        }
    rcp = spiceshare.recipes.recipe.Recipe("aaa", "bbb", "ccc", "ddd", {"a":  "a", "b": "b"})
    actual = rcp.marshal()
    assert expect == actual

def test_recipe_marshal_default_conf():
    expect = {
        'recipe_id' : None,
        'title': "aaa",
        'abstract': None,
        'category': None,
        'stuffs': {}
        }
    rcp = spiceshare.recipes.recipe.Recipe("aaa")
    actual = rcp.marshal()
