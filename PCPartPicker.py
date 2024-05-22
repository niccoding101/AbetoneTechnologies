#in development

import json

# Sample data
pc_parts = {
    "CPUs": [
        {"name": "AMD Ryzen 5 5600X", "price": 200, "rating": 4.8},
        {"name": "Intel i5 11600K", "price": 230, "rating": 4.7},
        # More CPUs...
    ],
    "GPUs": [
        {"name": "NVIDIA RTX 3060", "price": 400, "rating": 4.5},
        {"name": "AMD RX 6700 XT", "price": 480, "rating": 4.6},
        # More GPUs...
    ],
    "Motherboards": [
        {"name": "ASUS ROG Strix B550-F", "price": 180, "rating": 4.7},
        {"name": "MSI MPG Z490 Gaming Edge", "price": 200, "rating": 4.6},
        # More Motherboards...
    ],
    "RAM": [
        {"name": "Corsair Vengeance LPX 16GB", "price": 80, "rating": 4.7},
        {"name": "G.Skill Ripjaws V 16GB", "price": 85, "rating": 4.6},
        # More RAM...
    ],
    "Storage": [
        {"name": "Samsung 970 Evo 1TB", "price": 120, "rating": 4.8},
        {"name": "Western Digital Blue 1TB", "price": 50, "rating": 4.5},
        # More Storage...
    ],
    "Cases": [
        {"name": "NZXT H510", "price": 70, "rating": 4.7},
        {"name": "Corsair 275R", "price": 80, "rating": 4.6},
        # More Cases...
    ],
    "Power Supplies": [
        {"name": "Corsair RM750x", "price": 100, "rating": 4.8},
        {"name": "EVGA SuperNOVA 650 G5", "price": 90, "rating": 4.7},
        # More Power Supplies...
    ],
    "Peripherals": [
        {"name": "Logitech G502 Hero", "price": 50, "rating": 4.8},
        {"name": "Corsair K95 RGB Platinum", "price": 130, "rating": 4.7},
        # More Peripherals...
    ],
    "Games/Productivity": [
        {"name": "Cyberpunk 2077", "price": 60, "rating": 4.5},
        {"name": "Adobe Photoshop", "price": 240, "rating": 4.6},
        # More Games/Productivity software...
    ],
}

def filter_and_sort_parts(parts, budget):
    filtered_parts = {category: [] for category in parts}
    
    for category, items in parts.items():
        for item in items:
            if item["price"] <= budget:
                filtered_parts[category].append(item)
        
        # Sort by rating descending, then by price ascending
        filtered_parts[category].sort(key=lambda x: (-x["rating"], x["price"]))
    
    return filtered_parts

def recommend_parts(parts, budget, preferred_cpu, preferred_motherboard, preferred_ram):
    total_cost = 0
    recommendations = {category: [] for category in parts}
    
    # Adding preferred CPU to recommendations
    for cpu in parts["CPUs"]:
        if preferred_cpu.lower() in cpu["name"].lower() and cpu["price"] <= budget:
            recommendations["CPUs"].append(cpu)
            total_cost += cpu["price"]
            budget -= cpu["price"]
            break

    # Adding preferred Motherboard to recommendations
    for motherboard in parts["Motherboards"]:
        if preferred_motherboard.lower() in motherboard["name"].lower() and motherboard["price"] <= budget:
            recommendations["Motherboards"].append(motherboard)
            total_cost += motherboard["price"]
            budget -= motherboard["price"]
            break

    # Adding preferred RAM to recommendations
    for ram in parts["RAM"]:
        if preferred_ram.lower() in ram["name"].lower() and ram["price"] <= budget:
            recommendations["RAM"].append(ram)
            total_cost += ram["price"]
            budget -= ram["price"]
            break

    # Adding other parts based on remaining budget
    for category, items in parts.items():
        if category not in ["CPUs", "Motherboards", "RAM"]:
            for item in items:
                if item["price"] <= budget:
                    recommendations[category].append(item)
    
    return recommendations, total_cost

def display_recommendations(recommendations):
    print("Recommended Parts within Budget:")
    for category, items in recommendations.items():
        if items:
            print(f"\n{category}:")
            for i, item in enumerate(items):
                print(f"  {i+1}. {item['name']} - ${item['price']} (Rating: {item['rating']})")

def get_user_choice(options, prompt):
    while True:
        for i, option in enumerate(options):
            print(f"{i+1}. {option['name']} - ${option['price']} (Rating: {option['rating']})")
        choice = int(input(prompt)) - 1
        if 0 <= choice < len(options):
            return options[choice]
        else:
            print("Invalid choice. Please try again.")

def main():
    user_budget = int(input("Enter your budget: "))
    filtered_parts = filter_and_sort_parts(pc_parts, user_budget)
    
    print("Select your preferred CPU:")
    selected_cpu = get_user_choice(filtered_parts["CPUs"], "Choose a CPU: ")
    user_budget -= selected_cpu["price"]
    
    print("Select your preferred Motherboard:")
    selected_motherboard = get_user_choice(filtered_parts["Motherboards"], "Choose a Motherboard: ")
    user_budget -= selected_motherboard["price"]

    print("Select your preferred RAM:")
    selected_ram = get_user_choice(filtered_parts["RAM"], "Choose a RAM: ")
    user_budget -= selected_ram["price"]

    recommendations, total_cost = recommend_parts(filtered_parts, user_budget, selected_cpu["name"], selected_motherboard["name"], selected_ram["name"])
    
    display_recommendations(recommendations)
    print(f"\nTotal Cost: ${total_cost}")

if __name__ == "__main__":
    main()
