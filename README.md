# 🎬 Movie Recommendation System

A Movie Recommendation System built with **Python, MySQL, Pandas, Scikit-learn, and Streamlit** using **Collaborative Filtering** to recommend movies based on user preferences.


## 📌 Project Overview

This project recommends movies to users by analyzing rating patterns using Collaborative Filtering. The application uses the MovieLens dataset, stores data in MySQL, processes it with Pandas and Scikit-learn, and provides recommendations through a Streamlit web application.


## ✨ Features

- User-based Collaborative Filtering
- Movie recommendations based on similar users
- MySQL database integration
- Interactive Streamlit web interface
- Uses the MovieLens dataset
- Simple and easy-to-use UI


## 🛠️ Tech Stack

- **Programming Language:** Python 3.14
- **Frontend:** Streamlit
- **Database:** MySQL
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn
- **Version Control:** Git & GitHub

## 📂 Project Structure

movie-recommendation-system/
│── app.py
│── recommend.py
│── load_data.py
│── queries.sql
│── requirements.txt
│── README.md
│── .gitignore
│── movies.csv
│── ratings.csv
│── links.csv
│── tags.csv


## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/danish-mehmood1/movie-recommendation-system.git
```

### 2. Move into the project folder

```bash
cd movie-recommendation-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a database named:

```sql
movie_recommender
```

Run the SQL script:

```sql
queries.sql
```

### 5. Load the dataset

```bash
python load_data.py
```

### 6. Start the application

```bash
streamlit run app.py
```


## 📊 Dataset

This project uses the MovieLens Small Dataset provided by GroupLens Research.

Dataset includes:

- 100,836 Ratings
- 9,742 Movies
- 610 Users
- 3,683 Tags


## 🚀 Future Improvements

- Content-Based Recommendation
- Hybrid Recommendation System
- User Login System
- Movie Posters
- Search Movies
- Deploy on Streamlit Cloud
- Better UI Design


## 👨‍💻 Author

**Danish Mehmood**

GitHub:
https://github.com/danish-mehmood1