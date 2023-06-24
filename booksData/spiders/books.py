import pymongo
from pymongo import MongoClient
import datetime 

import scrapy
from pathlib import Path

client = MongoClient("mongodb+srv://test-data-scraping:Parmar-123@data-scraping.pksegyo.mongodb.net/")

db = client.BooksData            # Books is our collection name

def insertToDB (page, title, image, rating, price, inStock):
    collection = db[page]
    doc = {
        "title": title, "image": image, "rating":rating, "price":price, "inStock": inStock,
        "date": datetime.datetime.utcnow()
    }
    inserted = collection.insert_one(doc)
    return inserted.inserted_id

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrap.com"]
    start_urls = ["https://toscrap.com"]

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        bookdetail = {}
        # Save content as file
    
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        cards = response.css(".product_pod")
        for card in cards:
            title = card.css("h3>a::text").get()
            # print(title) 
            image = card.css(".image_container img")
            # print(image.attrib["src"]) 
            
            rating = card.css(".star-rating").attrib["class"].split(" ")[1]
            # print(rating) 

            price = card.css(".price_color::text").get()
            # print(price) 

            availablity = card.css(".availability")
            if len(availablity.css(".icon-ok"))>0:
                inStock = True
            else:
                isStock = False
            
            # print(inStock) 
            insertToDB(page, title, image.attrib["src"].replace("../../../../media", "https://books.toscrape.com/media"), rating, price, inStock );