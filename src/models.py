from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

peopleFavs = db.Table("peopleFav",
     db.Column("users_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
     db.Column("people_id", db.Integer, db.ForeignKey("people.id"), primary_key=True)
)

planetsFavs = db.Table("planetsFav",
     db.Column("users_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
     db.Column("planets_id", db.Integer, db.ForeignKey("planets.id"), primary_key=True)
)

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    genre = db.Column(db.String(20))
    eyeColor = db.Column(db.String(150))
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre,
            "eyeColor": self.eyeColor,
    }

class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    habitantes = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "habitantes": self.habitantes,
    }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    peopleFav = db.relationship(People,
                    secondary=peopleFavs,
                    lazy='subquery',
                    backref=db.backref('users', lazy=True))
    planetsFav = db.relationship(Planets,
                    secondary=planetsFavs,
                    lazy='subquery',
                    backref=db.backref('users', lazy=True))
    
    def __repr__(self):
         return '<User %r>' % self.nickname

    def serialize(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "email": self.email,
            "peopleFav": self.obtain_peopleFav(),
            "planetsFav": self.obtain_planetsFav(),
        }
    
    def obtain_peopleFav(self):
        return list(map(lambda x: x.serialize(), self.peopleFav))

    def obtain_planetsFav(self):
        return list(map(lambda x: x.serialize(), self.planetsFav))