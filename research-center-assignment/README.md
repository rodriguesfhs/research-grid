# Research Center Quality Classification

This project implements a simple machine learning pipeline to classify research centers into quality tiers based on internal infrastructure and nearby healthcare availability.

The work includes exploratory data analysis (EDA), feature selection, clustering using K-Means, model interpretation, and deployment through a FastAPI endpoint.

---

## Project Structure

```
research-center-assignment/
│
├── research_centers.csv
├── ML Test - Fabio Rodrigues.ipynb
├── app.py
├── clustering_pipeline.joblib
├── requirements.txt
└── README.md
```

---

## Approach

### 1. Data Exploration

The dataset was first inspected for:
- missing values
- basic statistics
- distribution of key variables

EDA included:
- number of research centres per city
- distribution of internal facilities
- healthcare availability (hospitals and pharmacies)
- facility density and diversity
- correlation analysis between numeric features

These steps helped to identify patterns and relationships relevant to research centre quality.

---

### 2. Feature Selection

The following features were selected:

- `internalFacilitiesCount`
- `hospitals_10km`
- `pharmacies_10km`
- `facilityDiversity_10km`
- `facilityDensity_10km`

Geographic coordinates were excluded, as they describe location but do not directly indicate quality.

Correlation analysis showed strong relationships between:
- internal capacity
- facility density and diversity
- healthcare availability

---

### 3. Data Normalisation

Features were standardised using `StandardScaler`.

This is necessary to ensure that variables on different scales would be comparable.

---

### 4. Clustering (K-Means)

A K-Means model was trained with:

- `n_clusters = 3`
- `random_state = 42`

This aligns with the three required quality tiers:
- Premium
- Standard
- Basic

Clustering performance was evaluated using the silhouette score.

---

### 5. Cluster Interpretation

Cluster averages were analysed to assign meaningful labels:

- Highest values across features → Premium
- Intermediate values → Standard
- Lowest values → Basic

Summary tables and visualisations were used to support this interpretation.

Key observations:
- Higher-quality centres tend to have more facilities and better healthcare access
- Facility diversity shows strong separation between clusters
- Premium centres are relatively evenly distributed across cities

---

### 6. Model Saving

A pipeline combining:
- `StandardScaler`
- `KMeans`

was saved using `joblib`:

```
clustering_pipeline.joblib
```

This allows consistent preprocessing and prediction during deployment.

---

## API (FastAPI)

A simple FastAPI app exposes the trained model.

### Endpoint

```
POST /predict
```

### Example Input

```json
{
  "internalFacilitiesCount": 9,
  "hospitals_10km": 3,
  "pharmacies_10km": 2,
  "facilityDiversity_10km": 0.82,
  "facilityDensity_10km": 0.45
}
```

### Example Output

```json
{
  "predictedCategory": "Premium"
}
```

The API:
- loads the saved pipeline
- scales automatically
- predicts the cluster
- maps it to a quality tier

---

---

## Author

Fabio Rodrigues
