from website import create_app

app = create_app()
app.secret_key = 'change this'

if __name__ == '__main__':
    app.run()