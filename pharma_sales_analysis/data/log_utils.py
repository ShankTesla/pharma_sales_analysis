# log_utils.py

# Import libraries
from pathlib import Path 
import json 
import os 

# find project root and point to reports/ 
PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_FILE = PROJECT_ROOT / "reports" / "pipeline_log.json"

def log_step(df, name):

     # Load log if exists or create new if it doesn't exist
    if os.path.exists(LOG_FILE):
          with open(LOG_FILE, "r") as f:
               log = json.load(f)
    else:
        log = []

    # Append the new row count meta-data
    log.append({"step": name, "rows": len(df)})

    # Save it back to the disk

    with open(LOG_FILE, "w") as f:
         json.dump(log, f, indent=4)

    return df 