# Dog_cat-Image-Classification
TEST PYTHON

This project is a small-scale image classification application implemented in Python, focused on distinguishing between images of cats and dogs.

## Overview

The project consists of two main Python scripts:

- `main.py`: The primary script for running the image classification tasks.
- `model_1.py`: Contains the `ImageClassifier` class, which handles data loading, feature extraction, training, and prediction.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- scikit-learn (`scikit-learn`)
- Matplotlib (`matplotlib`)

You can install these dependencies using pip:

```bash
pip install numpy opencv-python scikit-learn matplotlib
```

## Usage
1. Clone the repository to your local machine.
2. Ensure all dependencies are installed.
3. Run the main.py script to train the classifier and make predictions.

## Project Structure
- main.py: Contains the main functionality of the project, including data loading, model training, and prediction.
- model_1.py: Defines the ImageClassifier class responsible for handling image data and classification tasks.

## Dataset
The dataset is expected to be structured as follows:

```bash
project_root/
|_ input/
   |_ train_frames/
      |_ train/
         |_ cat/
            |_ cat001.png
            |_ cat002.png
            |_ ...
         |_ dog/
            |_ dog001.png
            |_ dog002.png
            |_ ...
```
Images of cats are expected to be stored in the cat folder, and images of dogs in the dog folder within the train directory.

## Model Training

The image classifier utilizes the Random Forest algorithm implemented in scikit-learn. Random Forest is an ensemble learning method that operates by constructing a multitude of decision trees during training and outputting the class that is the mode of the classes (classification) of the individual trees.

## License
NONE :)

