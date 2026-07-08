"""
AirAsia Project — main entry point.

This is the file you run to start the program:

    python src/main.py

Right now it just proves everything is wired up correctly. As the project
grows, add your real automation steps inside the run() function below.
"""

from dotenv import load_dotenv

from utils.helpers import get_logger

# Load settings from the .env file (if it exists) into the program.
load_dotenv()

log = get_logger()


def run() -> None:
    """The main routine. Add your automation steps here."""
    log.info("=" * 45)
    log.info("AirAsia Project is running! 🚀")
    log.info("=" * 45)

    # --- TODO: add your real steps below ---
    # Example:
    #   1. Read some input data from the data/ folder
    #   2. Do the automation (call an API, scrape a site, etc.)
    #   3. Save the results
    log.info("Everything is set up. Add your logic in src/main.py -> run().")


if __name__ == "__main__":
    run()
