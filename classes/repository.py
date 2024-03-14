from pymongo import MongoClient

# Conectar ao banco de dados
client = MongoClient("mongodb+srv://vinilv:perigo17@rpgdiscord.hu9grnk.mongodb.net/?retryWrites=true&w=majority&appName=RPGdiscord")
db = client['Bots']['User']

class User:
  def __init__(self, id):
    self.id = id
    self.initialize()

  def initialize(self):
    if not db.find_one({"_id": self.id}):
      db.insert_one(
        {"_id": self.id, 
        'sword': {'name': 'espada de brinquedo', 'tier': 1, 'dano': 1, 'valor': 0}, 
        'armor': {'name': 'armadura de brinquedo', 'tier': 1, 'defesa': 1, 'valor': 0},
        'inventory': {
          'sword': [{'name': 'espada de madeira', 'tier': 1, 'dano': 10, 'valor': 1}],
          'armor': [{'name': 'armadura de malha', 'tier': 1, 'defesa': 5, 'valor': 2}]
        },
        'coins': 0, 'tier': 1
      })

  def _get(self):
    return db.find_one({"_id": self.id})