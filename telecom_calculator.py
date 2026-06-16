import math

def dbm_to_watt(dbm):
    watt = 10 ** (dbm / 10) / 1000
    return watt

def watt_to_dbm(watt):
    dbm = 10 * math.log10(watt * 1000)
    return dbm

print("=== Telecom Unit Calculator ===")
print("1. dBm to Watt")
print("2. Watt to dBm")

choice = input("Choose operation (1 or 2): ")

if choice == "1":
    dbm = float(input("Enter value in dBm: "))
    print(f"Result: {dbm_to_watt(dbm)} Watt")

elif choice == "2":
    watt = float(input("Enter value in Watt: "))
    print(f"Result: {watt_to_dbm(watt)} dBm")

else:
    print("Invalid choice!")