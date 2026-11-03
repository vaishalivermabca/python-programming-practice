# 🛒 Product Recommendation System

A simple Python program that recommends products to a customer using **Jaccard similarity**.

> **PS No.:** 85 | **Rungta International Skills University** | School of Information Technology | Bachelor of Computer Application
> **Submitted by:** [Your Name] ([Enrollment No.])

---

## 📌 Problem Statement

Recommend products using Jaccard similarity (common products / all different products). Find the customer most similar to the chosen one and recommend what the chosen customer has not bought. If all similarities are 0, show the most popular product.

## 🧰 Tech Stack

- Python 3
- Concepts: Dictionaries, Sets, Lists, Functions

## 📂 Project Structure

```
product_recommendation/
├── recommend.py
├── README.md
└── screenshots/
    ├── test1.png
    ├── test2.png
    ├── test3a.png
    ├── test3b.png
    └── test4.png
```

## 🗃️ Sample Data

| Customer | Purchases |
|----------|-----------|
| Amit | Laptop, Mouse, Keyboard |
| Bina | Laptop, Mouse, Headphones |
| Chetan | Phone, Charger |
| Divya | Laptop, Keyboard, Monitor, Webcam |

## ⚙️ How It Works

1. Purchases are stored in a dictionary of lists.
2. Lists are converted to sets for comparison.
3. Jaccard similarity is calculated with:

   **J(A, B) = |A ∩ B| / |A ∪ B|**

4. Scores for all other customers are shown with two decimals, highest first.
5. Items bought by the most similar customer but not by the chosen customer are recommended.
6. If all scores are 0, the most popular product is shown instead.

**Example:** Amit = {Laptop, Mouse, Keyboard}, Bina = {Laptop, Mouse, Headphones}
Common = 2, Total unique = 4, so similarity = 2/4 = **0.50**

## ▶️ How to Run

```bash
git clone <your-repo-link>
cd product_recommendation
python recommend.py
```

Then enter a customer name when prompted.

## ✅ Test Cases

### Test Case 1: Normal Input
```
Recommend for: Amit
Similarity scores:
Bina : 0.50
Divya : 0.40
Chetan : 0.00
Most similar customer: Bina
Recommended: Headphones
```

### Test Case 2: Boundary / Minimum Input
```
Recommend for: Chetan
No similar customers found.
Popular product: Laptop (bought by 3 customers)
```

### Test Case 3: Invalid Input
```
Recommend for: Zara
Customer 'Zara' not found.
```
```
Recommend for:
Name cannot be empty.
```

### Test Case 4: Different Valid Scenario
```
Recommend for: Bina
Similarity scores:
Amit : 0.50
Divya : 0.17
Chetan : 0.00
Most similar customer: Amit
Recommended: Keyboard
```

## 📸 Screenshots

| Test Case 1 | Test Case 2 |
|---|---|
| ![Test 1](screenshots/test1.png) | ![Test 2](screenshots/test2.png) |

| Test Case 3 | Test Case 4 |
|---|---|
| ![Test 3](screenshots/test3a.png) | ![Test 4](screenshots/test4.png) |

## 🎯 Features

- Jaccard similarity function
- Scores sorted highest first (2 decimal places)
- Case-insensitive customer name search
- Handles unknown and empty names
- Popular product fallback when no similar customer exists

## 🏁 Conclusion

The system successfully recommends products using Jaccard similarity and handles edge cases like unknown customers, empty input, and zero similarity.
