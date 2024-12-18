### Put and Delete-HTTP Verbs
### Working With API's--Json

from flask import Flask,jsonify,render_template,redirect,url_for

app=Flask(__name__)
##Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]
@app.route('/')
def home():
    return "welcome to the to do list."
## get retrieve all the items.
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## retrieving the particular items.
@app.route('/items/<int:item_id>',methods=['POST'])
def get_items_byid(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)


## Create new task  api.
@app.route('/items',methods=['GET'])
def create()


if __name__=='__main__':
    app.run(debug=True)
 