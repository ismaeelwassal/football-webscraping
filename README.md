# 📊 Football Web Scraping

**Football Web Scraping** is a console-based **Python application** that scrapes football match details (teams, results, and match times) from **[Yallakora](https://www.yallakora.com/)** based on a **user-provided date**.  
The results are **exported into a CSV file** for easy access and analysis.  

---

## 🚀 **Features**
- **Scrape by Date** → Enter any date (**YYYY-MM-DD**) and get all matches of that day.  
- **Match Details** → Extracts **tournament name**, **team names**, **score**, and **match time**.  
- **CSV Export** → Saves results into:  
  `documents/yallakora/matches-details.csv`  
- **Error Handling** → Notifies you if there are **no matches** on the given date.  

---

## 🛠️ **Technologies Used**
- **Python 3**  
- **Requests** → for fetching the webpage.  
- **BeautifulSoup (bs4)** → for parsing HTML.  
- **lxml** → fast parser for BeautifulSoup.  
- **CSV module** → for saving results.
- ------- 
## Usage

1. Clone the repository:
```bash
git clone https://github.com/ismaeelwassal/webscraping-project.git

```
2. Navigate to the project folder:
```bash
cd webscraping-project
```
3.Install required dependencies:
```bash
pip install -r requirements.txt
```
4.Run the script:
```bash
python webscraping.py
```
5.Enter the desired date in the format YYYY-MM-DD.
6. The results will be automatically saved in:
```bash
documents/yallakora/matches-details.csv
```

