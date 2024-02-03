from flask import Flask
import DB

app = Flask(__name__)

@app.get('/hello')
def hello():
    db = DB.get_db()
    try:
        res = list(db.users.find({
            "id" : "test"
        }))
        print(res)
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)
