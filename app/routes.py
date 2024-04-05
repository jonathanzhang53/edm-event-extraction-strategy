from flask import jsonify, request
from . import app
from .adapters import TicketmasterAdapter, EdmtrainAdapter, DiceFmAdapter

@app.route('/')
def index():
    return "Welcome to the Event Extractor API!"

@app.route('/events')
def get_events():
    source = request.args.get('source')
    adapter = None

    if source == 'ticketmaster':
        adapter = TicketmasterAdapter()
    elif source == 'edmtrain':
        adapter = EdmtrainAdapter()
    elif source == 'dicefm':
        adapter = DiceFmAdapter()
    else:
        return jsonify({'error': 'Invalid source parameter'}), 400

    events = adapter.fetch_events()
    events_dict = [event.__dict__ for event in events]
    return jsonify(events_dict)
