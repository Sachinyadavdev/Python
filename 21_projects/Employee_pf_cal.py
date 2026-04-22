# This program helps in calculating the PF amount for an employee based on their basic salary and years of service.

def calculate_pf(basic_salary, years_of_service):
    # PF contribution is typically 12% of the basic salary
    pf_contribution = 0.12 * basic_salary
    
    # Total PF amount is the contribution multiplied by the number of years of service
    total_pf = pf_contribution * years_of_service
    
    return total_pf

# Function for Calculating the CTC, Hand in Salary and Basic Salary 
def calculate_salary(ctc):
    # Assuming basic salary is 40% of CTC
    basic_salary = 0.40 * ctc
    
    # Assuming hand in salary is 60% of CTC
    hand_in_salary = 0.60 * ctc
    
    return basic_salary, hand_in_salary

# Taking user input for CTC and years of service
ctc = float(input("Enter your CTC (Cost to Company): "))
years_of_service = int(input("Enter your years of service: "))
basic_salary, hand_in_salary = calculate_salary(ctc)
pf_amount = calculate_pf(basic_salary, years_of_service)
print(f"Your Basic Salary is: {basic_salary}")
print(f"Your Hand in Salary is: {hand_in_salary}")
print(f"Your PF amount after {years_of_service} years of service is: {pf_amount}")
