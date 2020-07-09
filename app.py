from flask import Flask, render_template, request, Response
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import iberdrola
from pprint import pprint
import pdb

app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = './'

#app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

@app.route('/upload')
def upload_file():
   return render_template('/upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
       f = request.files['file']
       pprint(f)
       pdb.set_trace()
       csv = iberdrola.convertir_csv (f)
       return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})
      #f.save(secure_filename(f.filename))
      #print (f)
      #return send_file(salida.csv)
       #print ('file uploaded successfully')
       #return  render_template('/download.html')
"""
@app.route('/getPlotCSV') # this is a job for GET, not POST
def getPlot_CSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    csv = iberdrola.convertir_csv (f)
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})
"""


if __name__ == '__main__':
    app.run(debug=True)
