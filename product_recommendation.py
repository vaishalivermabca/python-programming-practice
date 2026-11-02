customers = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}


def jaccard_similarity(a, b):
    set_a = set(a)
    set_b = set(b)

    common = len(set_a.intersection(set_b))
    total = len(set_a.union(set_b))

    if total == 0:
        return 0

    return common / total


def recommend(customer_name):

    if customer_name == "":
        print("Name cannot be empty.")
        return

    if customer_name not in customers:
        print(f"Customer '{customer_name}' not found.")
        return

    scores = {}

    for name in customers:
        if name != customer_name:
            scores[name] = jaccard_similarity(
                customers[customer_name],
                customers[name]
            )

    print("Similarity scores:")

    for name, score in sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{name}: {score:.2f}")

    best_customer = max(scores, key=scores.get)

    if scores[best_customer] == 0:
        print("No similar customers found.")

        popular = {}
        for products in customers.values():
            for product in products:
                popular[product] = popular.get(product, 0) + 1

        popular_product = max(popular, key=popular.get)
        print(f"Popular product: {popular_product}")
        return

    print("Most similar customer:", best_customer)

    bought = customers[customer_name]
    similar_products = customers[best_customer]

    recommendations = [
        p for p in similar_products if p not in bought
    ]

    if recommendations:
        print("Recommended:", ", ".join(recommendations))
    else:
        print("No new product to recommend.")


name = input("Recommend for: ").strip().title()
recommend(name)
