# utils/database.py
from pymongo import MongoClient
import config

# ===========================
# MongoDB Connection
# ===========================
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]

# ===========================
# Collections
# ===========================
users_col = db['users']          # User info
quizzes_col = db['quizzes']      # Quiz questions
results_col = db['results']      # Quiz results
messages_col = db['messages']    # Messages sent to admin
