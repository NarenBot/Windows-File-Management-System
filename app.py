import os
from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/arrange_files', methods=['GET', 'POST'])
def arrange_files():
    cwd = [str(x) for x in request.form.values()][0]
    if os.path.exists(cwd):
        files = os.listdir(cwd)
        folder_path = []
        for file in files:
            route = os.path.join(cwd, os.path.splitext(file)[1][1:])
            route = route.lower()
            if route not in folder_path:
                folder_path.append(route)
        print(folder_path)
        print(len(folder_path))

        for folder in folder_path:
            try:
                os.mkdir(folder)
            except:
                pass

            for file in files:
                if os.path.split(folder)[1] == os.path.splitext(file)[1][1:].lower():
                    os.rename(os.path.join(cwd, file),
                              os.path.join(folder, file))

        return render_template('index.html', output="Files successfully moved to respective folders.")

    else:
        return render_template('index.html', output="Please enter the correct path!")


if __name__ == '__main__':
    app.run(debug=True)
