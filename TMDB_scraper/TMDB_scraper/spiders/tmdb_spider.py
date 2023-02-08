# to run 
# scrapy crawl tmdb_spider -o movies.csv

import scrapy
import requests
from random import randint

# The two functions below are copied or referred directly from:
#   https://scrapeops.io/docs/fake-user-agent-headers-api/integrations/python-requests/
#   https://docs.scrapy.org/en/latest/topics/request-response.html
# to add a fake user agent and overcome the 403 error

def get_user_agent_list():
    API = '106a64bb-cf36-4c5e-bb5a-e576ac3dd531'
    response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=' + API)
    json_response = response.json()
    return json_response.get('result', [])

def get_random_user_agent(user_agent_list):
    random_index = randint(0, len(user_agent_list) - 1)
    return user_agent_list[random_index]

# Retrieve User-Agent List From ScrapeOps
user_agent_list = get_user_agent_list()
headers = {'User-Agent': get_random_user_agent(user_agent_list)}

class TmdbSpider(scrapy.Spider):
    name = 'tmdb_spider'
    start_urls = ['https://www.themoviedb.org/movie/680-pulp-fiction']

    def start_requests(self):
        '''
            The very first request to go. We defune the start url here,
            and add headers to scrapy.Request.
            Navigate to the movie page.
        '''

        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        '''
            Parse the main page of the MOVIE. 
            Get the link of the FULL CAST & CREW page.
            Navigate to FULL CAST & CREW page.
        '''

        # Get the hyperlink reference (on the Full Cast & Crew button) to the Cast page
        cast_page = response.css("p.new_button a::attr(href)").get()
        yield scrapy.Request(url = "https://www.themoviedb.org" + cast_page,
                            headers=headers,    # user agent
                            callback=self.parse_full_credits)

    def parse_full_credits(self, response):
        '''
            Parse the FULL CAST & CREW page.
            Get the links to all of the actors of our MOVIE.
            Navigate to each of the ACTOR pages.
        '''

        # Get the hyperlink references of all the actors
        links = response.css("ol[class='people credits '] p[class!='character'] a::attr(href)").getall()
        for link in links:  
            yield scrapy.Request(url = "https://www.themoviedb.org" + link,
                                headers=headers,    # user agent
                                callback=self.parse_actor_page)

    def parse_actor_page(self, response):
        '''
            Parse the ACTOR page.
            Get the actor name, and the names of all of the movies he/she was in.
            Output dictionaries containing the actor name and the movie name.
        '''

        # Get the name of actor
        name = response.css("h2.title a::text").get()
        # Get the names of all movies/shows the actor participated in
        movies = response.css("table.credit_group a.tooltip bdi::text").getall()
        # Yield the results as dictionary
        for movie in movies:
            yield{"name":name,
                  "movie":movie}