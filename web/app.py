from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)  


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
  if request.method == 'POST':
      text = request.form['text']
      results = []
      d = {}
      doc = nlp(text)
      service_opt = request.form.get("service", None)    
      if service_opt == 'UPOS tag':
        for token in doc.tokens:
          results.append(token.upos)    
        for index, value in enumerate(results):
          d[index] = value 
        return d
      if service_opt == 'Named entity label in IOBES encoding':
        for token in doc.tokens:
          results.append(token.ner)    
        for index, value in enumerate(results):
          d[index] = value 
        return d   
      if service_opt == 'Morphological features':
        for token in doc.tokens:
          results.append(token.feats)    
        for index, value in enumerate(results):
          d[index] = value 
        return d   
      if service_opt == 'Head of the token':
        for token in doc.tokens:
          results.append(token.head)    
        for index, value in enumerate(results):
          d[index] = value 
        return d  
      if service_opt == 'Token-head Dependency Relation':
        for token in doc.tokens:
          results.append(token.deprel)    
        for index, value in enumerate(results):
          d[index] = value 
        return d
app.run()
