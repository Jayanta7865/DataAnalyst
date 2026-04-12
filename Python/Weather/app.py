from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔥 Put your real API key here
API_KEY = "43c5a75775f6cdab74ae82e48b5e4436"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            url = f"https://wttr.in/{city}?format=j1"
            
            try:
                response = requests.get(url)
                data = response.json()

                print(data)  # 🔍 debug (optional)

                # ✅ check API response
                if str(data.get("cod")) == "200":
                    weather = {
                        "city": data.get("name"),
                        "temp": data["main"]["temp"],
                        "desc": data["weather"][0]["description"]
                    }
                else:
                   weather = {
    "city": city,
    "temp": data["current_condition"][0]["temp_C"],
    "desc": data["current_condition"][0]["weatherDesc"][0]["value"]
}

            except Exception as e:
                weather = {
                    "city": city,
                    "temp": "N/A",
                    "desc": "Something went wrong"
                }

    return render_template("index.html", weather=weather)


if __name__ == "__main__":
    app.run(debug=True)