from app import db

class Scenario(db.Model):
    key = db.Column('key', db.Integer, primary_key = True)
    shortname = db.Column('shortname', db.Text)
    desc = db.Column('desc', db.Text)

    def __init__(self, shortname, desc):
      self.shortname = shortname
      self.desc = desc
   
    def getJSON(self):
        json = {
            "key" : self.key,
            "shortname" : self.shortname,
            "desc": self.desc
        }
        return json
    
    def setAll(self, shortname, desc):
        self.shortname = shortname
        self.desc = desc

class Links(db.Model):
    key = db.Column('key', db.Integer, primary_key = True)
    from_key = db.Column('from_key', db.Integer)
    to_key = db.Column('to_key', db.Integer)
    desc = db.Column('desc', db.Text)

    def __init__(self, from_key, to_key, desc):
        self.from_key = from_key
        self.to_key = to_key
        self.desc = desc
        return True
   
    def getJSON(self):
        json = {
            "key" : self.key,
            "from_key" : self.from_key,
            "to_key" : self.to_key,
            "desc": self.desc
        }
        return json

    def setAll(self, from_key, to_key, desc):
        self.from_key = from_key
        self.to_key = to_key
        self.desc = desc

class History(db.Model):
    key = db.Column('key', db.Integer, primary_key = True)
    timestamp = db.Column('timestamp', db.Date)
    level = db.Column('level', db.Integer)
    desc = db.Column('desc', db.Text)

    def __init__(self, timestamp, level, desc):
      self.timestamp = timestamp
      self.level = level
      self.desc = desc

    def getJSON(self):
        json = {
            "key" : self.key,
            "timestamp" : self.timestamp,
            "level" : self.level,
            "desc": self.desc
        }
        return json

    def setAll(self, timestamp, level, desc):
        self.timestamp = timestamp
        self.level = level
        self.desc = desc