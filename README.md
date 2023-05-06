# SpamAssassin


SpamAssassin is a sophisticated Machine Learning project designed to detect spam messages with high accuracy. The project employs the latest advancements in Natural Language Processing and Machine Learning techniques to achieve an efficient classification of incoming messages.

The project utilizes a pre-trained deep learning model called Roberta, which has been shown to deliver high accuracy in many Natural Language Processing tasks. To build this project, a combination of publicly available spam datasets from different sources was collected, including SMS, email, and Twitter spam datasets. The dataset was carefully curated and preprocessed to ensure high data quality, and then split into training and testing sets.

To prepare the dataset for training, the data is preprocessed and tokenized. The encodings and labels are stored as features, and these features are then used to train the model. The newly trained model is optimized and converted to ONNX format, which is a popular format for deploying machine learning models. The model is then tested and compared with the old training to ensure that the new model exceeds the old model's performance. If the new model performs better, the old model asset is replaced with the new one.

The entire training pipeline is designed to be reproducible as the pipeline is defined. The dataset and the model assets are also version controlled, which ensures that the project is highly traceable and can be audited. This is essential for any project that involves sensitive data, such as messages.

Once the model is ready, it is hosted in the cloud, AWS Lambda to be precise. AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. The web application that allows users to input messages is hosted on an EC2 server, which is a scalable cloud computing service.

This project showcases the power of Machine Learning in real-life applications. The SpamAssassin project can be integrated into any system that requires monitoring of fraudulent activities. For instance, this system can be integrated into banking systems to detect fraudulent transactions or email systems to protect against phishing attacks. The possibilities are endless, and the only limitation is the imagination.
