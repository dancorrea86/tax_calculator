import pyinputplus as pyip

PIS_RATE = 0.0065
COFINS_RATE = 0.03


while True:
    print ('Qual o faturamento: ')
    revenues_of_month = input()
    try:
        revenues_of_month = float(revenues_of_month)
    except:
        print ('Por favor, informe um numero.')
        continue
    if revenues_of_month < 1:
        print ('Por favor, informe um numero positivo')
        continue
    break

def validation_if_input_isNumber():
    
def valation_input_issqn_rate():
    while True:
        print('ola')
        issqn_rate = input()

        if (issqn_rate < 0.02 and issqn_rate > 0.05):
            print("Por favor, a alíquota deve ser maior do que '2%' e menor que '5%'")
            continue

        try:
            issqn_rate = float(issqn_rate)
        except:
            print('Por favor, informe um número.')
            continue
        break
    return issqn_rate

# working in a new branch
print('Informe a alíquota de ISSQN')
issqn_rate = valation_input_issqn_rate()
issqn_retention_of_moth = input('Qual o valor da retenção: ')
pis_retention_of_moth = input('Qual o valor da retenção: ')
cofins_retention_of_moth = input('Qual o valor da retenção: ')

def pis_calculation(revenues_of_month):
    pis_value = revenues_of_month * PIS_RATE
    return float(pis_value)

def cofins_calculation(revenues_of_month):
    cofins_value = revenues_of_month * COFINS_RATE
    return float(cofins_value)

def issqn_calculation(revenues_of_month, issqn_rate):
    issqn_value = revenues_of_month * issqn_rate
    return float(issqn_value)

def show_the_results():

    print(pis_calculation(revenues_of_month))
    print(cofins_calculation(revenues_of_month))
    print(issqn_calculation(revenues_of_month, issqn_rate))

if __name__ == "__main__":
    show_the_results()