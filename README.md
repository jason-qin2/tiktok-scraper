# tiktok-scraper

This is a Tiktok scraper that gathers data on fashion related Tiktoks

## Usage

Build a Docker image
```bash
docker image build -t tiktok-scraper app/
```
Run the docker container and store it in the results.csv file
```bash
docker run tiktok-scraper > results.csv
```

