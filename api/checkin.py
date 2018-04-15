from flask import Blueprint

checkin = Blueprint('checkin', __name__)

@checkin.route('/api/checkin')
def get_checkin_data():
  return 'TODO: return JSON data here'
