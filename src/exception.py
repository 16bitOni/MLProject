import sys

def error_message(error, error_detail: sys):
    """Extracts detailed error message from an exception."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error: {str(error)} at line {line_number} in {file_name}"

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error = error_message(error, error_detail)

    def __str__(self):
        return self.error

# Example usage:
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will cause a ZeroDivisionError
    except Exception as e:
        raise CustomException(e, sys)
