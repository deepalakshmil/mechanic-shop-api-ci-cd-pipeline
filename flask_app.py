from dotenv import load_dotenv
from application import create_app
from application.models import db
import os

# Load .env only when running locally 
if os.environ.get("FLASK_ENV") != "production":
    load_dotenv() # This loads .env automatically
                 # Always call load_dotenv() locally before creating the app. 




#app = create_app('ProductionConfig')   
app = create_app("ProductionConfig" if os.environ.get("FLASK_ENV") == "production" else "DevelopmentConfig")
    ## Render will added in environment variable use this (you should set FLASK_ENV=production in Render)




with app.app_context():
    db.create_all() # creates tables if not exist
    # db.drop_all()

# # Run locally
#if __name__ == "__main__":
    # app.run() => remove this line because run the app using gunicorn in production
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

## gunicorn command to run the app in production environment and neccsccary to change app:app => flask_app:app

'''
Notes:

load_dotenv() ensures local .env is loaded.
FLASK_ENV controls whether to use Development or Production config.
PORT environment variable is used for Render deployment.

'''