from sqlite3 import IntegrityError
from app import app, db
from flask import request
from api.models import Scenario, Links, History
from datetime import datetime


@app.route('/scenario')
def all_scenario():
   ret = {"data" : []}
   for x in Scenario.query.order_by("key"):
      ret["data"].append(x.getJSON())
   return ret

@app.route('/links')
def all_links():
   ret = {"data" : []}
   for x in Links.query.order_by("key"):
      ret["data"].append(x.getJSON())
   return ret

@app.route('/history')
def all_history():
   ret = {"data" : []}
   for x in History.query.order_by("key"):
      ret["data"].append(x.getJSON())
   return ret

@app.route('/scenario/add', methods = ['POST'])
def add_scenario():
   shortname = request.form.get('shortname')
   desc = request.form.get('desc')
   try:
      scenario = Scenario(shortname, desc)
      db.session.add(scenario)

      history = History(datetime.now(), 1, shortname + " added with desc: " + desc)
      db.session.add(history)

      db.session.commit()
      return "inserted"
   except IntegrityError:
      return "IntegrityError: Please check the body of the request"
   except Exception as e:
      print(str(e))
      return "Exception: See console for error"