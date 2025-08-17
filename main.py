from src.clean_data import load_and_clean

PATH_FILE = "data/Sleep_health_and_lifestyle_dataset.csv"

df = load_and_clean(PATH_FILE)

if __name__ == "__main__":
    
    df.info()