from app import app, db

@app.cli.command("create-tables")
def create_tables():
    print("Creating database tables...")
    db.create_all()
    print("Tables created successfully.")

if __name__ == '__main__':
    app.run()