from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY")

def generate_answer(context, query):

    prompt = f"""
    Use travel data below:

    {context}

    User request:
    {query}

    Generate optimized itinerary.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content