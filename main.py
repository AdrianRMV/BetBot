import json
from api.fetch_data import get_odds_by_leagueid
from api.fetch_data import get_league_id


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
            # Muestra el primer resultado de forma legible
            # print(json.dumps(odds_data["response"][0], indent=4))
            print(odds_data["response"][0].fixture.id)
        else:
            print(f"No se encontraron datos para {league_name} en la fecha {date}.")
    else:
        print(f"No se encontró la liga {league_name} para el país {country}.")


if __name__ == "__main__":
    main()
