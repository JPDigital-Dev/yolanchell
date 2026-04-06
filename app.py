import os

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    services = [
        {
            "title": "Skin Consultations",
            "description": "Comprehensive assessments for acne, eczema, pigmentation, rashes, and chronic skin concerns.",
        },
        {
            "title": "Mole & Lesion Checks",
            "description": "Early screening and monitoring for suspicious moles, sun damage, and skin cancer warning signs.",
        },
        {
            "title": "Procedural Dermatology",
            "description": "Minor procedures including cryotherapy, biopsies, and treatment plans tailored to your diagnosis.",
        },
        {
            "title": "Aesthetic Skin Care",
            "description": "Medical-grade treatments for texture, scarring, rejuvenation, and long-term skin health.",
        },
    ]

    return render_template("index.html", services=services)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
