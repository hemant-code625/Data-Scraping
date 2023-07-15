<h1>Data Scraping using Scrapy and PyMongo</h1>

<h3> Welcome to the Data Scraping and Storage GitHub repository! 
This project focuses on utilizing the Scrapy web scraping framework to extract data of Travel and Mystery books from https://books.toscrape.com/index.html and storing it in a MongoDB Atlas database using PyMongo.
</h3>

<h2> Overview </h2>

![Screenshot 2023-06-24 134729](https://github.com/hemant-code625/Data-Scraping/assets/111212867/af3ff2a5-2845-4a68-adb4-df8010085521)

![Screenshot 2023-06-24 134828](https://github.com/hemant-code625/Data-Scraping/assets/111212867/c79e8d65-3b2d-478e-8b0c-f08cb6a31a67)


<p>This repository contains a Python script that demonstrates how to scrape book data from various websites using Scrapy. The scraped data is then processed and stored in a MongoDB Atlas database for further analysis and use. The script provides a flexible and efficient way to gather book-related information from online sources. </p>

<h2> Prerequisites: </h2>

<p> To run the script and replicate the project, you'll need the following: </p>
<ul> <li> Python 3.x </li>
  <li> Scrapy </li>
  <li> PyMongo </li>
  <li> MongoDB Atlas </li>
</ul>


Make sure to install the necessary dependencies using pip or any other package manager.

<h2> Usage </h2> 
<ol> <li> <p> Clone this repository to your local machine: </p> git clone https://github.com/your-username/book-data-scraping.git </li>
  <li> <p> Navigate to the project directory: </p> cd book-data-scraping </li>
  <li> Configure MongoDB Atlas: 
    <ul> 
    <li> Create a MongoDB Atlas account and set up a new cluster. </li> 
    <li> Obtain the connection string for your MongoDB Atlas cluster. </li> 
    <li> Update the MONGO_URI variable in the script with your connection string. </li> 
    </ul> 
  </li>

<li> Customize the scraping process: 
<ul> 
    <li> Open the book_scraper/spiders/books_spider.py file. </li> 
    <li> Modify the spider code to specify the websites to scrape, the data fields to extract, and the desired scraping logic. </li> 
    <li> Feel free to add more spiders or customize existing ones based on your requirements. </li> 
    </ul> 
</li>

<li> Run the scripts: </li>
scrapy crawl books

</ol>

<p> The script will start scraping the specified websites and store the scraped book data into your MongoDB Atlas database. </p>

<h2> Contributing </h2>
Contributions to this project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request. Let's make this project even better together.

<h2> License </h2>
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms and conditions of the license.

<h2> Acknowledgments </h2>
Special thanks to the developers of Scrapy and PyMongo for providing powerful tools that make web scraping and database integration seamless. Their contributions are invaluable to this project.

<p> If you have any questions or feedback, please don't hesitate to reach out. Happy scraping and data storage! </p>
