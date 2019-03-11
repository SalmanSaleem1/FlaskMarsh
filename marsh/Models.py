from marsh import db, ma


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref='rewards')


class AuthorSchema(ma.ModelSchema):
    class Meta:
        model = Author


class RewardSchema(ma.ModelSchema):
    class Meta:
        model = Reward
