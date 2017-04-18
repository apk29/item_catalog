from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurant')
def showRestaurants():
	return "This page will show all my restaurants"

@app.route('/restaurant/new')
def newRestaurant():
	return "This page will be for making a NEW restaurant"

@app.route('/restaurant/restaurant_id/edit')
def editRestaurant():
	restaurant_id = 1
	return "This page will be for editing restaurant %s" % restaurant_id

@app.route('/restaurant/restaurant_id/delete')
def deleteRestaurant():
	restaurant_id = 3
	return "This page will be for deleting restaurant %s" % restaurant_id

@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def showMenu():
	return "This page is the menu for restaurant %s" restaurant_id

@app.route('/restaurant/restaurant_id/menu/new')
def newMenu():
	restaurant_id = 3
	return "This page is for making new menu item for retaurant %s" % restaurant_id

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)