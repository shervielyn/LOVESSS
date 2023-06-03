from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/events")
def events_list():
  events_data = [
    {
    'id': 1,
    'Name': 'Swimming Competitions',
    'Location': 'Rutgers University',
    'Date': 'July 17th, 2021',
    'Description': 'Competition for the best swimming athletes around the world'
    },
    {
    'id': 2,
    'Name': 'Marathon',
    'Location': 'Brooklyn Bridge', 
    'Date': 'August 8th, 2021',
    'Description': 'Marathon for everyone in the city'
    },
    {
    'id': 3,
    'Name': 'Basketball Tournament',
    'Location': 'Columbia University',
    'Date': 'September 5th, 2021',
    'Description': 'Tournament for the best basketball players around the world'
    }
  ]
  return jsonify(events_data)
  

if __name__ == "__main__":
  app.run(debug=True)