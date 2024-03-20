# install untuk flasknya
from flask import Flask, request, render_template,jsonify
# install kebutuhan untuk dbnya
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bengkelku.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definisikan model Bengkel ormnya
class Bengkel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Bengkel {self.nama}>'

# Route untuk menambahkan data bengkel
@app.route('/add_bengkel', methods=['GET', 'POST'])
def add_bengkel():
    if request.method == 'POST':
        nama = request.form['nama']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        new_bengkel = Bengkel(nama=nama, latitude=latitude, longitude=longitude)
        db.session.add(new_bengkel)
        db.session.commit()
        return 'Bengkel added successfully'
    return render_template('add_bengkel.html')

# Route untuk melihat semua data bengkel
@app.route('/view_bengkel', methods=['GET'])
def view_bengkel():
    bengkels = Bengkel.query.all()
    return render_template('view_bengkel.html', bengkels=bengkels)

@app.route('/')
def bengkel_terdekat():
    return render_template('bengkel_terdekat.html')
    
@app.route('/get_bengkels', methods=['GET'])
def get_bengkels():
    bengkels = Bengkel.query.all()
    bengkels_list = []
    for bengkel in bengkels:
        bengkels_list.append({
            'nama': bengkel.nama,
            'latitude': bengkel.latitude,
            'longitude': bengkel.longitude
        })
    return jsonify(bengkels_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
