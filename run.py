from app import create_app, db

if __name__ == "__main__":
    flask_app = create_app("dev")
    with flask_app.app_context():
        db.create_all()
        print(db)

    flask_app.run(debug=True, host='0.0.0.0', port=8080)


