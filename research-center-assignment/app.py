#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("clustering_pipeline.joblib")

cluster_to_category = {
    1: "Premium",
    0: "Standard",
    2: "Basic"}

@app.post("/predict")
def predict(data: dict):
    X_new = pd.DataFrame([data])
    cluster = int(model.predict(X_new)[0])
    category = cluster_to_category[cluster]
    return {"predictedCategory": category}

