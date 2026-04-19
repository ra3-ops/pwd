
### The Python Solution

### Here is the code you would write using **BeautifulSoup** (to parse the HTML) and **Pandas** (to build the table). 

```python
from bs4 import BeautifulSoup
import pandas as pd

# 1. Load your raw HTML block (assigned to a variable for this example)
html_data = """<YOUR_HTML_STRING_HERE>"""

# 2. Initialize BeautifulSoup to parse the HTML tree
soup = BeautifulSoup(html_data, 'html.parser')

# This list will hold our parsed records before we make a table
parsed_records = []

# 3. Find every main row in the table
# Looking at the HTML, each day is wrapped in a <tr> with this specific class
daily_rows = soup.find_all('tr', class_='travel-history-table__row')

for row in daily_rows:
    # --- A. Extract the Date ---
    date_cell = row.find('td', class_='travel-history-table__scan-event-date')
    date_text = date_cell.text.strip() if date_cell else None
    
    # --- B. Extract the Events for that Date ---
    # One date can have multiple events (like Arriving, then Departing).
    # We find all event blocks within the current row.
    events = row.find_all('div', class_='travel-history__scan-event')
    
    for event in events:
        # Extract Time (It's typically the first simple <span> in the event block)
        time_text = event.find('span').text.strip() if event.find('span') else None
        
        # Extract Status (Conveniently, FedEx tagged this with id="status")
        status_element = event.find('span', id='status')
        status_text = status_element.text.strip() if status_element else None
        
        # Extract Location (It's stored in the last div with regular font weight)
        location_divs = event.find_all('div', class_='fdx-u-fontweight--regular')
        location_text = location_divs[-1].text.strip() if location_divs else None
        
        # Append the clean dictionary to our list
        parsed_records.append({
            'Raw_Date': date_text,
            'Time': time_text,
            'Status': status_text,
            'Location': location_text
        })

# 4. Transform into a Table using Pandas
df = pd.DataFrame(parsed_records)

# 5. Clean up the Data Types (Crucial for Data Engineering!)
# Remove the day of the week (e.g., "Saturday, ") to easily parse the date
df['Clean_Date'] = df['Raw_Date'].str.split(', ').str[-1]

# Combine Date and Time into a single, highly queryable Datetime object
df['Timestamp'] = pd.to_datetime(df['Clean_Date'] + ' ' + df['Time'])

# Drop the old messy columns and reorder for a clean final table
final_table = df[['Timestamp', 'Status', 'Location']]

print(final_table)
```
