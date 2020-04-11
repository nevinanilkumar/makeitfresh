from shopproject import create_app
from shopproject.config import Config

app = create_app()
app.config.from_object(Config)

if __name__=='__main__':
    app.run(debug=True)