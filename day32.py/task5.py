# Employee Salary Calculator

# Step 1: Collect employee details
name = input("Enter employee's name: ")
basic_salary = float(input("Enter basic salary (₹): "))
allowances = float(input("Enter total allowances (₹): "))
tax_rate = 0.10  # 10% tax deduction

# Step 2: Calculate deductions and net salary
gross_salary = basic_salary + allowances
tax_deduction = gross_salary * tax_rate
net_salary = gross_salary - tax_deduction

# Step 3: Display formatted salary slip
print("\n💼 --- Salary Slip ---")
print(f"Employee Name : {name}")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"Allowances    : ₹{allowances:.2f}")
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Tax Deduction : ₹{tax_deduction:.2f} (10%)")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("------------------------")
