from flask import Flask, redirect, url_for, request, render_template
from modelPanel import evaluate_model
app = Flask(__name__)

@app.route('/home',methods = ['GET'])
def main():
	return render_template('home.html')

@app.route('/submit-form',methods = ['POST'])
def submit():
	return redirect(f"/results?temperatura={request.form['temperatura']}&irradiancia={request.form['irradiancia']}")

@app.route('/results',methods = ['GET'])
def result():
	temperatura = float(request.args.get('temperatura'))
	irradiancia = float(request.args.get('irradiancia'))
	resultados, Vmpp, Impp, P_max = evaluate_model(irradiancia,temperatura+273)
	
	values_chart_x = str([ "%.2f"%(v) for v in resultados['Voltaje (V)'].tolist()]).replace("'", "")
	values_chart_y_corriente = [(x - min(resultados['Corriente (A)'].tolist())) / (max(resultados['Corriente (A)'].tolist()) - min(resultados['Corriente (A)'].tolist())) for x in resultados['Corriente (A)'].tolist()] 
	values_chart_y_potencia = [(x - min(resultados['Potencia (W)'].tolist())) / (max(resultados['Potencia (W)'].tolist()) - min(resultados['Potencia (W)'].tolist())) for x in resultados['Potencia (W)'].tolist()] 

	return render_template('result.html',
		temperatura=temperatura,
		irradiancia=irradiancia,
		max_potencia="%.2f"%(P_max),
		max_voltaje="%.2f"%(Vmpp),
		max_corriente="%.2f"%(Impp),
		chart_x=values_chart_x,
		chart_y_corriente=values_chart_y_corriente,
		chart_y_potencia=values_chart_y_potencia)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)