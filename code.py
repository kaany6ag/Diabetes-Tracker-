"""
======================================================
      DIABETES HEALTH TRACKER - FULL PROJECT
======================================================

Features Included:
✔ Login system (Birth year question)
✔ Menu system
✔ Add daily entry
✔ Diabetes risk calculation
✔ BP recommendations
✔ Weekly summary
✔ Save text report
✔ Export JSON
✔ Plot graph (matplotlib)
✔ PDF report
"""

import json
from fpdf import FPDF
import matplotlib.pyplot as plt

# LOGIN SYSTEM
def login():
    print("===== LOGIN =====")

    username = input("Create your username: ")

    print("\nTo set your password, answer this question:")
    question = "What is your birth year? "
    correct_answer = input(question)

    print("\nNow login to continue.\n")

    while True:
        entered_username = input("Username: ")
        entered_password = input(question)

        if entered_username == username and entered_password == correct_answer:
            print("\n✔ Login successful!\n")
            return True
        else:
            print("\n❌ Incorrect answer. Try again.\n")


# RISK CALCULATION

def calculate_risk(glucose, bmi, age, bp):
    score = glucose * 0.4 + bmi * 0.3 + age * 0.2 + bp * 0.1
    if score < 80:
        return "Low Risk"
    elif score < 120:
        return "Moderate Risk"
    else:
        return "High Risk"


# BP RECOMMENDATION SYSTEM

def bp_recommendation(bp):
    if bp < 80:
        return "Low BP — Eat salty food, drink fluids, avoid sudden standing."
    elif 80 <= bp <= 120:
        return "Normal BP — Maintain healthy lifestyle."
    elif 121 <= bp <= 139:
        return "Elevated BP — Reduce salt, walk daily."
    elif 140 <= bp <= 159:
        return "Stage 1 Hypertension — Avoid oily foods, monitor BP weekly."
    else:
        return "Stage 2 Hypertension — Consult doctor immediately."


# List to store all entries
entries = []



# ADD DAILY ENTRY

def add_entry():
    print("\n=== ADD TODAY'S ENTRY ===")
    glucose = float(input("Glucose Level: "))
    bmi = float(input("BMI: "))
    age = int(input("Age: "))
    bp = float(input("Blood Pressure: "))

    risk = calculate_risk(glucose, bmi, age, bp)
    advice = bp_recommendation(bp)

    data = {
        "Glucose": glucose,
        "BMI": bmi,
        "Age": age,
        "BP": bp,
        "Risk": risk,
        "Advice": advice
    }

    entries.append(data)

    print("\n Risk Level:", risk)
    print(" Recommendation:", advice)
# SUMMARY

def show_summary():
    if not entries:
        print("\nNo entries found.\n")
        return

    print("\n========= SUMMARY =========\n")

    glucose_values = [e["Glucose"] for e in entries]
    bp_values = [e["BP"] for e in entries]

    print("Total Days Recorded:", len(entries))
    print("Average Glucose:", sum(glucose_values) / len(glucose_values))
    print("Highest Glucose:", max(glucose_values))
    print("Lowest Glucose:", min(glucose_values))

    print("\nDetailed Entries:")
    for i, entry in enumerate(entries):
        print(f"Day {i+1}: {entry}")


# SAVE TEXT REPORT

def save_text():
    with open("diabetes_report.txt", "w") as f:
        f.write("===== DIABETES REPORT =====\n\n")
        for i, entry in enumerate(entries):
            f.write(f"Day {i+1}: {entry}\n")

    print("\n📁 Text report saved as 'diabetes_report.txt'")

# EXPORT JSON

def export_json():
    with open("diabetes_data.json", "w") as f:
        json.dump(entries, f, indent=4)

    print("\n📁 JSON file saved as 'diabetes_data.json'")

# GRAPH
def plot_graph():
    if not entries:
        print("\nNo data to plot.\n")
        return

    glucose_values = [e["Glucose"] for e in entries]

    plt.plot(glucose_values, marker='o')
    plt.title("Glucose Levels Over Days")
    plt.xlabel("Day Number")
    plt.ylabel("Glucose Level")
    plt.grid(True)
    plt.show()

# PDF REPORT
def export_pdf():
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Diabetes Tracker Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)

    for i, entry in enumerate(entries):
        pdf.cell(0, 10, txt=f"Day {i+1}: {entry}", ln=True)

    pdf.output("diabetes_report.pdf")
    print("\n📁 PDF saved as 'diabetes_report.pdf'")

# MENU SYSTEM

def menu():
    while True:
        print("""
============================
        MAIN MENU
============================
1. Add new entry
2. View summary
3. Save text report
4. Export JSON file
5. View glucose graph
6. Export PDF report
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            save_text()
        elif choice == "4":
            export_json()
        elif choice == "5":
            plot_graph()
        elif choice == "6":
            export_pdf()
        elif choice == "7":
            print("\nThank you for using the Diabetes Tracker!")
            break
        else:
            print("\nInvalid choice. Try again.\n")

login()
menu()