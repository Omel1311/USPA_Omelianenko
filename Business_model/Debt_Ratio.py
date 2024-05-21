# Расчет уровня задолженности
def calculate_debt_ratio(total_debt, total_assets):
    return (total_debt / total_assets) * 100

total_debt = 5000000  # Общая сумма долга в долларах
total_assets = 10000000  # Общая стоимость активов в долларах

debt_ratio = calculate_debt_ratio(total_debt, total_assets)
print(f"Уровень задолженности составляет {debt_ratio}%")