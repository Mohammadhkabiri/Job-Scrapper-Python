# Jobvision Scraper & Data Analyzer 🕷️📊

A powerful Python tool designed to scrape, clean, and analyze job postings from [Jobvision](https://jobvision.ir/) (One of the leading job boards in Iran). This project automates the data collection process, handles pagination, and uses data manipulation techniques to generate insightful, ready-to-use CSV reports.

## 🚀 Features

- **Automated Scraping:** Iterates through pages and extracts hundreds of job postings automatically.
- **Data Extraction:** Captures key details such as Job Title, Company Name, Salary Range, Location, and Company Score.
- **Data Cleaning & Processing:** Cleans messy strings, normalizes salary ranges, and handles missing values.
- **Statistical Output:** Generates summarized datasets (e.g., job distributions, average salaries, top-rated companies).
- **CSV Export:** Saves the raw and processed data into structured `.csv` files for further analysis or visualization.

## 🛠️ Technologies Used

- **Python 3.x**: The core programming language.
- **[Requests](https://pypi.org/project/requests/)**: For sending HTTP requests and communicating with the website/API.
- **[BeautifulSoup4 (bs4)](https://pypi.org/project/beautifulsoup4/)**: For parsing HTML content and extracting specific tags (if applicable).
- **[Pandas](https://pandas.pydata.org/)**: For powerful data manipulation, aggregation, and exporting to CSV.

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/your-username/jobvision-scraper.git
   cd jobvision-scraper
   
