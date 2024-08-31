def zeroDivisionCheck(operand1,operand2):
    try:
        result=operand1/operand2
        return result
    except ZeroDivisionError:
        print("\nError : Division by zero is not allowed")
        return None
result=zeroDivisionCheck(10,2)
print(result)
result = zeroDivisionCheck(10,0)
print(result)

# Output
# 5.0
# Error : Division by zero is not allowed
# None