import json
import re

class Product:
    def __init__(self):
        self.__averageRating = None
        self.__images = []
        self.__meetingPoint = ""

    def set_averageRating(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Average rating must be a number")
        if not(0 <= value <= 5):
            raise ValueError("Average rating cannot be less than 0 nor more than 5")
        self.__averageRating = float(value)

    def set_images(self, value):
        if not isinstance(value, list):
            raise ValueError("The images must be in a list")
        for url in value:
            if not isinstance(url, str):
                raise ValueError("Each url must be a string")
        self.__images = value

    def set_meetingPoint(self, value):
        if not isinstance(value, str):
            raise ValueError("Meeting point must be a string")
        self.__meetingPoint = value

    def toJSON(self):
        product_data = {
            "averageRating": self.__averageRating,
            "images": self.__images,
            "meetingPoint": self.__meetingPoint
        }
        return json.dumps(product_data, indent=1)
    
    def calculateAverageRating(reviews):
        total_reviews = reviews["totalReviews"]
        review_totals = reviews["reviewCountTotals"]
        valuation_sum = 0

        for valuation in review_totals:
            valuation_sum += (valuation["rating"] * valuation["count"])

        return round(valuation_sum / total_reviews, 2)

    def extractLargestImages(productImages):
        largestImagesUrls = []

        for img in productImages:
            variants = img.get("variants")

            if variants:
                max_width = 0

                for variant in variants:
                    if variant["width"] > max_width:
                        max_width = variant["width"]
                        largest_variant = variant

                largestImagesUrls.append(largest_variant["url"])

        return largestImagesUrls
    
    def extractMeetingPoint(description):
        pattern = r"Meeting point:\s*(.*?)(\n|$)"
        match = re.search(pattern, description)

        if match:
            meeting_point = match.group(1).strip() 

        if not meeting_point[0].isupper():
            meeting_point = meeting_point.capitalize()
        
        return meeting_point

    def parseProduct(productData):
       productInstance = Product()

       if "reviews" in productData:
        averageRating = Product.calculateAverageRating(productData["reviews"])
        productInstance.set_averageRating(averageRating)

       if "images" in productData:
        largestImages = Product.extractLargestImages(productData["images"])
        productInstance.set_images(largestImages)

       if "description" in productData:
        meetingPoint = Product.extractMeetingPoint(productData["description"])
        productInstance.set_meetingPoint(meetingPoint)

       return productInstance 


with open("product.json", errors="ignore") as file:
    data = json.load(file)
    productList = data['products']

activeProducts= []

for product in productList:
    if product['status'] == "ACTIVE":
        activeProducts.append(product)

parsedProducts = []

for product in activeProducts:
    parsed_product = Product.parseProduct(product)
    parsedProducts.append(parsed_product)
    
for parsed_product in parsedProducts:
    print(parsed_product.toJSON())