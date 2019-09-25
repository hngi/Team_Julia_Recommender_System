from flask import Flask, jsonify, request
import turicreate as tc
import json
app = Flask(__name__)
model = tc.load_model("follower_rec")
article = tc.load_model('rating_model')


@app.route('/recomend/<int:num>',  methods=['GET'])
def prediction(num):
    if request.method == 'GET':
        print('users recommended are: ')
        return jsonify(list(model.recommend([num], k=3)))


@app.route('/articles/<int:num>',  methods=['GET'])
def prediction_article(num):
    if request.method == 'GET':
        print('users recommended are: ')
        return jsonify(list(article.recommend([num], k=3)))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')