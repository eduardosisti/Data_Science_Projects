from app_flask import app

app = app.server

if __name__ == "__main__":
    app.run_server(debug=False, use_reloader=False)