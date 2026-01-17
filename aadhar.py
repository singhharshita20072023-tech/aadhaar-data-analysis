
"""
Aadhaar Data Analysis Project
Author: Harshita Singh
Hackathon Submission
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# File Paths (same folder)
# -----------------------------
ENROLLMENT_FILE = "aadhaar_enrolment_update.csv"
DEMOGRAPHIC_FILE = "aadhaar_demographic_update.csv"
BIOMETRIC_FILE = "aadhaar_biometric_update.csv"

# -----------------------------
# Load Datasets
# -----------------------------
try:
    enrollment_df = pd.read_csv(ENROLLMENT_FILE, low_memory=False)
    demographic_df = pd.read_csv(DEMOGRAPHIC_FILE, low_memory=False)
    biometric_df = pd.read_csv(BIOMETRIC_FILE, low_memory=False)
    print("All Aadhaar datasets loaded successfully.\n")
except FileNotFoundError as e:
    print("Dataset file not found:", e)
    exit()

# -----------------------------
# Convert numeric columns safely
# -----------------------------
enrollment_cols = ["age_0_5", "age_5_17", "age_18_greater"]
demographic_cols = ["demo_age_5_17", "demo_age_17_"]
biometric_cols = ["bio_age_5_17", "bio_age_17_"]

for col in enrollment_cols:
    enrollment_df[col] = pd.to_numeric(enrollment_df[col], errors="coerce")

for col in demographic_cols:
    demographic_df[col] = pd.to_numeric(demographic_df[col], errors="coerce")

for col in biometric_cols:
    biometric_df[col] = pd.to_numeric(biometric_df[col], errors="coerce")

# Drop missing values
enrollment_df.dropna(inplace=True)
demographic_df.dropna(inplace=True)
biometric_df.dropna(inplace=True)

# -----------------------------
# Show Data Overview
# -----------------------------
print("Aadhaar Enrollment Data Overview")
print(enrollment_df.head(), "\n")

print("Aadhaar Demographic Update Data Overview")
print(demographic_df.head(), "\n")

print("Aadhaar Biometric Update Data Overview")
print(biometric_df.head(), "\n")

# -----------------------------
# ANALYSIS & VISUALIZATION
# -----------------------------

# 1️⃣ Enrollment Age-wise Distribution
enrollment_age_sum = enrollment_df[enrollment_cols].sum()

plt.figure(figsize=(8, 5))
enrollment_age_sum.plot(kind="bar")
plt.title("Aadhaar Enrollment by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Enrollments")
plt.tight_layout()
plt.show()

# 2️⃣ Demographic Updates by State (Top 10)
demo_state = demographic_df.groupby("state")["demo_age_17_"].sum()
top10_demo = demo_state.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
top10_demo.plot(kind="bar")
plt.title("Top 10 States by Aadhaar Demographic Updates (Age 17+)")
plt.xlabel("State")
plt.ylabel("Number of Updates")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3️⃣ Biometric Updates by State (Top 10)
bio_state = biometric_df.groupby("state")["bio_age_17_"].sum()
top10_bio = bio_state.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
top10_bio.plot(kind="bar")
plt.title("Top 10 States by Aadhaar Biometric Updates (Age 17+)")
plt.xlabel("State")
plt.ylabel("Number of Updates")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Aadhaar Data Analysis Completed Successfully.")
print("Insights generated from enrollment, demographic, and biometric datasets.")
