# PIC16B-HW2

## Description

This is homework 2 (web scraping) for PIC16B, a web scraper using Scrapy to crawl from [*TMDB*](https://www.themoviedb.org/) all movies that the actors in one movie have participated in, 
and make a movie recommendation according to the number of shared actors in these movies.

Here is the link to my blog post for this project: [**Yuanting's HW2 Blog**](https://yuanting.quarto.pub/homework/posts/HW2/).
In the blog you can find a detailed description of the project and a guidance about how to run it.

## Guidance

- [**tmdb_spider.py**](https://github.com/YuantingPan/PIC16B-HW2/blob/main/TMDB_scraper/TMDB_scraper/spiders/tmdb_spider.py)

  This is the main spider file that performs the web-scraping. More descriptions can be found in my blog post.

- [**results.csv**](https://github.com/YuantingPan/PIC16B-HW2/blob/main/TMDB_scraper/results.csv)

  This is the samle result file after crawling the TMDB page of *Pulp Fiction*(https://www.themoviedb.org/movie/680-pulp-fiction)

- [**recommendation.ipynb**](https://github.com/YuantingPan/PIC16B-HW2/blob/main/TMDB_scraper/recommendation.ipynb)

  This is a jupyter notebook that presents the simple movie recommendation with the information gathered by spider.

