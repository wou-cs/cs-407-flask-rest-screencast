from flask import Flask, abort, request, url_for


app = Flask(__name__)

siamese = {"breed": "Siamese", "style": "Feisty"}

persian = {"breed": "Persian", "style": "Ambivalent"}

cat_breed_list = [siamese, persian]


@app.route("/api/catbreeds/<int:breed_id>", methods=["GET"])
def cat_breed(breed_id):
    if breed_id < 0 or breed_id >= len(cat_breed_list):
        abort(404)
    return cat_breed_list[breed_id]


@app.route("/api/catbreeds", methods=["GET"])
def cat_breeds():
    return {"catbreeds": cat_breed_list}


@app.route("/api/catbreeds", methods=["POST"])
def new_cat_breed():
    if not request.json:
        abort(400)
    new_breed = request.get_json()
    if "breed" not in new_breed or "style" not in new_breed:
        abort(400)
    new_breed["id"] = 999
    new_breed["location"] = url_for("catbreed", id=999)
    return new_breed
