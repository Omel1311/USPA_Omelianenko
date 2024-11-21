""""Стоимость привлечения клиента (Customer Acquisition Cost, CAC)"""

# Расчет CAC
def calculate_cac(total_marketing_costs, new_customers_acquired):
    return total_marketing_costs / new_customers_acquired

total_marketing_costs = int(input("Введите общие затраты на маркетинг в долларах: "))  # Общие затраты на маркетинг в долларах

new_customers_acquired = 500  # Количество новых клиентов


cac = calculate_cac(total_marketing_costs, new_customers_acquired)
print(f"CAC составляет ${cac} на каждого нового клиента")