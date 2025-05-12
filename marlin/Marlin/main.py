from app import app

# Initialize the database at startup
with app.app_context():
    from app import db
    db.create_all()

# This handler is needed for Vercel
def handler(request, **kwargs):
    return app(request.environ, request.start_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
