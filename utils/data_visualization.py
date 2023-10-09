import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib.request


def plot_odds(teams, odds):
    fig, axs = plt.subplots(len(teams), 1, figsize=(10, 8 * len(teams)))

    for idx, (team, team_odds) in enumerate(odds.items()):
        # Descargar el logo del equipo
        urllib.request.urlretrieve(team["logo"], "temp_logo.png")
        img = mpimg.imread("temp_logo.png")

        # Mostrar el logo del equipo
        axs[idx].imshow(img)
        axs[idx].axis("off")

        # Mostrar las probabilidades
        for odd in team_odds:
            bet = odd["value"]
            value = odd["odd"]
            axs[idx].text(
                1.2, 0.5, f"{bet}: {value}", transform=axs[idx].transAxes, fontsize=12
            )

    plt.tight_layout()
    plt.show()
