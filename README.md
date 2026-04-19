# pwd
Wrangling data with pythons bs4 and pandas for dashboard

### The Strategy

You don't want to parse HTML using basic string replacements (which breaks easily). Instead, you want to approach it systematically:
1. **Extract:** Read the raw HTML.
2. **Parse:** Use an HTML parser to navigate the "tree" of tags (finding elements by their `class` or `id`). Notice how one date row (like Tuesday, 3/31) contains *multiple* nested scan events. Your code needs to handle that.
3. **Transform:** Clean the extracted text and merge the dates and times into a proper, standardized timestamp.
4. **Load:** Put the cleaned data into a tabular format.

### Breaking Down Why This Code Works

* **`BeautifulSoup` prevents headaches:** Instead of using messy Regex to try and find text between `<span>` and `</span>`, BeautifulSoup understands HTML hierarchy. It lets you say, *"Find me the span that explicitly has the ID of 'status'."*
* **Handling 1-to-Many Relationships:** The nested `for` loop is vital here. If you just scraped dates and statuses separately, your columns wouldn't line up because days like "3/31/26" have four different statuses attached to them. Looping through the *events inside the row* keeps the data linked.
* **Creating a `Timestamp`:** A massive part of a Data Engineer's job is standardizing data types. "Saturday, 3/21/26" and "1:10 AM" are just useless strings to a database. Combining them into a formal `pd.to_datetime` object allows analysts down the line to actually filter the data (e.g., "Show me all packages that moved between 2 AM and 6 AM").

If you run this code, that giant block of HTML garbage will instantly become a pristine, three-column table sorted perfectly by Timestamp, Status, and Location. 
