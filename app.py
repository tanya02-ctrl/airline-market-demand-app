from flask import Flask, render_template, request
from utils.data_processing import fetch_api_data, process_api_data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    selected_route = request.args.get('route', '')
    api_data = fetch_api_data()
    all_insights = process_api_data(api_data)

    # Filter insights by selected route
    if selected_route and selected_route in all_insights:
        filtered_insights = {selected_route: all_insights[selected_route]}
    else:
        filtered_insights = all_insights

    return render_template('index.html', insights=filtered_insights, all_routes=list(all_insights.keys()), selected_route=selected_route)

if __name__ == '__main__':
    app.run(debug=True)
