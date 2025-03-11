import matplotlib.pyplot as plt
import matplotlib

from Scraper import *
from PiApprox import r_est
from Constants import BETA, LETTERS_IN_ALPHABET


def matplot_settings():
    matplotlib.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    matplotlib.rc('text', usetex=True)


def plot_letter_against_frequency():
    matplot_settings()

    xs = []
    ys = []

    for letter, count in get_counter().most_common():
        xs.append(letter)
        ys.append(count)

    plt.bar(xs, ys, color='royalblue')

    plt.title("Letter frequencies in The Tau Manifesto")
    plt.xlabel("Letter")
    plt.ylabel("Number of appearances")

    plt.savefig('plot-frequency-against-letter.png', dpi=300)
    plt.show()


def plot_frequency_function():
    matplot_settings()

    xs = list(range(1, LETTERS_IN_ALPHABET + 1))
    ys = []

    for _, count in get_counter().most_common():
        ys.append(count)

    plt.plot(xs, ys, marker='o', linestyle='', color='royalblue')

    plt.title("The frequency function $f(r)$")
    plt.xlabel("$r$")
    plt.ylabel("$f(r)$")

    plt.savefig('plot-frequency-function.png', dpi=300)
    plt.show()


def plot_r_est():
    matplot_settings()

    xs1 = []
    xs2 = []
    t = 1
    while t <= 26:
        xs1.append(t)
        if t > 1 + BETA:
            xs2.append(t)
        t += 0.1

    reciprocals = list(map(lambda x: 1 / x, xs1))
    r_ests = list(map(r_est, xs2))

    plt.plot(xs1, reciprocals, color='lightgrey', label=r'$y = 1/r$')
    plt.plot(xs2, r_ests, color='royalblue', label=r'$y = R_{\mathrm{est}}(r)$ where $r \geq 1 + \beta$')

    plt.title(r"Comparing the graphs of $y = R_{\mathrm{est}}(r)$ and $y = 1/r$")
    plt.xlabel("$y$")
    plt.ylabel("$r$")
    plt.legend(loc="upper right")

    plt.savefig('plot-r-est.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    plot_letter_against_frequency()
    plot_frequency_function()
    plot_r_est()