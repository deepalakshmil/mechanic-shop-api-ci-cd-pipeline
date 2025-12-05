
from application import create_app
from application.models import db
# import os

app = create_app('ProductionConfig')   

with app.app_context():
    db.create_all()
    # db.drop_all()


# app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))