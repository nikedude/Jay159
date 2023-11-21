from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
	name = "Lifts"
	start_urls = [
		"https://digital.jaypeakresort.com/conditions/snow-report/snow-report/",
		]

	def parse(self, response):
		for Lifts in response.css("article.SnowReport-Lift"):
			yield {
				"liftname": Lifts.css("h3.SnowReport-feature-title::text").get(),
				"liftstatus": Lifts.css("span.SnowReport-item-status .SnowReport-sr-label::text").get(),
			}