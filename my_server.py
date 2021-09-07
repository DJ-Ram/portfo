from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

##way - 1
@app.route('/')
def my_home():
	return render_template('index.html')

# @app.route('/index.html')
# def my_index():
# 	return render_template('index.html')

# @app.route('/works.html')
# def my_works():
# 	return render_template('works.html')

# @app.route('/about.html')
# def my_info():
# 	return render_template('about.html')

# @app.route('/contact.html')
# def my_contact():
# 	return render_template('contact.html')

##we do not need components page, hence delete the related nv bar contect from each html file
# @app.route('/components.html')
# def my_components():
# 	return render_template('components.html')

##way -2 keep my_home route as it is
@app.route('/<string:pagename>')
def html_page(pagename = None):
	return render_template(pagename)
 #----------------------------------------------------------
 #writing to database.txt file
def write_to_file(data):
	with open('database.txt', 'a') as db:
		email = data['email']
		subject = data['text']
		message = data['msg']
		file = db.write(f'\n{email},{subject},{message}')

#writing to database.csv
def write_to_csv(data):
	with open('database.csv' , mode = 'a', newline ='') as db2:
		email = data['email']
		subject = data['text']
		message = data['msg']
		csv_writer = csv.writer(db2, delimiter =',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict() #retrieving and converting data submitted in the contact page to dict
			print(data) #observe the op in cmd prompt
			#write_to_file(data)
			write_to_csv(data)
			return redirect('/thankyou.html') ##as soon as user submit the form, we are redirecting to tq.html to display msg
		except:
			return 'Did not save to database'
	else:
		return 'Something went wrong. Please try again!!'


