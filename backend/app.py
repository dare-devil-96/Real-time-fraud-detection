
### 2.3 `backend/app.py`
Create folder **backend**, then **app.py** inside → paste:
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import time

app = FastAPI(title="FraudGuard AI API", version="0.1.0")

class Transaction(BaseModel):
    amount: float
    location: str
    device: Literal["Mobile", "Desktop", "Tablet"]
    timestamp: float | None = None

@app.get("/")
def root():
    return {"status": "ok", "service": "FraudGuard AI"}

@app.post("/predict")
def predict(txn: Transaction):
    # naive placeholder "model"
    score = 0.0
    high_risk_locations = {"Moscow, Russia", "Beijing, China"}
    if txn.amount > 800: score += 0.5
    if txn.location in high_risk_locations: score += 0.4
    score += 0.1  # small base
    score = min(score, 0.99)

    label = "high" if score > 0.7 else ("medium" if score > 0.4 else "low")
    return {
        "risk_score": round(score, 2),
        "risk_label": label,
        "evaluated_at": time.time()
    }
