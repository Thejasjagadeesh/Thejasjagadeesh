# 🎬 Movie Magic – Cloud Based Movie Ticket Booking System

## 📌 Project Overview

Movie Magic is a smart cloud-based movie ticket booking application that allows users to browse movies, select seats, and confirm bookings online. The system is built using **Flask** and designed to be deployed on AWS cloud services.

The application provides a simple interface where users can register, log in, view available movies, choose seats, and receive booking confirmation.

---

## 🚀 Features

* User Registration
* User Login
* Browse Available Movies
* Seat Selection
* Ticket Booking Confirmation
* Simple and interactive UI
* Cloud-ready architecture

---

## 🛠 Technologies Used

* Python
* Flask
* HTML / CSS
* AWS EC2 (for deployment)
* AWS DynamoDB (database)
* AWS SNS (email notifications)

---

## 📂 Project Structure

```
movie-magic
│
├── app.py
├── config.py
├── requirements.txt
│
├── templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── movies.html
│   ├── book.html
│   └── confirmation.html
│
├── static
│   └── style.css
│
└── aws
    ├── dynamodb.py
    └── sns.py
```

---

## ▶ How to Run the Project

1. Install Python packages:

```
pip install flask boto3
```

2. Run the application:

```
python app.py
```

3. Open the browser and go to:

```
http://127.0.0.1:5000
```

---

## ☁ Cloud Architecture

The system is designed to work with the following AWS services:

* EC2 – Hosting the Flask application
* DynamoDB – Storing user and booking data
* SNS – Sending booking confirmation emails

---

## 👥 Team Members

Team Lead

* Thejas C J

Team Members

* Poorvi J Poojary
* Varun Kumar S
* Tejang Dandekar

---

## 📸 Demo

The application demonstrates a full movie ticket booking workflow including login, browsing movies, seat selection, and booking confirmation.

---


---
