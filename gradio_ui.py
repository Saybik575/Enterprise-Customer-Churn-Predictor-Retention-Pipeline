import gradio as gr
import requests

def evaluate_retention(
    gender, senior_citizen, partner, dependents, phone_service, multiple_lines,
    internet_service, online_security, online_backup, device_protection,
    tech_support, streaming_tv, streaming_movies, tenure, contract,
    paperless_billing, payment_method, monthly_charges, total_charges
):
    # Construct the payload exact data schema expected by FastAPI
    payload = {
        "gender": gender, "SeniorCitizen": int(senior_citizen), "Partner": partner, "Dependents": dependents,
        "PhoneService": phone_service, "MultipleLines": multiple_lines, "InternetService": internet_service,
        "OnlineSecurity": online_security, "OnlineBackup": online_backup, "DeviceProtection": device_protection,
        "TechSupport": tech_support, "StreamingTV": streaming_tv, "StreamingMovies": streaming_movies,
        "tenure": int(tenure), "Contract": contract, "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method, "MonthlyCharges": float(monthly_charges), "TotalCharges": float(total_charges)
    }
    
    try:
        # Hit our background FastAPI endpoint
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()
        
        prob = result["churn_probability_score"]
        strategy = result["automated_retention_strategy"]
        
        # Format a clean string output for the UI
        risk_status = "🚨 HIGH RISK" if prob >= 0.5 else "✅ STABLE ACCOUNT"
        return f"Risk Assessment: {risk_status}\nCalculated Churn Probability: {prob * 100:.2f}%\n\nPrescribed Action:\n{strategy}"
        
    except Exception as e:
        return f"Error connecting to FastAPI backend. Ensure the server thread is running! Detals: {e}"

# Build the Gradio Input Layout Interface
inputs = [
    gr.Dropdown(["Male", "Female"], label="Gender"),
    gr.Dropdown(["0", "1"], label="Senior Citizen"),
    gr.Dropdown(["Yes", "No"], label="Partner"),
    gr.Dropdown(["Yes", "No"], label="Dependents"),
    gr.Dropdown(["Yes", "No"], label="Phone Service"),
    gr.Dropdown(["No phone service", "No", "Yes"], label="Multiple Lines"),
    gr.Dropdown(["DSL", "Fiber optic", "No"], label="Internet Service"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Online Security"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Online Backup"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Device Protection"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Tech Support"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Streaming TV"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Streaming Movies"),
    gr.Slider(0, 72, value=12, step=1, label="Tenure (Months)"),
    gr.Dropdown(["Month-to-month", "One year", "Two year"], label="Contract Type"),
    gr.Dropdown(["Yes", "No"], label="Paperless Billing"),
    gr.Dropdown(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], label="Payment Method"),
    gr.Slider(18.0, 120.0, value=65.0, label="Monthly Charges ($)"),
    gr.Number(value=780.0, label="Total Charges ($)")
]

# Assemble interface
demo = gr.Interface(
    fn=evaluate_retention,
    inputs=inputs,
    outputs=gr.Textbox(label="Retention Engine Output Analysis", lines=6),
    title="📊 Enterprise Customer Churn Dashboard (Gradio)",
    description="Adjust customer traits to calculate real-time churn risk and view automated response strategies."
)

if __name__ == "__main__":
    # Launch with share=True to generate a public link natively!
    demo.launch(share=True)
