# 🐍 Python — Lists Basics & Operations
# A list in Python is used to store multiple values in one variable

# A list of drone models
drone_models = ["DJI Mini 3", "Parrot Anafi", "Autel Evo", "Skydio 2"]

print(drone_models)         # Show entire list
print(drone_models[0])      # First item
print(drone_models[-1])     # Last item

print("")

# 1️⃣ Creating Lists: List of flight speeds in m/s
speeds = [5, 10, 15, 20]

# 2️⃣ Adding Items to the list
speeds.append(25)       # Add to the end
speeds.insert(1, 8)     # Add at position 1

# 3️⃣ Removing Items from the list
speeds.remove(10)      # Remove by value
speeds.pop()           # Remove last item
speeds.pop(0)           # Remove first item

# Display updated list
print(speeds)

print("")

# 4️⃣ Changing Values
speeds[2] = 18
print(speeds)

# 5️⃣ Looping through a list
for speed in speeds:
    print(f"Drone speed: {speed} m/s")


# 🐍 Python — Lists Basics & Operations
drone_weights = [250, 300, 400, 500]  # Weights in kg

# 1️⃣ Adding Items to the list
drone_weights.append(600)  # Add to the end

# 2️⃣ Change the second item in the list to a new weight.
drone_weights[1] = 320  # Update second item

# 3️⃣ Remove the last item from the list.
drone_weights.pop()  # Remove last item

# 4️⃣ Loop through the list and print each weight.
for weight in drone_weights:
    print(f"Drone weight: {weight} kg")


# 🚁 Python List Challenge — Drone Fleet Manager
# 1️⃣ A list of drones
drones = ["DJI Mini 3", "Parrot Anafi", "Skydio 2", "Autel Evo"]

# 2️⃣ A list of battery percentages
batteries = [85, 65, 40, 95]

# 3️⃣ Add a new drone "DJI Air 2S" with a battery level of 72% to both lists.
drones.append("DJI Air 2S")
batteries.append(72)

# 4️⃣ Change "Parrot Anafi"’s battery to 80%.
batteries[drones.index("Parrot Anafi")] = 80

# 5️⃣ Remove "Skydio 2" and its battery from the lists.
drones.remove("Skydio 2")
batteries.remove(40)

# 6️⃣ Loop through the lists and print each drone’s name with its battery, like:
for i in range(len(drones)):
    print(f"Drone: {drones[i]}, - Battery: {batteries[i]}%")