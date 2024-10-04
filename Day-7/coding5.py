class CustomError(Exception):
    pass

def process_input(data):
    try:
        if not data:
            raise CustomError("Error:Empty input provided")
        if len(data) >255:
            raise CustomError("Error:Input Exceeds maximum length")
        if any(char.isdigit() for char in data):
            raise CustomError("Error:Input contains invalid characters")
        return "Input processed successfully"

    except CustomError as e:
            return str(e)

    finally:
            print("Program execution completed")