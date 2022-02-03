from flask import request, Flask, render_template, redirect, url_for, jsonify
from service import gen_rand_civ, gen_matches
app = Flask(__name__)
candidates1, candidates2 = None, None
civi1, civi2 = None, None
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        rand_count = request.form['randCount']
        ban_count = request.form['banCount']
        print(rand_count, ban_count)
        return redirect(url_for('pick', rand_count=rand_count, ban_count=ban_count))
    else:    
        return render_template('home.html')

@app.route("/pick", methods=['GET'])
def pick():
    rand_count = int(request.args['rand_count'])
    ban_count = int(request.args['ban_count'])
    print(rand_count, ban_count)
    global candidates1
    global candidates2
    candidates1, candidates2 = gen_rand_civ(rand_count)

    return render_template('pick.html', candidates1=candidates1, candidates2 = candidates2, ban_count=ban_count)


@app.route("/match", methods=['GET', 'POST'])
def match():
    if request.method == 'POST':
        data = request.json
        bans1 = data['bans1']
        bans2 = data['bans2']
        bans1 = list(map(int, bans1))
        bans2 = list(map(int, bans2))
        global civi1, civi2
        civi1, civi2 = gen_matches(bans1, bans2, candidates1, candidates2)
        print(civi1, civi2)
        return 'ok', 200
    else:
        print(civi1)
        return render_template('match.html', matches = zip(civi1, civi2))





if __name__ == "__main__":
    app.run(debug=True)