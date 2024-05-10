# import libaries
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# import model
from model_1 import ImageClassifier

if __name__ == "__main__":
    classifier = ImageClassifier(dataset_path=f"C:/Programming_Work/Project/Python/CuoiKy/dog_cat/input/train_frames/train")
    classifier.load_data()
    features = classifier.extract_features(f"C:/Programming_Work/Project/Python/CuoiKy/dog_cat/input/train_frames/train/cat/cat002.png")
    image_matrix = features.reshape(classifier.image_size) 
    # Display image
    plt.imshow(image_matrix, cmap='gray')
    plt.axis('off')
    plt.show()
    
    
    accuracy = classifier.train()
    print("Accuracy:", accuracy)
    # Example of using the trained classifier to predict a single image
    image_path_to_predict = f"C:/Programming_Work/Project/Python/CuoiKy/dog_cat/input/train_frames/train/cat/cat002.png"
    prediction = classifier.predict(image_path_to_predict)
    print("Prediction for", image_path_to_predict, ":", prediction)
    