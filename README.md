# Real-Time Fraud Detection System

## Team: Code Hackerz

* Arushi Jain
* Jasmitha Lokesh
* Gnana Prasuna M
  
  *College*: SRM Institute of Science & Technology, Kattankulathur, Chennai
  *Theme*: AI for Core Applications

---

## Problem Statement

With the increasing number of online financial frauds, traditional fraud detection systems are:

* *Delayed & reactive* – fraud detected after the event.
* *Vulnerable* – rule-based systems are easy to bypass.
* *Costly* – financial losses & reduced customer trust.

There is a need for a *real-time, scalable, and accurate fraud detection system*.

---

## Objectives

* Detect fraudulent transactions instantly.
* Reduce false positives & negatives.
* Ensure scalability for high transaction volumes.
* Protect customers & improve trust.

---

##  Limitations of Existing Systems

* Rule-based systems are static & easy to exploit.
* Post-event fraud detection is “too late”.
* High false alarms inconvenience genuine users.
* Poor adaptability to new fraud patterns.

---

## Proposed Solution

An *AI/ML-powered fraud detection engine* with:

* Real-time monitoring of transactions.
* Adaptive learning models to detect emerging fraud patterns.
* Seamless integration with banking & payment systems.

---

## System Architecture

1. *Data Ingestion* → Transaction details (amount, location, device, time).
2. *Feature Engineering* → Behavioral & historical data.
3. *Machine Learning Model* → Supervised + unsupervised learning.
4. *Real-Time Scoring* → Predict fraud likelihood.
5. *Alert System* → Notify banks/customers instantly.

---

## Technology Stack

* *Backend & Logic*: Python (Flask / FastAPI)
* *Machine Learning*: Pandas, NumPy, Scikit-learn, Joblib
* *Database*: SQLite
* *Frontend/Dashboard*: HTML, CSS, JavaScript

---

## Impact

* Significant reduction in fraud-related financial losses.
* Increased customer trust & satisfaction.
* Strengthened financial ecosystem security.
* Scalable solution for banks, fintechs, and e-commerce platforms.

---


## Installation & Setup

bash
# Clone the repo
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate    # (Linux/Mac)
venv\Scripts\activate       # (Windows)

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py


---
