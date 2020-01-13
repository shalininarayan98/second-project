from application import db

class Predictions(db.Model):
    predictionID = db.Column(db.Integer, primary_key=True, autoincrement = True)
    prediction = db.Column(db.String(200), nullable = True)


    def __repr__(self):
        return ''.join([
            'ID: ', str(self.id),'\r\n',
            'prediction ', self.theme
        ])


