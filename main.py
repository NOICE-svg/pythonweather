import bs4
import requests
url = "https://forecast.weather.gov/MapClick.php?lat=37.6624&lon=-121.8726"
response = requests.get(url)
print(response)
soup = bs4.BeautifulSoup(response.text, "html.parser")
print(soup)