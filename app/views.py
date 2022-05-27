from flask import render_template, redirect, request, session, url_for
from app.forms import EmailForm
from app import app, babel

@babel.localeselector
def get_locale():
	# If the user has set up the language manually it will be stored in the session
	try:
		language = session['language']
	except KeyError:
		language = None
	if language is not None:
		return language
	return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

@app.context_processor
def inject_conf_var():
	return dict(
		AVAILABLE_LANGUAGES=app.config['LANGUAGES'],
		CURRENT_LANGUAGE=session.get(
			'language',
			request.accept_languages.best_match(app.config['LANGUAGES'].keys())
		)
	)

# This route handles the language change and will store the selected language in the session
@app.route('/language/<language>')
def set_language(language=None):
	session['language'] = language
	return redirect(url_for('index'))

@app.route('/')
def index():
	form = EmailForm()
	return render_template('index.html', form=form)