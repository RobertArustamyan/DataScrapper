[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas Version](https://img.shields.io/badge/Pandas-1.3.3-orange?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

This project is a Python-based web scraper designed to collect and process data from a real estate website, specifically for properties available for sale and rent. The scraper extracts various details about each property, such as category (sale or rent), address, price, area, floor, and more, and saves the data into a CSV file for further analysis.

## Overview
The scraper consists of several modules, each responsible for a specific task:
- `links_parsing.py`: Contains classes for parsing links to properties available for sale and rent.
- `geting_data_from_link.py`: Defines a class for extracting data from each property link.
- `converting_to_excel.py`: Provides a function to convert the collected data from CSV to Excel format.

## Features
- Parses property links for both sale and rent categories.
- Extracts detailed information about each property, including address, price, area, and more.
- Saves the collected data into a CSV file.
- Supports converting the CSV file to Excel format for easier data visualization and analysis.
![](screenshots/img.png)

## Usage
1. Clone the repository to your local machine.
2. Install the required libraries mentioned in the `Requirements` section.
3. Run the `main.py` script to start the scraping process.
4. Once the scraping is complete, the collected data will be saved in the `Data` directory as `result.csv`.
5. Optionally, you can convert the CSV file to Excel format using the `converter()` function from `converting_to_excel.py`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
