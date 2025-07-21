# 🚚 Logistics Delay Prediction API

A production-grade FastAPI microservice that predicts whether a delivery will be delayed or not, based on delivery distance, weather condition, and time of day.  
This project is built to attract logistics companies by showcasing how ML can drive smarter delivery decisions.

---

## 🛠️ Tech Stack

![for-the-badge](https://img.shields.io/badge/BACKEND-FastAPI-blue?style=for-the-badge&logo=fastapi)
![for-the-badge](https://img.shields.io/badge/MODEL-DecisionTree-yellow?style=for-the-badge)
![for-the-badge](https://img.shields.io/badge/SERIALIZATION-Joblib-orange?style=for-the-badge)
![for-the-badge](https://img.shields.io/badge/DEPLOYMENT-Render-purple?style=for-the-badge)
![for-the-badge](https://img.shields.io/badge/ML-Pandas%20%7C%20Sklearn%20%7C%20Numpy-green?style=for-the-badge)

---

## 🧠 Machine Learning Overview

| Component       | Details                             |
|----------------|--------------------------------------|
| Model Type      | Decision Tree Classifier             |
| Problem Type    | Binary Classification (Yes/No)       |
| Output          | `Delayed`: "Yes" or "No"             |
| Input Features  | `DistanceKM`, `Weather`, `TimeOfDay` |
| Preprocessing   | Label Encoding for Categorical Vars  |
| Dataset Format  | Custom `.json` mock logistics data   |

---

<pre><code>## 📁 Project Structure

logistics-delay-api/
├── app/
│   ├── main.py         # FastAPI app with all routes
│   ├── model.py        # Model loading & prediction logic
│   ├── schema.py       # Pydantic models for request/response
│   └── utils.py        # (Optional) helper functions
├── delivery_data.json  # Mock dataset used for training
├── model.pkl           # Trained Decision Tree Classifier
├── encoders.pkl        # LabelEncoders for input/output values
└── README.md           # You're reading it
</code></pre>

<pre><code>## 🔗 API Endpoints

📍 GET /
  └── Description : Health check route
  └── Response :
        {
          "message": "Logistics Delay Prediction API is live 🔥"
        }

📍 POST /predict-delay
  └── Description : Predict if a delivery will be delayed
  └── Request Body :
        {
          "DistanceKM": 45.0,
          "Weather": "Rainy",
          "TimeOfDay": "Evening"
        }

  └── Response :
        {
          "delay_prediction": "Delayed"
        }
</code></pre>

<pre><code>## 👨‍💻 Author

Made with ❤️ by [Chirag](https://github.com/your-github-username)

- 🚀 BCA Student | Aspiring Data Scientist
- 🛠️ Passionate about building real-world ML + Fullstack projects
- 🧠 Believer in project-based learning & practical problem solving
- 📫 Reach me at: beingchirag6@gmail.com
</code></pre>