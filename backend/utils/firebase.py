# utils/firebase.py
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('backend/firebase_config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
