** Diabetes Health Tracker — Python Project **

A complete Python-based Diabetes Health Tracker built using ONLY beginner-friendly concepts such as lists, dictionaries, loops, functions, file handling, and simple logic. The system allows users to record health data, calculate diabetes risk, get BP-based recommendations, generate reports, create PDFs, and view glucose graphs.

** Features **

 1. Login System  
- User chooses ANY username  
- Password = **answer to: “What is your birth year?”**  
- Very easy, case-insensitive, and space-insensitive  

 2. Add Daily Health Entries  
 User enters:
- Glucose Level (mg/dL)  
- BMI  
- Age  
- Blood Pressure  

Stored using **list of dictionaries**.



 3. Diabetes Risk Calculation  
Risk levels:
- Low Risk  
- Moderate Risk  
- High Risk  

Uses a simple weighted formula.

 4. Blood Pressure Recommendations  
Based on BP value:
- Eat salty food / hydration tips  
- Reduce salt / avoid oily foods  
- When to consult a doctor  
- Lifestyle guidance  


 5. Weekly Summary  
Shows:
- Number of days recorded  
- Average glucose  
- Highest & lowest glucose  
- All entries listed day-wise  


6. File Saving  
 **Text Report:**  
Saved as:

diabetes_report.txt

 **JSON Export:**  
Saved as:

diabetes_data.json



7. Glucose Graph  
Uses **matplotlib** to show glucose level trend over days.


 8. PDF Report  
Generates a full PDF:

diabetes_report.pdf

Using **FPDF** library.

 >>>Project Structure

DiabetesTracker/ │ ├── diabetes_tracker_full.py   # Main program ├── diabetes_report.txt        # Auto-created ├── diabetes_data.json         # Auto-created ├── diabetes_report.pdf        # Auto-created └── README.md                  # Documentation



>>>Technologies Used

- Python  
- Lists & Dictionaries  
- Loops (while, for)  
- Functions  
- File Handling  
- JSON  
- Matplotlib  
- FPDF  


>>> Installation

Install required libraries:

pip install matplotlib fpdf

>>>How to Run??

Run the project in terminal:

python diabetes_tracker_full.py

> Steps:
1. Create username  
2. Enter your birth year (this becomes your password)  
3. Login  
4. Choose from menu:

1. Add new entry

2. View summary

3. Save text report

4. Export JSON file

5. View glucose graph

6. Export PDF report

7. Exit





> Python Concepts Covered

- Lists and append()  
- Dictionaries  
- Loops  
- Functions  
- If-Else conditions  
- File handling  
- JSON export  
- Graph plotting  
- Menu-driven system  
- Login logic  
 
 >Conclusion

This project is a complete and beginner-friendly Python health tracker that demonstrates multiple programming concepts while being practical and easy to explain for academic submission.

 >Author

Kaanya Agrawal
Reg no.:25BAI10237
Branch: CSE -AIML  

