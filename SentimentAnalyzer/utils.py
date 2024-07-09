import pandas as pd
import io
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import pos_tag
import nltk
nltk.download('punkt')


# Load the dataset
df = pd.read_csv("/Users/ashikalhabib/Desktop/test/merger_v2.csv")


def analyze_product_reviews(product_id):
    product_reviews = df[df['P_ID'] == product_id]
    if product_reviews.empty:
        return f"No reviews found for product ID: {product_id}"
    reviews_text = ' '.join(product_reviews['Review'].astype(str))
    tokens = word_tokenize(reviews_text)
    pos_tags = pos_tag(tokens)
    adjectives = [word for word, pos in pos_tags if pos in ['JJ', 'JJR', 'JJS']]
    stop_words = set(stopwords.words('english'))
    adjectives = [adj for adj in adjectives if adj.lower() not in stop_words]
    if not adjectives:
        return f"No adjectives found in the reviews for product ID: {product_id}"
    sia = SentimentIntensityAnalyzer()
    good_adjectives = []
    bad_adjectives = []
    for adj in adjectives:
        sentiment = sia.polarity_scores(adj)
        if sentiment['compound'] > 0:
            good_adjectives.append(adj)
        elif sentiment['compound'] < 0:
            bad_adjectives.append(adj)
    good_count = len(good_adjectives)
    bad_count = len(bad_adjectives)
    if good_count > bad_count:
        overall_sentiment = "Good"
    elif bad_count > good_count:
        overall_sentiment = "Bad"
    else:
        overall_sentiment = "Neutral"
    return {
        'Product ID': product_id,
        'Good Adjectives Count': good_count,
        'Bad Adjectives Count': bad_count,
        'Overall Sentiment': overall_sentiment,
        'Good Adjectives': good_adjectives,
        'Bad Adjectives': bad_adjectives
    }


def generate_word_cloud(words, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
    buffer = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title, fontsize=20)
    plt.axis('off')
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    return f"data:image/png;base64,{img_str}"