import scrapy, json

class NBA_Spider(scrapy.Spider):

  name="NBA_Spider"

  start_urls = []
  input_file = open('nba_links.txt', 'r')

  for link in input_file:
    start_urls.append(link)

  def parse(self, response):
    content = response.xpath('//script[@type="application/json"]/text()').get()
    data = json.loads(content)
    homeTeam = data['props']['pageProps']['game']['homeTeam']['teamCity']+" "+data['props']['pageProps']['game']['homeTeam']['teamName']
    pointsHomeTeam = data['props']['pageProps']['game']['homeTeam']['score']
    awayTeam = data['props']['pageProps']['game']['awayTeam']['teamCity']+" "+data['props']['pageProps']['game']['awayTeam']['teamName']
    pointsAwayTeam = data['props']['pageProps']['game']['awayTeam']['score']
    dateGame = data['props']['pageProps']['game']['gameTimeUTC'][:10]
    # new_string = json.dumps(podaci1, indent=2)
    
    yield {
        'homeTeam': homeTeam,
        'pointsHomeTeam': pointsHomeTeam,
        'awayTeam': awayTeam,
        'pointsAwayTeam': pointsAwayTeam,
        'dateGame': dateGame
    }