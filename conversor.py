import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"  # URL da API

def get_exchange_rates(base_currency):
    """Obtém as taxas de câmbio a partir da moeda base."""
    response = requests.get(API_URL + base_currency)
    if response.status_code == 200:
        return response.json()['rates']
    else:
        print("Erro ao buscar taxas de câmbio.")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """Converte um valor de uma moeda para outra usando as taxas de câmbio."""
    if from_currency == to_currency:
        return amount
    conversion_rate = rates[to_currency] / rates[from_currency]
    return amount * conversion_rate

def main():
    print("Bem-vindo ao Conversor de Moedas!")
    base_currency = input("Insira a moeda de origem (ex: USD, EUR, BRL): ").upper()
    rates = get_exchange_rates(base_currency)

    if rates:
        print("Moedas disponíveis para conversão:")
        for currency in rates.keys():
            print(currency)

        to_currency = input("Insira a moeda de destino: ").upper()
        if to_currency not in rates:
            print("Moeda de destino inválida.")
            return

        amount = float(input("Insira o valor a ser convertido: "))
        converted_amount = convert_currency(amount, base_currency, to_currency, rates)
        print(f"{amount} {base_currency} é igual a {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
