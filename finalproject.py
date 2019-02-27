from flask import Flask
app = Flask(__name__)
print "This part works"


@app.route('/')
@app.route('/restaurants')
def mainMenu():
    return "See all the restaurants"


@app.route('/restaurant/new')
def newRest():
    return "Create a new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRest():
    return "Edit a restaurant"


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRest():
    return "Delete a restaurant"


@app.route('/restaurant/<int:restaurant_id/menu')
def showMenu():
    return "See restaurant menu"


@app.route('/restaurannt/<int:restaurant_id>/menu/new')
def newMenu():
    return "New menu"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenu():
    return "Edit a menu"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenu():
    return "Delete a menu"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
