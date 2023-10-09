import json
from api.fetch_data import get_odds_by_leagueid
from api.fetch_data import get_league_id
from api.fetch_data import get_fixture_details_by_id


def main():
    print("=== INICIANDO ===")
    date = "2023-10-08"  # Fecha actual
    league_name = "Liga MX"
    country = "Mexico"
    season = 2023

    # Obtén el ID de la liga
    league_id = get_league_id(country, league_name)

    if league_id:
        # Obtén los fixtures usando el ID de la liga
        odds_data = get_odds_by_leagueid(league_id, season, date)
        if odds_data:
            for fixture in odds_data["response"]:
                fixture_id = fixture["fixture"]["id"]
                details = get_fixture_details_by_id(fixture_id)

                home_team = details["response"][0]["teams"]["home"]["name"]
                away_team = details["response"][0]["teams"]["away"]["name"]

                print(
                    f"Fixture id: {fixture_id}, Equipos:{home_team} (casa) VS {away_team} (visitante)"
                )
        else:
            print(f"No se encontraron datos para {league_name} en la fecha {date}.")
    else:
        print(f"No se encontró la liga {league_name} para el país {country}.")


if __name__ == "__main__":
    main()
