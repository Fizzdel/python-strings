reviews = [ 
     "This product is really good. I'm impressed with its quality.",
     "The performance of this product is excellent. Highly recommended!",
     "I had a bad experience with this product. It didn't meet my expectations.",
     "poor quality product. Wouldn't recommend it to anyone.",
     "The product was average. Nothing extraordinary about it."]
keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for review in reviews:
    modified_review = review
    for keyword in keywords:
        modified_review = modified_review.replace(keyword, keyword.upper())
        modified_review = modified_review.replace(keyword.capitalize(), keyword.upper())
    print(modified_review)

    
def tally_sentiments(reviews):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        for word in positive_words:
            if word in review:
                word.lower()
                positive_count += 1
    for review in reviews:
        for word in negative_words:
            if word in review:
                word.lower()
                negative_count += 1

    return {"positive": positive_count, "negative": negative_count}

# Run the function and print the result
result = tally_sentiments(reviews)
print("Sentiment Tally:")
print(f"Positive words: {result['positive']}")
print(f"Negative words: {result['negative']}")