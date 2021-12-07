Scrapy is a Python framework for large scale web scraping. 
It gives you all the tools you need to efficiently extract data from websites, process them as you want, and store them in your preferred structure and format.

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19oQcz6XszWJNUpXBbaQIIo7dtpex4pQ4?usp=sharing)


Steps that will help you scrape web page:

1) Install scrapy directly with:
>pip install scrapy

2) Make new scrapy project:
> !scrapy startproject spider_name

3) Save data in csv file:
>!scrapy crawl spider_name -O file_name.csv

4) Display saved data from csv file via pandas:
>import pandas as pd
>data = pd.read_csv('file_name.csv')
>data.head()
