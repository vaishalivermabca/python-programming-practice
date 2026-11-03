from collections import Counter

# Purchases stored as a dictionary of lists
purchases = {
    "Amit":   ["Laptop", "Mouse", "Keyboard"],
    "Bina":   ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya":  ["Laptop", "Keyboard", "Monitor", "Webcam"],
}


def jaccard_similarity(list_a, list_b):
    """Jaccard = |A ∩ B| / |A ∪ B|"""
    set_a, set_b = set(list_a), set(list_b)
    union = set_a | set_b
    if not union:
        return 0.0
    return len(set_a & set_b) / len(union)


def find_customer(name):
    """Case-insensitive lookup; returns the stored name or None."""
    for customer in purchases:
        if customer.lower() == name.lower():
            return customer
    return None


def recommend(name):
    name = name.strip()

    # Invalid input handling
    if name == "":
        print("Name cannot be empty.")
        return
    customer = find_customer(name)
    if customer is None:
        print(f"Customer '{name}' not found.")
        return

    # Calculate similarity with every other customer
    scores = {}
    for other, items in purchases.items():
        if other != customer:
            scores[other] = jaccard_similarity(purchases[customer], items)

    # Show scores, highest first
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_name, best_score = sorted_scores[0]

    if best_score == 0:
        # Boundary case: nobody is similar
        print("No similar customers found.")
        all_items = [item for items in purchases.values() for item in items]
        product, count = Counter(all_items).most_common(1)[0]
        print(f"Popular product: {product} (bought by {count} customers)")
        return

    print("Similarity scores:")
    for other, score in sorted_scores:
        print(f"{other} : {score:.2f}")
    print(f"Most similar customer: {best_name}")

    # Recommend what the similar customer has but this customer doesn't
    recommended = [p for p in purchases[best_name] if p not in purchases[customer]]
    print("Recommended: " + ", ".join(recommended))


def main():
    name = input("Recommend for: ")
    recommend(name)


if __name__ == "__main__":
    main()
