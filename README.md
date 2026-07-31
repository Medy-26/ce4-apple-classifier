# CE4: Fresh Apple vs Formalin-mixed Apple Classifier

GET 324 — Laboratory Exercise 10 (Mini-Project)
Group CE4 | Chemical Engineering

## Overview
This project trains a Convolutional Neural Network (CNN), using MobileNetV2
transfer learning, to classify apple images as either **Fresh** or
**Formalin-mixed**. The trained model is deployed as an interactive
Streamlit web application.

## Live App
🔗 **[(https://ce4-apple-classifier-od7r8ktrebqm5np3jhscfo.streamlit.app/)]**

## Dataset
- **Source:** FruitVision — A Benchmark Dataset for Fresh, Rotten, and
  Formalin-mixed Fruit Detection (Mendeley Data, 2025)
  https://data.mendeley.com/datasets/xkbjx8959c/2
- We used the "Fresh Apple" and "Formalin-mixed Apple" subsets for this
  binary classification task.
- License: CC BY-NC-ND 4.0 (used here for academic/non-commercial purposes only)

## Model
- Architecture: MobileNetV2 (pretrained on ImageNet) + custom classification head
- Framework: TensorFlow / Keras
- Input size: 224x224 RGB images
- Output: Binary classification (sigmoid), Fresh Apple vs Formalin-mixed Apple

## Repository Structure
```
├── app.py                  # Streamlit application
├── train_model.py          # Model training script (run in Google Colab)
├── ce4_apple_model.keras      # Trained model (add after training)
├── requirements.txt        # Python dependencies
├── report.md               # Project report
└── README.md
```

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## How to Use the App
1. Open the deployed app link (above).
2. Upload a clear image of an apple (JPG or PNG).
3. The app displays the prediction (Fresh or Formalin-mixed) with a
   confidence score.

## Deployment
Deployed on Streamlit Community Cloud (https://share.streamlit.io), connected
directly to this GitHub repository.

## Team Members
| Names| Reg Numbers | Usernames | Contribution  |
|------|---------------------|------------------|---------------|
| Ukpong,Medara Godson| _23/EG/CE/051_ | _Medy-26_ | Group Leader |
| Umohntuen, Mfoniso Amanam| _23/EG/CE/021_ | _mfon-iso_ | Model training |
| Archibong,Ekemini John| _23/EG/CE/101_| _ekemini756-wq_| App development |
| Robert Samuel Ukpong|23/EG/CE/041 |SammueL234 | Uploading the model |
| AniekanAbasi Linus| 23/EG/CE/081| aniekanlinus59 | researched for dataset |
| Abikpa , Joshua Gospel| 23/EG/CE/031 | joshua360-lgtm | Report writing |
| Anyim Divine Odinaka| 23/EG/CE/001 | anyimdivineodinaka| model taining |
| UTIP FAVOUR UWEM | 23/EG/CE/011 | utipfavour0-beep| Report writing |
| Nyong Unwana Eno | 23/EG/CE/091 | nyongunwana2-ctrl | Troubleshooting
## Course Learning Outcomes Addressed
- **CLO5:** Designed, trained, and evaluated a CNN (transfer learning) using
  TensorFlow/Keras for image data.
- **CLO7:** Deployed the trained model as a cloud-based web application using
  Streamlit, managed via Git/GitHub.
- **CLO8:** Documented the experimental procedure and results in this README
  and the accompanying project report.
