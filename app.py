from flask import Flask, jsonify, request
import digital_twin as dt
import pandas
import requests

app = Flask(__name__)


@app.route("/get_scores/<int:playerID>", methods=["GET"])
def get_scores(playerID):
    headers = request.headers
    bearer_token = headers.get(
        "Authorization"
    )  # Extract the bearer token from the request headers --> Bearer Token
    # return bearer_token
    token = bearer_token.split()[1]  # JUST THE TOKEN (without "Bearer")

    (
        player_types_labels,
        health_literacy_score,
        response_pt,
        response_hl,
        metrics_overview_pt,
        metrics_overview_hl,
    ) = dt.get_digital_twin(playerID, token)

    scores_dict = {
        "player_types_labels": player_types_labels,
        "health_literacy_score": health_literacy_score,
    }
    return jsonify(scores_dict), 200