# TweetSentinel: Disaster News Checker

TweetSentinel is an advanced machine learning-based system that uses the "Natural Language Processing with Disaster Tweets" dataset from Kaggle to detect whether news posted on Twitter is real or fake. With the increasing amount of fake news circulating on social media platforms, the TweetSentinel project aims to provide an accurate and efficient solution for businesses and individuals to distinguish between genuine news and fabricated stories.

The methodology behind TweetSentinel involves preprocessing and tokenizing the dataset to create encodings and labels for the model. The model is then trained using these features with the help of a state-of-the-art language model. The training dataset is split into training and testing sets to evaluate the model's performance.

Once the model is trained, it is optimized and deployed on AWS Lambda, a highly scalable and cost-effective compute service that allows developers to run code without managing servers. The web app, which enables users to input tweets, is hosted on an EC2 server.

When a user inputs a tweet, the web app sends a request to the AWS Lambda function, which uses the TweetSentinel model to determine whether the tweet is real or fake news. The result is then returned to the web app, which displays the output to the user. The TweetSentinel system can be integrated with almost anything to monitor tweets, making it a versatile and useful tool for businesses and individuals alike.

In conclusion, TweetSentinel is a prime example of how machine learning can be used to solve real-world problems. By leveraging powerful language models and the Kaggle dataset, the project has created a highly accurate and efficient system to detect real vs. fake news on Twitter. With its reproducible training pipeline and deployment on AWS Lambda, the TweetSentinel project is a valuable asset for anyone seeking to combat the spread of fake news on social media platforms.