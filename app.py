from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            img = qrcode.make(text)
            img_path = os.path.join("static", "qrcode.png")
            img.save(img_path)
            return render_template("index.html", qr_code=img_path)
    return render_template("index.html", qr_code=None)

@app.route("/download")
def download_qr():
    return send_file("static/qrcode.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)