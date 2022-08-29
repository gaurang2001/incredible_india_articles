# Incredible India Articles

This web scraper built on [`scrapy`](https://scrapy.org/) scrapes 100 articles from [www.incredibleindia.org](https://www.incredibleindia.org/) as a part of my IT458 Assignment.

### Pre-requisites

Install `scrapy`

```bash
pip install scrapy
```

Clone the repository and go to the directory

Create an `articles` folder

```bash
mkdir articles
```

### Crawling

Run the following to crawl articles from various categories (Code can be found in [regions.py](./incredible_india_articles/spiders/articles.py)) -

```bash
scrapy crawl articles
```

Update links under [`start_urls`](./incredible_india_articles/spiders/articles.py#L17) to fetch articles from different start points.

Run the following to crawl all "region" based articles (Code can be found in [regions.py](./incredible_india_articles/spiders/regions.py)) -

```bash
scrapy crawl regions
```
