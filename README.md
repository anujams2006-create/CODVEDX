# ⚡ Utility Usage Prediction System

A Machine Learning-based web application developed using **Python, Flask, and Scikit-learn** to predict electricity utility bills based on units consumed. The application also provides complete CRUD (Create, Read, Update, Delete) functionality for managing utility usage records through a user-friendly web interface.

---

## 📌 Project Overview

The **Utility Usage Prediction System** is designed to help users estimate electricity bills by leveraging a Machine Learning model trained on historical usage data. In addition to bill prediction, the application allows users to maintain utility records efficiently through an intuitive dashboard.

This project demonstrates the integration of **Machine Learning** with **Flask Web Development**, making it suitable for academic learning and real-world applications.

---

## ✨ Features

- 🔐 Secure Login Page
- 📊 Dashboard with Utility Statistics
- ➕ Add New Utility Records
- 📋 View All Records
- ✏️ Edit Existing Records
- 🗑️ Delete Records
- 🤖 Machine Learning-Based Bill Prediction
- 📅 Separate Month and Year Selection
- 💰 Automatic Bill Amount Generation
- 📈 Dashboard Summary
- 🎨 Responsive User Interface

---

## 🛠️ Technologies Used

### Programming Language
- Python 3

### Backend
- Flask

### Machine Learning
- Scikit-learn
- Linear Regression

### Data Processing
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3
- Bootstrap

### Database
- CSV File (data.csv)

### Deployment
- Render

### Version Control
- Git & GitHub

---

## 📂 Project Structure

```
UtilityUsagePrediction/
│
├── app.py
├── model.py
├── data.csv
├── requirements.txt
├── runtime.txt
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── add.html
│   ├── edit.html
│   ├── view.html
│   └── predict.html
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/UtilityUsagePrediction.git
```

### 2. Navigate to Project Folder

```bash
cd UtilityUsagePrediction
```

### 3. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```bash
py -m pip install flask pandas numpy scikit-learn gunicorn
```

### 4. Run the Application

```bash
py app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔑 Login Credentials

Default Login

**Username**

```
admin
```

**Password**

```
admin123
```

*(Update these credentials in `app.py` if required.)*

---

## 📊 Machine Learning Model

The project uses the **Linear Regression Algorithm** from Scikit-learn.

### Workflow

- Load historical utility data
- Train Linear Regression model
- Predict electricity bill
- Display predicted amount

---

## 📁 Dataset

The dataset contains:

| Column | Description |
|---------|-------------|
| Month | Month and Year |
| Units_Used | Electricity Units Consumed |
| Bill_Amount | Electricity Bill |

Example

| Month | Units Used | Bill |
|--------|-----------:|-----:|
| January 2025 | 120 | 600 |
| February 2025 | 150 | 750 |
| March 2025 | 180 | 900 |

---

## 🚀 Future Enhancements

- SQLite/MySQL Database Integration
- User Authentication
- Charts and Graphs
- PDF Bill Generation
- Email Notifications
- Multiple Utility Types
- Monthly Usage Analytics
- Cloud Database Integration
- AI-Based Forecasting

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Flask Web Framework
- Machine Learning Integration
- Data Preprocessing
- CRUD Operations
- Model Training
- Web Development
- GitHub
- Deployment using Render
- Debugging and Problem Solving

---

## 💡 Challenges Faced

During development, several practical challenges were encountered:

- Fixing Machine Learning prediction accuracy
- Handling CSV parsing errors
- Designing a responsive user interface
- Implementing CRUD functionality
- Managing Flask routing
- Resolving CSS loading issues
- Configuring deployment on Render
- Solving dependency and package compatibility problems
- Debugging runtime errors

Overcoming these challenges significantly improved debugging, development, and deployment skills.

---

## 📸 Screenshots

Add screenshots here.

- Login Page
- Dashboard
- Add Record
- View Records
- Edit Record
- Prediction Page

---

## 👩‍💻 Author

**Anuja Shelke**

Computer Engineering Student

KJ College of Engineering & Management Research

---

## 🙏 Acknowledgement

This project was developed as **Task 1** during the **CodVedX Internship Program**.

I sincerely thank **CodVedX** for providing an opportunity to apply Machine Learning concepts in a practical web application and enhance my technical skills through hands-on project development.

---

## 📄 License

This project is developed for educational and learning purposes.

---

⭐ If you found this project useful, don't forget to **Star** the repository!
