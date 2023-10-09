import http.client
import json

HEADERS = {
    "X-RapidAPI-Key": "de84e8834amshedd7a3ebf2390e5p1193a5jsn85418706d0d5",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
}


def get_countries():
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    conn.request("GET", "/v3/countries", headers=HEADERS)

    res = conn.getresponse()

    return json.loads(res.read().decode("utf-8"))


def get_leagues_by_country_name(country):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    endpoint = f"/v3/leagues?country={country}"
    conn.request("GET", endpoint, headers=HEADERS)

    res = conn.getresponse()
    tournmentsData = json.loads(res.read().decode("utf-8"))

    return tournmentsData


def get_fixtures_by_leagueid(date):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    endpoint = f"/v3/fixtures?date={date}"
    conn.request("GET", endpoint, headers=HEADERS)

    res = conn.getresponse()
    fixturesData = json.loads(res.read().decode("utf-8"))

    return fixturesData


def get_league_id(country, league_name):
    leagues_data = get_leagues_by_country_name(country)

    for league in leagues_data["response"]:
        if league["league"]["name"] == league_name:
            return league["league"]["id"]

    return "Hola"


def get_odds_by_leagueid(league_id, season, date):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    endpoint = f"/v3/odds?league={league_id}&season={season}&date={date}"
    conn.request("GET", endpoint, headers=HEADERS)
    res = conn.getresponse()
    odds_data = json.loads(res.read().decode("utf-8"))

    return odds_data
