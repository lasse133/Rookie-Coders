from webapp import create_app

app = create_app()

# run file directly 
if __name__ == '__main__':
    app.run(debug=True)

