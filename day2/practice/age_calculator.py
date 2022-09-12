try:
    age = int(input('Enter your Age:'))

except Exception as e:
    print(f'Error: {e}')

decaces = age // 10
years = age % 10
print(f'Age: {age}, Decaces: {decaces}, Years: {years}')
