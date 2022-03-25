from URL_Shortening_Service import app, db
from flask import Flask, render_template, url_for, session, logging, request, flash, redirect
from .models import Link, random_token
from .config import domain


@app.route('/', methods = ['POST', 'GET'])
def add_link():
	if request.method == 'POST':
		original_url = request.form['original_url']
		custom = request.form['custom']

		if original_url :
			token_str = domain + custom if custom else domain +random_token()
			print(token_str)
			link = Link(original_url = original_url, shorten_url = token_str)
			db.session.add(link)
			db.session.commit()
			flash("Mission Done , Success..!")
			print(link.shorten_url)
			return render_template('view_new_link.html', original_URL = original_url ,Shorten_URL = link.shorten_url)
		
		else:
			flash("Enter a Valid URL..!")
			return render_template('index.html')

	return render_template('index.html')


@app.route('/view_links')
def status():

	links = Link.query.all()
	titles = ('Original', 'Shorten_URL', 'Visits')

	return render_template('view_links.html' , row_titles = titles, links = links )


@app.route('/delet_link/<id>', methods =['POST', 'GET'])
def delet_article(id):
	my_row = Link.query.filter_by(id = id).first()

	# delete the row from db session if it exists
	if my_row :
	    db.session.delete(my_row)
	    db.session.commit()
	    flash("YOU Are Deleting an exiting Shorten Link , Success..!")
		
	return render_template('index.html')


@app.route('/visit/<shorten_url>')
def redirect_to_url(shorten_url):
	"""When users access a short link, our service should redirect them to the original link
	"""
	link = Link.query.filter_by(shorten_url = shorten_url).first()
	if link:
		link.visits += 1
		db.session.commit()
		return redirect(link.original_url)
	
	else:
		flash("No Valid URL Found")
	return render_template('index.html')

