# Product Recommendation System - PS No. 85

# Customer purchase history
customers = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Mobile", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Headphones"]
}

def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if len(set1.union(set2)) == 0:
        return 0
    return len(set1.intersection(set2)) / len(set1.union(set2))

# Input from user
name = input("Enter customer name: ").strip()

# Validation
if name == "":
    print("Name cannot be empty")
else:
    if name not in customers:
        print(f"Customer {name} not found")
        # Show popular product if not found
        all_products = []
        for products in customers.values():
            all_products.extend(products)
        popular = max(set(all_products), key=all_products.count)
        print(f"Popular product: {popular}")
    else:
        current_user_products = customers[name]
        max_similarity = 0
        most_similar_user = None

        # Find most similar customer
        for other_name, other_products in customers.items():
            if other_name != name:
                similarity = jaccard_similarity(current_user_products, other_products)
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_user = other_name
        
        if most_similar_user:
            print(f"Most similar customer: {most_similar_user}")
            # Recommend product not already bought
            similar_user_products = customers[most_similar_user]
            recommendation = None
            for product in similar_user_products:
                if product not in current_user_products:
                    recommendation = product
                    break
            
            if recommendation:
                print(f"Recommended: {recommendation}")
            else:
                print("No new product to recommend")
        else:
            print("No similar customer found")
