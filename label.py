from openai import OpenAI


def get_sentiment(text: list) -> str:
    """
    Labels each review in a list as positive, neutral, negative, or irrelevant using GPT.
    Returns a newline-separated string of labels.
    """
    from openai import OpenAI
    client = OpenAI()


    system_prompt = """
    You were the 2024's best reviews labeler in the US. Now you need to prove that you're still great at it 
    and label 50 reviews of the ZICO Coconut Water.
    If you don't complete this assignment correctly, you will lose your title and your job. 
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": """
For each line of text in the string below, please categorize the review
as either positive, neutral, negative, or irrelevant.
Label each review as positive, negative, neutral or irrelevant.
Example of a positive review: I love this coconut water. I like ZICO coconut water. Will order again.
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
