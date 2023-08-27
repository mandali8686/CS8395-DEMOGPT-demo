# CS8395-DEMOGPT-demo


# Feature Extraction Application

## Description

This Streamlit application is designed to extract features from a given application description. The extracted features are displayed to the user, offering valuable insights into the key aspects of an application design.

## Dependencies

- `streamlit`
- `langchain`
- `tempfile`

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run `pip install -r requirements.txt` to install the required packages.

## How to Run

1. Open the terminal and navigate to the project directory.
2. Run `streamlit run <filename>.py` where `<filename>` is the name of the Python script.

## Features

- **Text Area for Description**: Users can input the description paragraph of an application.
- **Submit Button**: Once the description is entered, click the 'Submit' button to initiate the feature extraction process.
- **Display Features**: The extracted features will be displayed below the 'Submit' button.

## Functions

- `featureExtractor(description)`: This function takes in a description and returns the extracted features using the Langchain library and a GPT-3.5 Turbo model.

## Limitations

- The application uses the Langchain library, which may have API rate limits based on your subscription.
  
## Future Improvements

- Add support for additional language models.
- Improve the accuracy of feature extraction.

## License

This project is licensed under the MIT License.
