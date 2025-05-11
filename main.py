from flask import Flask, jsonify, send_from_directory
import psycopg2

app = Flask(__name__, static_folder='static')

def get_partners():
    conn = psycopg2.connect(
        dbname="exam",
        user="postgres",
        password="root",
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, phone FROM partners")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [f"{name} - {phone}" for name, phone in rows]

@app.route('/api/partners')
def partners():
    return jsonify(get_partners())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def static_files(path):
    if path == '':
        path = 'index.html'
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
