from flask import Flask,jsonify,request
import json
app=Flask(__name__)

languages = [{'name':'Python'},{'name':'Ruby'},{'name':'Swift'}]

@app.route('/')
def main():
    return jsonify({'The languages are':languages})

@app.route('/<keyword>')
def keyword(keyword):
    return jsonify({'Is this the lang u typed':keyword})

@app.route('/filtered/<string:keyword>')
def filtered(keyword):
    lang = [language for language in languages if language['name']==keyword]
    return jsonify({'the filtered result is' : lang})

@app.route('/posting',methods=['POST'])
def posting():
    lang={'new_name': request.json['keyword']}
    languages.append(lang)
    return jsonify({'result':languages})

@app.route('/putt/<string:keyword>',methods=['PUT'])
def putt(keyword):
    lang=[i for i in languages if i['name'] == keyword]
    lang[0]['name']=request.json['input_data']
    return jsonify({'new_name' : lang})

@app.route('/delete/<string:keyword>',methods=['DELETE'])
def delete(keyword):
    lang=[i for i in languages if i['name'] == keyword]
    languages.remove(lang[0])
    return jsonify({'deleted version':languages})


if __name__ == '__main__':
    app.run(debug=True)
