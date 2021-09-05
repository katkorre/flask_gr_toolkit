from flask import Flask, request, render_template
from gr_nlp_toolkit import Pipeline
nlp = Pipeline("pos,ner,dp")
app = Flask(__name__)



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
