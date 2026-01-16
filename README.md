# Product Categorization & Attribution System

## Overview

The **Product Categorization & Attribution System** is a data operations pipeline designed to transform raw, unstructured retail product data into **accurate, client-specific category mappings**.  
It mirrors real-world data operations workflows used in alternative data and market intelligence companies.

The system prioritizes **accuracy, explainability, and scalability** by combining:
- Rule-based categorization
- Machine learning for ambiguous cases
- Manual review workflows
- Client-specific taxonomy support
- SQL persistence for downstream analytics

---

## Problem Statement

Retail product data is often:
- Messy and unstructured
- Inconsistent across sources
- Ambiguous in wording
- Interpreted differently by different clients

Example:
"Protein Bar Chocolate 50g"

markdown
Copy code

- Client A → *Protein Snacks*
- Client B → *Health Nutrition*

Manual categorization does not scale, while pure ML approaches can silently introduce errors.  
This system solves the problem by using a **hybrid attribution strategy**.

---

## Key Features

- **Rule-Based Categorization**
  - Regex-based rules for high-confidence mappings
  - Deterministic and explainable decisions

- **Machine Learning Fallback**
  - ML classification applied only when rules fail
  - Confidence thresholding to avoid silent errors

- **Manual Review Workflow**
  - Low-confidence products are flagged for human validation
  - Preserves high data accuracy

- **Client-Specific Taxonomies**
  - Same product can map differently per client
  - No pipeline retraining required

- **SQL Persistence**
  - Final product-category mappings stored in SQL
  - Enables analytics, reporting, and auditing

- **Scalable Architecture**
  - Designed to scale to millions of products using PySpark

---

## System Architecture

Raw Product Data
↓
Text Cleaning & Normalization
↓
Rule-Based Categorization (High Confidence)
↓
ML Classification (Ambiguous Cases Only)
↓
Manual Review (Low Confidence)
↓
Client-Specific Category Mapping
↓
SQL Storage for Analytics

yaml
Copy code

---

## Tech Stack

- **Programming:** Python
- **Data Processing:** Pandas, PySpark, Spark SQL
- **Databases:** SQLite / PostgreSQL
- **Machine Learning:** Scikit-learn
- **Text Processing:** RegEx
- **Tools:** Git, VS Code

---

## Project Structure

Product Categorization & Attribution System/
│
├── data/
│ └── products.csv
│
├── rules/
│ └── category_rules.py
│
├── ml/
│ └── ml_classifier.py
│
├── clients/
│ └── client_taxonomies.py
│
├── database/
│ └── db.py
│
├── attribution.py
├── main.py
└── README.md

yaml
Copy code

---

## How It Works

### 1. Data Ingestion
Reads raw product data including titles and descriptions.

### 2. Text Cleaning
Normalizes text to improve matching and classification accuracy.

### 3. Rule-Based Attribution
Applies regex-based rules for high-confidence category matches.

### 4. ML-Based Attribution
Uses a text classifier only for products not matched by rules.

### 5. Manual Review
Flags low-confidence predictions for human validation.

### 6. Client-Specific Mapping
Applies client-defined category hierarchies.

### 7. Persistence
Stores final product-category mappings in SQL.

---

## Example Output

product_id	client	final_category
1	Client_A	Energy Drinks
2	Client_A	Soft Drinks
3	Client_A	Protein Snacks
4	Client_A	Tea & Coffee

yaml
Copy code

---

## Why This Approach

- **Accuracy First:** Rules > ML > Manual Review
- **Explainability:** Every decision is traceable
- **Client Flexibility:** One pipeline supports multiple clients
- **Production-Oriented:** Designed like a real data operations system

---

## Use Cases

- Retail analytics
- Alternative data attribution
- Product intelligence platforms
- Market research pipelines

---

## Future Enhancements

- Integration with cloud data warehouses
- UI for manual review and auditing
- Active learning loop for model improvement
- Support for additional client taxonomies

---

## Author

**G Nikhil Chand**  
