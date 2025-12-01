def safe_div(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "Error: Cannot Divide by Zero"
    except TypeError:
        return "Please Enter Numbers only"
    except Exception as e:
        return f"Unknown Error: {e}"
print(safe_div(5,2))
print(safe_div(5,0))
print(safe_div(5,"A"))