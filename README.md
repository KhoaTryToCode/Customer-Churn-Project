
---

# 📊 MLOps Workflow: Data & Code Versioning

This project uses **Git** for code versioning and **DVC (Data Version Control)** to manage large datasets and model artifacts. This setup ensures reproducibility, allows for "time travel" between versions, and keeps the GitHub repository lightweight by storing data on **DagsHub**.

---

## 🛠 Project Lifecycle Commands

### 1. Daily Workflow: Adding New Data

When you have new data to ingest into the project, follow this linear sequence to ensure both code and data are synchronized.

1. **Ingest & Process:** Run the ingestion script to append new data to the master CSV.
```bash
python add_data.py

```


2. **Snapshot Data (DVC):** Update the DVC tracking for the modified dataset.
```bash
dvc add telecom_churn.csv

```


3. **Upload Data:** Push the physical file to DagsHub remote storage.
```bash
dvc push

```


4. **Commit Metadata (Git):** Save the updated `.dvc` pointer and push to GitHub.
```bash
git add telecom_churn.csv.dvc
git commit -m "data: ingest new batch into telecom_churn.csv"
git push origin main

```



---

### 2. Time Travel: Switching Versions

To move the entire project (code + data) to a previous state or a specific milestone.

1. **Find Target Version:** List the project history to find a commit hash or tag.
```bash
git log --oneline

```


2. **Checkout Code:** Revert scripts and `.dvc` pointers.
```bash
git checkout <commit_hash_or_tag>

```


3. **Checkout Data:** Sync the physical data files to match the current code version.
```bash
dvc checkout

```


*Note: If the data is not in your local cache, use `dvc pull` to download it from DagsHub.*

---

### 3. Setup & Recovery: New Environment

Use this if you are cloning the project for the first time or moving to a new machine.

1. **Clone Repository:**
```bash
git clone https://dagshub.com/KhoaTryToCode/Customer-Churn-Project.git
cd Customer-Churn-Project

```


2. **Pull Data:**
```bash
dvc pull

```



---

## 📂 Key Files & Directory Structure

* `telecom_churn.csv`: The actual dataset (ignored by Git).
* `telecom_churn.csv.dvc`: The **metadata file** (tracked by Git) containing the data hash.
* `.dvc/config`: DVC remote configuration (Public).
* `.dvc/config.local`: Authentication credentials (Private/Ignored by Git).

---