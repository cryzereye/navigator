from sqlite3 import IntegrityError
from app import app, db
from flask import request
from api.models import Scenario, Link, History
from datetime import datetime


@app.route('/scenario')
def all_scenario():
   ret = {"data" : []}
   for x in Scenario.query.order_by("key"):
      ret["data"].append(x.getJSON())
   return ret

@app.route('/link')
def all_link():
   ret = {"data" : []}
   for x in Link.query.order_by("key"):
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
      
      res =  {
         "response": {
            "key": scenario.key,
            "shortname" : scenario.shortname,
            "desc": scenario.desc
         }
      }
      return res
   except IntegrityError:
      return "IntegrityError: Please check the body of the request"
   except Exception as e:
      print(str(e))
      return "Exception: See console for error"

@app.route('/link/add', methods = ['POST'])
def add_link():
   from_sname = request.form.get('from_sname')
   to_sname = request.form.get('to_sname')
   desc = request.form.get('desc')
   try:
      from_key = Scenario.query.filter_by(shortname = from_sname).with_entities(Scenario.key).first()
      to_key = Scenario.query.filter_by(shortname = to_sname).with_entities(Scenario.key).first()

      link = Link(from_key[0], to_key[0], desc)
      db.session.add(link)

      history = History(datetime.now(), 1, from_sname + " linked to " + to_sname)
      db.session.add(history)

      db.session.commit()
      
      res =  {
         "response": {
            "key": link.key,
            "from_sname" : from_sname,
            "to_sname": to_sname,
            "desc": desc
         }
      }
      return res
   except IntegrityError:
      return "IntegrityError: Please check the body of the request"
   except Exception as e:
      print(str(e))
      return "Exception: See console for error"