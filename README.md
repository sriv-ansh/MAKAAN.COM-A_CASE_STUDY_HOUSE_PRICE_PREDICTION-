# 🏠 Makaan.Com -:(A-CASE-STUDY) Housing Price Prediction 🏡

Welcome to the Indian Housing Price Prediction project! This project leverages machine learning to predict housing prices based on various 
features such as house type, size, city, status (furnished, semi-furnished, unfurnished), and location. The project is built using Flask for the web application
and scikit-learn for the machine learning model.

## 📂 Project Structure

- `app.py`: Main Flask application file.
- `templates/`: Contains the HTML templates (`index.html` and `result.html`).
- `Feature Scaling File/`: Contains the pre-trained MinMax scaler, OneHot encoder, and location dictionary.
- `Model_File/`: Contains the trained machine learning model.
- `static/`: Contains any static files such as CSS or JavaScript.

## 🛠️ Prerequisites

- Python
- Flask
- Pandas
- scikit-learn
- Pickle
- JSON
- Numpy
- Seaborn

## 🚀 Setup

1. Clone the repository:
    ```bash
    https://github.com/sriv-ansh/MAKAAN.COM-A_CASE_STUDY_HOUSE_PRICE_PREDICTION
    cd house-price-prediction
    ```
2. Navigate to the project directory:
    ```bash
    cd house-price-prediction
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🌐 Usage

1. Start the Flask application:
    ```bash
    python app.py
    ```
2. Open a web browser and go to `http://127.0.0.1:5001/`.
3. Fill in the form with the required details and submit.
4. View the predicted housing price on the result page.

## 📊 Data Logging

The application logs the file path and the last modification date of the input files into a CSV file for tracking purposes.

## 🧠 Model Training

1. **Data Cleaning**: Cleaned the data to remove any inconsistencies or missing values.
2. **Feature Scaling**: Applied MinMax scaling to normalize the features.
3. **Model Initialization**: Trained various models including Lasso, Ridge, ElasticNet, and Linear Regression.
4. **Hyperparameter Tuning**: Used GridSearchCV to find the best parameters.
5. **Cross-Validation**: Performed cross-validation to evaluate model performance, achieving a maximum accuracy of 72% and a minimum of 65%.
6. **Feature Selection**: Selected the best features for the model.

## 🌍 Deployment

- **Frontend**: Built with Flask.
- **Deployment**: Deployed on Render (free version), with a maximum loading time of 52 seconds.
- **Features**: Initialized different locations within the application.

## 🏙️ Dataset

Includes data from three major cities: Delhi, Mumbai, and Pune.

## 📖 Case Study: House Price Prediction

### Objective

To predict housing prices for a real estate company to help them set competitive prices and understand market trends.

### Methodology

1. **Data Collection**: Collected historical housing price data from various sources including online real estate portals and government records.
   The data has been scraped using BeautifulSoup/Web Scraping from Makaan. If you want to learn more, you can visit their [website](https://www.makaan.com).
3. **Data Preprocessing**: Cleaned and preprocessed the data by handling missing values, encoding categorical variables, and scaling numerical features.
4. **Model Training**: Trained multiple regression models to predict housing prices and evaluated their performance using cross-validation.
5. **Feature Engineering**: Engineered additional features such as proximity to amenities, crime rates, and average income in the area.
6. **Deployment**: Deployed the best-performing model using Flask and made it accessible through a web interface.

### Results

- The model achieved an accuracy range between 65% to 72% on cross-validation.
- The web application allows users to input details and get real-time predictions of housing prices.
- The company was able to use these predictions to better understand market trends and price their properties more competitively.

### Conclusion

This project successfully demonstrates how machine learning can be applied to predict housing prices with a reasonable accuracy.
The model and web application provide valuable insights that can assist real estate companies in making informed decisions.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.
