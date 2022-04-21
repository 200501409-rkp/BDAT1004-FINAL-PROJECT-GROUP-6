<img src="https://user-images.githubusercontent.com/98443528/164374315-315a05fd-98f4-402d-bd1f-24511c16f5b9.png" alt="Barrie Weather Logo" width="80" height="80" style="display:inline;" align="left">

# BDAT1004 FINAL PROJECT GROUP 6

![GitHub last commit](https://img.shields.io/github/last-commit/200501409-rkp/BDAT1004-FINAL-PROJECT-GROUP-6?color=red&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/200501409-rkp/BDAT1004-FINAL-PROJECT-GROUP-6?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/200501409-rkp/BDAT1004-FINAL-PROJECT-GROUP-6?color=lightcoral&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/200501409-rkp/BDAT1004-FINAL-PROJECT-GROUP-6?color=blueberry&style=for-the-badge)

<br>

## Table of Contents
- [About Project 📂](#about-project)
- [Installation and Setup 💻](#installation-and-setup)
- [Snapshots 📸](#snapshots)
- [Live Website 🌐](#live-website)

<br>

---

<br>

## About Project

### **Barrie Weather** <img src="https://user-images.githubusercontent.com/98443528/164374315-315a05fd-98f4-402d-bd1f-24511c16f5b9.png" alt="Barrie Weather Logo" width="26" height="26" style="display:inline;">

> The project aims to provide the minutely and hourly weather updates of ***Barrie***, Ontario.


* Group Number - **6**
* Team Members
  * Ravi Kant Pujari
  * Khushboo Jaikishan Kodwani
  * Nikita Dhingra
  * Gowripriya Ginnam

<br>

---

<br>

## Installation and Setup

####  We recommend you to create a ***virtual environment***.

<br>

* Clone this repository

  ```bash
  git clone https://github.com/200501409-rkp/BDAT1004-FINAL-PROJECT-GROUP-6.git
  ```

* Install ```virtualenv```, ignore this if you already have installed it
  ```
  pip install virtualenv
  ```

* Creating a virtual environment
  ```
  python -m venv venv
  ```

* Activating a virtual environment
  #### - Windows Users
  ```
  .\env\Scripts\activate
  ```
  #### - Unix/macOS Users
  ```
  source env/bin/activate
  ```

* Install requirements with ```pip```

  ```
  pip install -r requirements.txt
  ```

* Create a new file **.env** ([dot]env) and add following:
  ```
  FLASK_DEBUG=True
  FLASK_ENV=development
  FLASK_APP=flaskr.app.py
  MONGODB_USER=barrieweatheruser
  MONGODB_PASS=barrieweatherpass
  ```

* To run the project
  ```
  flask run
  ```
  OR
  ```
  flask run -p [port-number]
  ```

<br>

---

<br>

## Snapshots

<br>

* Homepage - Laptop/Desktop View
  
  <br>

  ![2](https://user-images.githubusercontent.com/98443528/164378857-e869cad2-9d67-4b33-9d1c-1f64b9eccd1d.png)

<br>

* Homepage - Mobile View
  
  <br>

  ![3](https://user-images.githubusercontent.com/98443528/164380358-80a08f6f-f946-442d-a9cc-aac7439a8a58.png)

<br>

---

<br>

## Live Website

   - This website is hosted on ***Heroku*** and open it by <a style="display:inline" href="http://bdat1004-openweatherapp.herokuapp.com/" target="_blank">clicking here</a>.

<br>

---

<br>

## Thank You 🙏🏻😊👍🏻
  - Thank you so much for reading the project documentation.

<br>

![](https://visitor-badge.glitch.me/badge?page_id=200501409-rkp.BDAT1004-FINAL-PROJECT-GROUP-6)