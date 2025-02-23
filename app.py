from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/github-stats', methods=['GET'])
def get_github_stats():
    username = request.args.get('username')  # Get username from URL params
    if not username:
        return jsonify({"error": "Username parameter is required"}), 400

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    data = response.json()
    return jsonify({
        "name": data.get("name"),
        "avatar_url": data.get("avatar_url"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "bio": data.get("bio"),
        "location": data.get("location"),
    })

if __name__ == '__main__':
    app.run(debug=True)
