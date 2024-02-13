from flask import Flask, render_template, request
from youtube_scraping_api import YoutubeAPI

app = Flask(__name__)
api = YoutubeAPI()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        video_id = request.form["video_id"]

        search_results = api.search(query)
        video_info = api.video(video_id)

        return render_template(
            "results.html", search_results=search_results, video_info=video_info
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
