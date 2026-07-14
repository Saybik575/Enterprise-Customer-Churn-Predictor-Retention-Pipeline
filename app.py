from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# 1. Initialize the FastAPI framework instance
app = FastAPI(title="Enterprise Customer Retention Engine", version="1.0")

# 2. Load the compiled machine learning pipeline into memory once when the server boots
with open('winning_churn_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# 3. Define the structural data schema expected by the endpoint
class CustomerPayload(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    tenure: int
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# 4. Create the operational POST endpoint for predictions
@app.post("/predict")
def predict_customer_churn(data: CustomerPayload):
    # Convert the incoming structured JSON payload into a pandas DataFrame format
    input_data = pd.DataFrame([data.dict()])
    
    # Extract the probability score for Churning (Class 1)
    churn_probability = pipeline.predict_proba(input_data)[0][1]
    
    # Implement automated routing logic based on financial risk thresholds
    if churn_probability >= 0.75:
        prescribed_action = "CRITICAL RISK: Route automatically to Premium Retention Team. Issue immediate 20% loyalty voucher."
    elif churn_probability >= 0.50:
        prescribed_action = "MEDIUM RISK: Flag account for automated email nurturing sequence and technical satisfaction check-in."
    else:
        prescribed_action = "LOW RISK: Standard operational status maintained. No intervention required."
        
    return {
        "churn_probability_score": round(float(churn_probability), 4),
        "automated_retention_strategy": prescribed_action
    }
