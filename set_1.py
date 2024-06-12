import math 
def savings(gross_pay,tax_rate,expenses):
    taxed_amount=gross_pay*tax_rate
    after_tax_pay= math.floor(gross_pay-taxed_amount)
    savings= (after_tax_pay-expenses)
    return savings
    
def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material_consumed=int(num_jobs*job_consumption)
    material_waste=str(int(total_material)-int(total_material_consumed))+ material_units
    return material_waste

def interest(principal, rate, periods):
    simple_interest=int(principal*rate*periods)
    final_value=math.floor(principal+simple_interest)
    return final_value