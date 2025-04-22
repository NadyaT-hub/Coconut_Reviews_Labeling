from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Opens the json file, reviews_only - drops any other data but results.
    """
    # open the json object
    with open(filepath, 'r') as file:
           data = json.load(file)


    # extract the reviews from the json file
    reviews_only = data['results']
    print(reviews_only)


    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews_only)
    make_plot(sentiments)
   


def get_sentiment(text: list) -> str:
    """
    Labels each review in a list as positive, neutral, negative, or irrelevant using GPT.
    Returns a newline-separated string of labels.
    """
    from openai import OpenAI
    client = OpenAI()


    system_prompt = """
    You were the 2024's best reviews labeler in the US. Now you need to prove that you're still great at it or you will get fired,
    and label Google reviews for ZICO coconut water.
    """


    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": """
For each line of text in the string below, please categorize the review
as either positive, neutral, negative, or irrelevant.
Label each review as positive, negative, neutral or irrelevant.
Example of a positive review: I love this coconut water. I like ZICO coconut water. My children like this coconut water. Will order again.
Example of a negative review: I don't like it. I like another water better. Contents taste like plastic.
Example of a neutral review: It was okay. It didn't do much for me.
Example of an irrelevant review: It's a water. It's a coconut water.
Use only a one-word response per line. Do not include any numbers.
"""},
            {"role": "user", "content": "\n".join(review.replace("\n", " ") for review in text)}
        ]
    )


    output = completion.choices[0].message.content.strip()
    print(output)
    return output
   
# plot a visualization expressing sentiment ratio
import matplotlib.pyplot as plt
from collections import Counter


def make_plot(sentiments: str):
    """
    Takes the sentiment labels (one per line) as a string,
    normalizes and filters them, and creates a bar chart.
    """
    # Valid sentiment labels
    valid_labels = {'positive', 'neutral', 'negative', 'irrelevant'}


    # Normalize each line, remove extra stuff, filter invalid entries
    sentiment_list = [
        line.strip().lower()
        for line in sentiments.strip().splitlines()
        if line.strip().lower() in valid_labels
    ]


    # Count valid sentiment labels
    sentiment_counts = Counter(sentiment_list)


    # Ensure all categories are present
    categories = ['positive', 'neutral', 'negative', 'irrelevant']
    counts = [sentiment_counts.get(cat, 0) for cat in categories]


    # Plotting
    plt.figure(figsize=(8, 5))
    bars = plt.bar(categories, counts, color=['green', 'gray', 'red', 'orange'])


    # Add value labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')


    plt.title("Sentiment Distribution of Coconut Water Reviews")
    plt.ylabel("Number of Reviews")
    plt.xlabel("Sentiment")
    plt.tight_layout()
    plt.savefig("images/sentiment_bar_chart.png")
    plt.show()


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))