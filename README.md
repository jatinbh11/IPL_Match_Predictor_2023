# IPL Win Probability Predictor

A machine learning project to predict the win probability of an IPL (Indian Premier League) match based on real-time match conditions.

## 🚀 Overview
This project aims to predict the probability of a team winning an IPL match using various input parameters such as the current score, overs completed, wickets lost, and match venue.

## 📌 Features
- Predicts the **winning probability (%)** of the batting team.
- Uses **real-time match data** as input.
- Implements **machine learning algorithms** for accurate predictions.
- Preprocessed IPL match dataset for training.

## 🎯 Input Parameters
- **Batting Team** 🏏 (e.g., Mumbai Indians, Chennai Super Kings)
- **Bowling Team** 🏏
- **Host City** 📍
- **Target Score** 🎯
- **Current Score** 🏆
- **Overs Completed** ✅
- **Wickets Out** ❌

## 📊 Output
The model predicts the **winning probability (%)** of the batting team based on the input conditions.

## 🏗️ Tech Stack
- **Python** 🐍
- **Scikit-Learn** 🤖
- **Pandas & NumPy** 📊
- **Matplotlib & Seaborn** 📉
- **Flask** *(for deployment)* 🌐

## 📂 Dataset
The dataset consists of historical IPL match data, including team performances, match locations, scores, and outcomes. The data was cleaned and preprocessed for training.

## ⚙️ Model Training
- Applied **classification algorithms** (Logistic Regression, Decision Trees, Random Forest, etc.).
- Used **feature engineering** to extract important insights.
- Evaluated performance using **accuracy, precision, recall, and AUC-ROC scores**.


## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ipl-win-probability-predictor.git
   cd ipl-win-probability-predictor
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the model:**
   ```bash
   python main.py
   ```
4. **Deploy with Streamlit (Optional):**
   ```bash
   flask run app.py
   ```

## 🎯 Future Improvements
- Enhance dataset with **more historical match details**.
- Integrate **Deep Learning models** for better accuracy.



