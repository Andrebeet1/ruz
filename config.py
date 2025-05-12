import os

class Config:
    # Clé secrète utilisée pour signer les cookies et autres objets sécurisés
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_change_this'
    
    # URI de la base de données (ici avec SQLite par défaut, mais tu peux configurer PostgreSQL sur Render)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///ruz.db'
    
    # Désactivation du suivi des modifications de la base de données (économise des ressources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
