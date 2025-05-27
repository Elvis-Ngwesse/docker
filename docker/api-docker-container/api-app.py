from flask import Flask, jsonify, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load the CSV once
df = pd.read_csv("cities.csv")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/top-cities', methods=['POST'])
def top_cities():
    country_name = request.form.get('country_name', '').strip()
    filtered = df[df['country'].str.lower() == country_name.lower()]

    if filtered.empty:
        return render_template('index.html', error="Country not found or no data available.", country=country_name)

    top_cities = filtered.sort_values(by='population', ascending=False).head(20)
    cities = top_cities[['city', 'population']].to_dict(orient='records')

    return render_template('index.html', cities=cities, country=country_name)


@app.route('/api/top-cities/<country_name>', methods=['GET'])
def api_top_cities(country_name):
    filtered = df[df['country'].str.lower() == country_name.lower()]
    if filtered.empty:
        return jsonify({"error": "Country not found or no data available."}), 404

    top_cities = filtered.sort_values(by='population', ascending=False).head(20)
    result = top_cities[['city', 'population']].to_dict(orient='records')

    return jsonify({
        "country": country_name,
        "top_cities": result
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
