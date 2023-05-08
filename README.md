# LAU-Banner-Scraper
Web Scraper for course listed on LAU's Banner page
=======
# LAU Course Scraper

This Python script scrapes the LAU course website and exports the data to a CSV file.

## Prerequisites

- Python 3.x
- Selenium
- Chrome webdriver
- A LAU student account

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Download the Chrome webdriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system path.
4. Open the `banner_scraper.py` file and either edit the `username` and `password` variables to match your LAU student account or run the script and add as arguments the username and password.
5. Run the script using `python banner_scraper.py first.lastname password`.
6. When prompted, enter the filename to store the data in. The file should end with `.csv`.

## Usage

After running the script, the data will be exported to a CSV file in the format:

| Select | CRN | Subj | Crse | Sec | Cmp | Cred | Title | Days | Time | Cap | Act | Rem | WL | Cap | WL | Act | WL | Rem | XL | Cap | XL | Act | XL | Rem | Instructor | Date (MM/DD) | Location | Attribute |

---

## Script generated for the CSC498P Course
![LAU](https://img.shields.io/badge/CSC498P-7D4698?style=for-the-badge&logo=LAU-Browser&logoColor=white)

