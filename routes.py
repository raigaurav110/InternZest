from app import app
from flask import Flask, render_template, url_for,abort
import json
import os

with open("data/states_data.json", "r") as f:
    states_data = json.load(f)

@app.route('/')
@app.route('/index')
@app.route('/state/index')
@app.route('/state/index.html')
def index():
    return render_template('index.html', states=states_data)

@app.route('/packages')
def packages():
    return render_template('package.html')

@app.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

@app.route('/login')
@app.route('/state/login.html')
def login():
    return render_template('login.html')

@app.route('/state/<state_key>')
def show_state(state_key):
    state = states_data.get(state_key)

    if state is None:
        abort(404) 
    return render_template(
        "state.html",
        state_key=state_key,
        state=state,
        state_name=state['name'],
        header_bg=state['backgrounds']['header'],
        discover_bg=state['backgrounds']['discover'],
        fixed_img_bg=state['backgrounds']['fixed'],
        img1=state['history_images']['img1'],
        img2=state['history_images']['img2'],
        box_img = state['box_image']['box_img'],
        discover_img1 = state['discover_images']['discover_img1'],
        discover_img2 = state['discover_images']['discover_img2'],
        discover_img3 = state['discover_images']['discover_img3'],
        discover_img4 = state['discover_images']['discover_img4'],
        history_text = state.get('history_text', []),
        discover_text = state.get('discover_text', []),
        more_text = state.get('more_text', []),
        state_table=state.get('state_table', {})
    )