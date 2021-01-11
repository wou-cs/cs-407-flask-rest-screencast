from flask import Flask, abort, request, url_for


app = Flask(__name__)

siamese = {"breed": "Siamese", "style": "Feisty"}
persian = {"breed": "Persian", "style": "Ambivalent"}
cat_breed_list = [siamese, persian]


@app.route("/api/cat_breeds/<int:breed_id>", methods=["GET"])
def cat_breed(breed_id):
    if 0 <= breed_id < len(cat_breed_list):
        return cat_breed_list[breed_id]
    else:
        abort(404)


@app.route("/api/cat_breeds", methods=["GET"])
def cat_breeds():
    return {"cat_breeds": cat_breed_list}


@app.route("/api/cat_breeds", methods=["POST"])
def new_cat_breed():
    if not request.json:
        abort(400)
    new_breed = request.get_json()
    if "breed" not in new_breed or "style" not in new_breed:
        abort(400)
    new_breed["id"] = 999
    new_breed["location"] = url_for("cat_breed", breed_id=999)
    return new_breed
