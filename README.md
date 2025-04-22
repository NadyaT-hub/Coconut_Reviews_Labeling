# Review Processing

You are a growth analyst at a Vancouver-based consulting firm called [Bernardino Group](https://en.wikipedia.org/wiki/Bernardino_of_Siena#:~:text=Saint%20Bernardino%20is%20the%20Roman,problems%20involving%20the%20chest%20area.). Your manager is spear-heading the completion of a new analytical tool which will automatically label if a review is positive, neutral, negative, or irrelevant (aka [sentiment](https://en.wikipedia.org/wiki/Sentiment_analysis)). The release schedule for this product is ambitious as your company would like to be able to advertise this service to potential clients as soon as possible. You will be kicking off the completion of this first milestone by independently implementing a minimal-viable product. This will be a Python pipeline that ingests review data and interfaces with the Open AI API to automatically label each review.

For example, if you were checking the reviews for a wearable ring from SengLinks that tracks heart rate, the following would be examples of the mentioned sentiment:
* positive: *I love this ring, I use it all the time when working out.*
* neutral: *It's an ok ring. Some features could be better but for the price it's fine.*
* negative: *Absolutely terrible ring. The green light that the ring emitted kept attracting mosquitos.*
* irrelevant: *I like strawberry ice cream because its the best.* 

You are tasked with creating a minimal pipeline that reads a JSON file of reviews and generates an output file that contains one of these sentiment labels for each respective review.

For example, if your input file contains the following array of reviews:
```
[
 "this ring smells weird, don't recomend",
 "I love this ring, I use it all the time when working out.",
 "I will never buy another brand again, I love this ring",
 "It's an ok ring. Some features could be better but for the price its fine.",
 "its a ring",
 "Bought this ring and it came broken. rip-off."
]
```

Your program would output the following list of labels:
```
["negative", "positive", "positive", "neutral", "irrelevant", "negative"]
```

