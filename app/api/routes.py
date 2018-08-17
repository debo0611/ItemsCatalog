"""routes for api blueprint"""

from app.api import api
from app.catalog.models import Catalog, Item
from flask import jsonify

@api.route('/categories')
def categories_api():
    """
    Api endpoint to lists all created categories
    """
    categories = Catalog.query.all()
    category_list = [c.serialize() for c in categories]
    return jsonify(category_list)


@api.route('/category/<int:category_id>')
def category_api(category_id):
    """
    Api endpoint to show a category with a given id
    """
    category = Catalog.query.get(category_id)
    return jsonify(category.serialize())


@api.route('/items')
def items_api():
    """
    Api endpoint to list all created items
    """
    items = Item.query.all()
    item_list = [i.serialize() for i in items]
    return jsonify(item_list)

@api.route('/item/<int:item_id>')
def item_api(item_id):
    """
    Api endpoint to show an item with a given id
    """
    item = Item.query.get(item_id)
    return jsonify(item.serialize())
