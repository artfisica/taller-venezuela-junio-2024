# taller-ucv-junio-2024

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/artfisica/taller-ucv-junio-2024/HEAD)

## esto es un subtitulo

### esto es otro subtitulo


```
name: Weekly Earnings Check and Publish

on:
  schedule:
    - cron: '00 0 * * *' # Runs every day at 00:00 UTC
  workflow_dispatch:  # Allows manual triggering

jobs:
  check_earnings:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install beautifulsoup4
          pip install requests

      - name: Run earnings check script
        run: |
          chmod +x portafolio-next-week.sh
          chmod +x earnings-csv-single-line.sh
          ./portafolio-next-week.sh stock_symbols.txt > earnings_output.md
          ./earnings-csv-single-line.sh stock_symbols.txt > earnings_output.csv
          cat earnings_output.csv
```