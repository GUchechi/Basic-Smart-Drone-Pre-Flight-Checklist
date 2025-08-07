# Initial input
battery = int(input("Enter battery %: "))
wind = int(input("Enter wind speed (km/h): "))
signal = input("Enter signal status (strong/weak): ")

# Keep checking until all conditions are optimal
while not (battery >= 70 and wind <= 20 and signal == "strong"):
    if battery < 50:
        print("❌ Battery too low!")
    elif wind > 30:
        print("🌪️ Too windy to fly!")
    elif signal == "weak":
        print("📡 Weak signal. Check connection.")
    else:
        print("⚠️ Conditions not ideal. Use caution.")
    
    #Ask again
    print("\n🔁 Re-enter updated conditions:")
    battery = int(input("Enter battery %: "))
    wind = int(input("Enter wind speed (km/h): "))
    signal = input("Enter signal status (strong/weak): ")

print("✅ All conditions optimal. Ready for takeoff!")
print("🧾 Pilot check complete. Status logged.")
