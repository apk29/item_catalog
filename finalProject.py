from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
	# return "This page will show all my restaurants"
	return render_template('restaurants.html', restaurant=restaurant)

@app.route('/restaurant/new/')
def newRestaurant():
# 	# return "This page will be for making a NEW restaurant"
	return render_template('newrestaurant.html', restaurants=restaurants)

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
	# restaurant_id = 1
	# return "This page will be for editing restaurant %s" % restaurant_id
	return render_template('editRestaurant.html', restaurant=restaurant)

@app.route('/restaurant/restaurant_id/delete/')
def deleteRestaurant():
	# restaurant_id = 2
	# return "This page will be for deleting restaurant %s" % restaurant_id
	return render_template('deleteRestaurant.html', restaurants=restaurants)

@app.route('/restaurant/restaurant_id/')
@app.route('/restaurant/restaurant_id/menu/')
def showMenu():
	# restaurant_id = 3
	# return "This page is the menu for restaurant %s" % restaurant_id
	return render_template('menus.html', restaurants=restaurants)
# @app.route('/restaurant/restaurant_id/menu/new/')
# def newMenuItem():
# 	# restaurant_id = 4
# 	# return "This page is for making new menu item for retaurant %s" % restaurant_id

# @app.route('/restaurant/restaurant_id/menu/menu_id/edit/')
# def editMenuItem():
# 	# restaurant_id = 4
# 	# menu_id= 5
# 	# return "This page is for is for editing menu item %s" % menu_id	

# @app.route('/restaurant/restaurant_id/menu/menu_id/delete/')
# def deleteMenuItem():
# 	# restaurant_id = 6
# 	# menu_id= 7
# 	# return "This page is for deleting menu item %s" % menu_id

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)