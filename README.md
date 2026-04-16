# CSCI461 — Assignment 1: Big Data Pipeline

## Team Members
- Member 1: [Mohamed elkassas]
- Member 2: [mohamed elerkesocy]
- Member 3: [ebrahim ahmed]

## Dataset
Amazon Fine Food Reviews (Reviews.csv)
Source: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews

## Docker Commands

### Build the image
docker build -t customer-analytics .

### Run the container
docker run -it --name analytics-container -v "%cd%":/app/pipeline customer-analytics

### Run the pipeline (inside container)
python ingest.py Reviews.csv

### Copy results to host (new terminal)
bash summary.sh

## Execution Flow
Reviews.csv → ingest.py → preprocess.py → analytics.py → visualize.py → cluster.py

## Output Files
| File | Description |
|------|-------------|
| data_raw.csv | Raw copy of input dataset |
| data_preprocessed.csv | Cleaned and transformed data |
| insight1.txt | Statistical summary |
| insight2.txt | Top correlated features |
| insight3.txt | Column types and null check |
| summary_plot.png | 3 visualizations |
| clusters.txt | K-Means cluster sizes |