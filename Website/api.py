from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)
import model_file as mdl
import json
@app.route('/upload')
def upload_file():
   return render_template('Index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_2():
   if request.method == 'POST':
      f = request.files['file']
      extension_name=(f.filename.split("."))
      f.save("img."+extension_name[1])
      file_name = "img."+extension_name[1]
      lst_of_json_objects=mdl.execute_model_all(file_name)
      with open("Detected_objects.json","w+") as fl:
         json.dump(lst_of_json_objects,fl)
      with open("Detected_objects.json","r") as fl:
         s = fl.read()
         s = str(s)
      return s
		
if __name__ == '__main__':
   app.run(debug = True)


