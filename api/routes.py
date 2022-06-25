from app import app
from api.models import scenario, links

@app.route('/scenario')
def all_scenario():
   ret = {"data" : []}
   for x in scenario.query.order_by("key"):
      ret["data"].append(x.getJSON())
   return ret

@app.route('/links')
def all_links():
   ret = {"data" : []}
   for x in links.query.order_by("key"):
      ret["data"].append(x.getJSON())
   return ret