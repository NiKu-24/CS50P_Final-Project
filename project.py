from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/binary")
def binary():
    return render_template("binary.html")

@app.route("/addition")
def addition():
    return render_template("addition.html")

@app.route("/subtraction")
def subtraction():
    return render_template("subtraction.html")

@app.route("/multiplication")
def multiplication():
    return render_template("multiplication.html")

@app.route("/division")
def division():
    return render_template("division.html")

# Converter and Calculations ............................................

def convert_to_binary(n):
    n = str(n).strip()
    if not n or not n.isdigit():
        raise ValueError("Please enter a whole number like 0, 1, 42...")
    n = int(n)
    return bin(n).replace("0b", "")

def convert_to_decimal(binary_string):
    binary_string = str(binary_string).strip()
    if not binary_string or not set(binary_string).issubset({'0', '1'}):
        raise ValueError("Binary numbers can only contain 0s and 1s.")
    return int(binary_string, 2)

def add_binary(a, b):
    a = str(a).strip()
    b = str(b).strip()
    if not a or not b or not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Use only 0 and 1 in both binary numbers.")
    return bin(int(a, 2) + int(b, 2)).replace("0b", "")

def subtract_binary(a, b):
    a = str(a).strip()
    b = str(b).strip()
    if not a or not b or not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Use only 0 and 1 in both binary numbers.")
    result = int(a, 2) - int(b, 2)
    if result < 0:
        raise ValueError("You can't subtract a bigger binary number from a smaller one.")
    return bin(result).replace("0b", "")

def multiply_binary(a, b):
    a = str(a).strip()
    b = str(b).strip()
    if not a or not b or not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Use only 0 and 1 in both binary numbers.")
    return bin(int(a, 2) * int(b, 2)).replace("0b", "")

def divide_binary(a, b, precision=10):
    a = str(a).strip()
    b = str(b).strip()
    if not a or not b or not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Use only 0 and 1 in both binary numbers.")
    if int(b, 2) == 0:
        return "Error: You can't divide by zero."
    
    dividend = int(a, 2)
    divisor = int(b, 2)

    # Integer part
    integer_part = dividend // divisor
    remainder = dividend % divisor

    result = bin(integer_part)[2:] + '.'

    # Fractional part
    for _ in range(precision):
        remainder *= 2
        bit = remainder // divisor
        result += str(bit)
        remainder %= divisor
        if remainder == 0:
            break

    return result

# --------------------------------------------------------------------------    

@app.route("/try_out", methods=["GET", "POST"])
def convert():
    binary_result = ""
    decimal_result = ""
    binary_add = ""
    binary_subtract = ""
    binary_multiply = ""
    binary_divide = ""
    
    if request.method == "POST":
        if "decimal_input" in request.form:
            value_1 = request.form.get("decimal_input")
            decimal_num= int(value_1)
            binary_result = convert_to_binary(decimal_num)
                
        elif "binary_input" in request.form:
            value_2 = request.form.get("binary_input")
            decimal_result = convert_to_decimal(value_2)
        
        elif "add_input_1" in request.form and "add_input_2" in request.form:
            a = request.form.get("add_input_1")  
            b = request.form.get("add_input_2")
            binary_add = add_binary(a,b)
            
        elif "subtract_input_1" in request.form and "subtract_input_2" in request.form:
            a = request.form.get("subtract_input_1")  
            b = request.form.get("subtract_input_2")
            binary_subtract = subtract_binary(a,b)    
        
        elif "multiply_input_1" in request.form and "multiply_input_2" in request.form:
            a = request.form.get("multiply_input_1")  
            b = request.form.get("multiply_input_2")
            binary_multiply = multiply_binary(a,b)
            
        elif "divide_input_1" in request.form and "divide_input_2" in request.form:
            a = request.form.get("divide_input_1")  
            b = request.form.get("divide_input_2")
            binary_divide = divide_binary(a,b)
            
    return render_template(
    "try_out.html",
    binary=binary_result,
    decimal=decimal_result,
    binary_add=binary_add,
    binary_subtract=binary_subtract,
    binary_multiply=binary_multiply,
    binary_divide=binary_divide
)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
