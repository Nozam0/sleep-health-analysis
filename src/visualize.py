import seaborn as sns
import matplotlib.pyplot as plt

def plot_sleep_distribution(df):
    sns.histplot(df["sleep_duration_(hours)"], bins=10)
    plt.title("Distribución de duración del sueño")
    plt.xlabel("Horas")
    plt.ylabel("Frecuencia")
    plt.show()