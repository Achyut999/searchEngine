from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
qw = ['what','which','when','where','who', 'whom','whose','why','whether','how']
av = ['be','am', 'is','are','was', 'were', 'been','being','have','have', 'has','had','will','shall']
q = input()
if str in qw and q:
  navv = string.split(str in qw in q)
if str in av and q:
  nv = string.split(str in av in q)

# Define the URL to scrape
url1 = "https://www.geeksforgeeks.org/"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the elements with the class "head"
    articles = soup.find_all(class_="head")

    # Loop through the articles and print their titles
    for article in articles:
        title = article.a.text
        print(title)
