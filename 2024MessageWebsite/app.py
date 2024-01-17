from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = """
    Hey [Friend's Name],

    Yaar, jab sochta hoon ki hum mile 2023 mein, toh bas ek hi cheez aati hai dimaag mein – 2024 mein milna kitna amazing hoga! Seriously, yaar, teri mulaqat se hi mera har saal perfect ho jaata hai.

    Tere bina toh kuch bhi adhoora lagta hai. Teri woh hassi, tere saath bitaye pal, sab kuch yaadgaar hai. Aur pata hai, 2024 mein humare saath hone wale moments se mera excitement bhi next level pe hai.

    Saath mein jo bhi karenge, har ek pal dhamal hoga. Can't wait to create more memories and have a blast together in 2024. Tu meri life ka best part hai, aur tujhe milna hi ek special feeling hai.

    2024, hum aayenge aur chha jayenge! Ready ho ja, yaar, kyunki yeh saal humara hoga!

    Dher saara pyaar,

    [Tera Naam]
    """

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)


