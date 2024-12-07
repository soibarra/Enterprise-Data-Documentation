# Enterprise Data Metadata Documentation

## Data Dictionary
The data dictionary provides a detailed description of each column in the dataset, including data types and purpose.

- `Patient_ID`: Unique identifier for each patient (INTEGER).
- `Visit_Date`: Date of patient visit (DATE).
- `Diagnosis_Code`: Code for patient diagnosis (VARCHAR).
- `Treatment_Cost`: Cost of treatment during the visit (FLOAT).
- `Provider_ID`: Unique identifier for the provider (INTEGER).

## Data Lineage
1. **Input Data Sources**:
   - Data is collected from hospital systems and healthcare providers.
2. **Data Transformation**:
   - Data is cleaned and validated for anomalies (e.g., missing values).
   - Transformation scripts ensure consistent formatting across systems.
3. **Output and Usage**:
   - Data is used for patient billing, analytics, and reporting.

## Dependencies
- `Provider_ID` is related to provider information in the `Providers` table.
- `Diagnosis_Code` maps to diagnosis details in the `Diagnosis` reference table.

