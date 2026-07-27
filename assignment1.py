
#Accept item cost from user . 
# Add sale tax 12%, 
# Octroi 4% and and 
# excise duty 2%
#print the total cost of item


#Accept item cost from user . 
cost=float(input("Enter the cost value:"))

sales_tax=cost*0.12
octroi=cost*0.4
excise_duty=cost*0.2

total_cost=cost+sales_tax+octroi+excise_duty

# Display results
print("Item Cost:", cost)
print("Sales Tax (12%):", sales_tax)
print("Octroi (4%):", octroi)
print("Excise Duty (2%):", excise_duty)
print("Total Cost:", total_cost)