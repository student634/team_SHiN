import os

# 必要そうなライブラリを取りあえずコピペ（後々増えたり減ったりするはず）
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# 空の辞書
# REGISTANTS = {}

# 人気な言語をあらかじめ用意しておく
LANGUAGES = [
    "Python",
    "C",
    "C++",
    "C#",
    "Java",
    "JavaScript",
    "VB",
    "SQL",
    "PHP",
    "Assembly language",
    "Ruby",
    "Go",
    "Kotlin",
    "AWS",
    "Swift",
    "HTML",
    "CSS"
]

# データベースを紐付ける
db = SQL("sqlite:///sns.db")

# 起動時、必ずHomeが表示されるように
@app.route("/")
def home():
    # ただHome画面を表示するだけ
    return render_template('home.html')

# ログイン処理
@app.route("/login", methods=["GET", "POST"])
def login():
    # それまで保存されていたセッションを消去
    # session.clear()

    # POST通信だった（フォームが送信された）場合
    if request.method == "POST":

        # フォームの情報を取得
        login_id = request.form.get("login_id") # ユーザー名
        login_pass = request.form.get("login_pass") # パスワード

        # データベースから（ユーザー名・パスワード）が一致する行を抜き出し
        line = db.execute("SELECT * FROM users WHERE name = ? AND WHERE password = ?", login_id, login_pass)

        # セッションにidを代入
        session["user_id"] = line[0]["user_id"]

        # page移動
        return redirect("record.html")

    # /loginにアクセスしただけの場合
    else:
        return render_template("login.html")

# 登録処理
@app.route("/register", methods=["GET", "POST"])
def register():

    # POST通信だった（フォームが送信された）場合
    if request.method == "POST":

        # フォームの情報を取得
        register_id = request.form.get("register_id") # ユーザー名
        register_pass = request.form.get("register_pass") # パスワード

        # 名前被りチェック
        # パスワードをハッシュ化
        hashed_password = generate_password_hash(register_pass, method='pbkdf2:sha256', salt_length=8)

        # データベースにformのデータを記録 & 返ってきた主キーをuser_idへ代入
        user_id = db.execute("INSERT INTO users (name, password) VALUES (?,?)", register_id, hashed_password)

        # セッションにuser_idを代入
        session["user_id"] = user_id

        # page移動
        return redirect('record.html')

    # /registerにアクセスしただけの場合
    else:
        return render_template("register.html")

# 記録処理
# 中井が担当
@app.route("/record", methods=["GET", "POST"])
# @login_required
def record():

    if request.method == "POST":

        # エラー言語（選ぶ）formじゃないかも?
        language = request.form.get("language")
        # エラー
        error = request.form.get("error")
        # 状況説明
        explanation = request.form.get("explanation")
        # 解決策
        solution = request.form.get("solution")

        # apology 作らないといけない,helpers.pyみたいなの
        if not language:
            return apology("missing language", 400)


        if not error:
            return apology("please enter an error", 400)

        if not explanation:
            return apology("Please explain the situation", 400)

        # 未解決の場合（ボタンが押されたらにした方がいい？）
        if not solution:
            flash("記録しました！頑張ったね！")
            db.execute("INSERT INTO errors (language, message, explain) VALUES(?, ?, ?)", language, error, explanation)
            return render_template("unsolved.html")

        # 解決できた場合
        else:
            flash("記録しました！解決できてすごい！")
            db.execute("INSERT INTO errors (language, message, explain, solved) VALUES(?, ?, ?, ?)", language, error, explanation, solution)
            return render_template("solved.html")

    else:
        return render_template("record.html", language=LANGUAGES)

#イシモリ #最終更新 2/25
# 未解決のエラーを表示
@app.route("/unsolved")
# @login_required
def display_unsolved():

    # 未解決エラーをデータベースから取り出し、格納
    unsolved_errors = db.execute("SELECT * FROM errors WHERE solved LIKE 'unsolved' AND user_id=?", session["user_id"])

    return render_template("unsolved.html", unsolved_errors=unsolved_errors)

#解決済みのエラーを表示
@app.route("/solved")
# @login_required
def display_solved():

    # 解決済みのエラーをデータベースから取り出し、格納
    solved_errors = db.execute("SELECT * FROM errors WHERE solved LIKE 'solved' AND user_id=?", session["user_id"])

    return render_template("solved.html", solved_errors=solved_errors)

#####イシモリ
if __name__ == "__main__":
    app.run(debug=True)