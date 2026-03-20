import logging
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_db

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("Pipeline started")

    df = extract_data("data/mentah/reviews.csv")
    logging.info(f"Extracted {len(df)} rows")

    df = transform_data(df)
    logging.info("Data transformed")

    load_to_db(df)
    logging.info("Data loaded to database")

    logging.info("Pipeline finished")

if __name__ == "__main__":
    run_pipeline()