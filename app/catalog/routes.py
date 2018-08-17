from app.catalog import catalog
from app import db
from app.catalog.models import Catalog, Item
from flask import render_template, flash, request, redirect, url_for
# from flask_login import login_required
from app.catalog.forms import EditCategoryForm, EditItemForm, CreateCategoryForm, CreateItemForm

from app.tools import user_info, login_required, is_user_authorized


@catalog.route('/')
def display_catalog():
    catalogs = Catalog.query.all()
    items = Item.query.all()
    return render_template('home.html', catalogs=catalogs, items=items, user=user_info())


@catalog.route('/category/get/<category_id>')
def display_category(category_id):
    category = Catalog.query.get(category_id)
    return render_template('category.html', category=category, user=user_info())


@catalog.route('/category/edit/<category_id>', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    category = Catalog.query.get(category_id)
    form = EditCategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        # category.description = form.description.data
        # category.category_id = form.category_id.data
        db.session.add(category)
        db.session.commit()
        flash('Category edit successful')
        return redirect(url_for('catalog.display_catalog'))
    return render_template('edit_category.html', form=form, user=user_info())



@catalog.route('/category/delete/<category_id>', methods=['GET', 'POST'])
@login_required
def delete_category(category_id):
    category = Catalog.query.get(category_id)
    if request.method == 'POST':
        db.session.delete(category)
        db.session.commit()
        flash('category deletion successful')
        return redirect(url_for('catalog.display_catalog'))
    return render_template('delete_category.html', category=category, category_id=category_id, user=user_info())



@catalog.route('/item/get/<item_id>')
def display_item(item_id):
    item = Item.query.get(item_id)
    return render_template('item.html', item=item, user=user_info())


@catalog.route('/create/category', methods=['GET', 'POST'])
@login_required
def add_category():
    form = CreateCategoryForm()
    if form.validate_on_submit():
        # user_info = user_info()
        category = Catalog(name=form.name.data, owner=user_info()['email'])

        db.session.add(category)
        db.session.commit()
        flash('category added successfully')

        return redirect(url_for('catalog.display_catalog'))
    return render_template('create_category.html', form=form, user=user_info())


@catalog.route('/create/item/', methods=['GET', 'POST'])
@login_required
def add_item():
    form = CreateItemForm()

    if form.validate_on_submit():
        # user_info = user_info()
        item = Item(name=form.name.data, description=form.description.data, category_id=form.category_id.data, owner=user_info()['email'])

        db.session.add(item)
        db.session.commit()
        flash('Item added successfully')

        return redirect(url_for('catalog.display_catalog'))        
    return render_template('create_item.html', form=form, user=user_info())


@catalog.route('/item/edit/<item_id>', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):
    item = Item.query.get(item_id)
    form = EditItemForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        item.category_id = form.category_id.data
        db.session.add(item)
        db.session.commit()
        flash('Item edit successful')
        return redirect(url_for('catalog.display_catalog'))
    return render_template('edit_item.html', form=form, user=user_info())


@catalog.route('/item/delete/<item_id>', methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    item = Item.query.get(item_id)
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        flash('item deletion successful')
        return redirect(url_for('catalog.display_catalog'))
    return render_template('delete_item.html', item=item, item_id=item_id, user=user_info())


