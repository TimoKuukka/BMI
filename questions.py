# MODULE FOR ASKING QUESTION FROM CONSOLE AND CONVERTING ANSWERS TO VARIOUS DATA TYPES
#-------------------------------------------------------------------------------------

# LIBRARIES AND MODULES

# CLASS DEFINITIONS


class Question():
    """A class containing methods to ask questions on console and converting answers to various datatypes."""
    def __init__(self, question):
        self.question = question

    def ask_user_float(self, loop):
        """Asks a question and converts the answer to a floating point number

        Args:
            loop (bool): If True asks the question until able to convert it
        
        Returns:
            tuple: answer as float, error message, error code, detailed error
        """
        # If loop argument is True use while loop until user inputs correct
        if loop == True:

            while True:
                answer_txt = input(self.question)

            # Let's try to convert input to numeric
                try:
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

            # If an error occurs tell the user to check 
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
           
        # Else ask once and return zero value and error information 
        else:
             answer_txt = input(self.question)

            # Let's try to convert input to numeric
        try:
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')

            # If an error occurs tell the user to check 
        except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
                
        return result
    

    def ask_user_integer(self, loop):
        """Asks a question and converts the answer to a integer

        Args:
            loop (bool): If True asks the question until able to convert it
        
        Returns:
            tuple: answer as integer, error message, error code, detailed error
        """
        # If loop argument is True use while loop until user inputs correct
        if loop == True:

            while True:
                answer_txt = input(self.question)

            # Let's try to convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

            # If an error occurs tell the user to check 
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
           
        # Else ask once and return zero value and error information 
        else:
             answer_txt = input(self.question)

            # Let's try to convert input to numeric
        try:
                answer = int(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')

            # If an error occurs tell the user to check 
        except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
                
        return result

    def ask_user_boolean(self, true_value, false_value, loop):
        """_summary_

        Args:
            true_value (str): value to use as True
            false_value (str): value to use as False
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as integer, error message, error code, detailed error
        """
        
        # If loop argument is True use while loop until user inputs correct
        if loop == True:

            while True:
                answer_txt = input(self.question)

            # Let's try to convert input to numeric
                try:
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

            # If an error occurs tell the user to check 
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
           
        # Else ask once and return zero value and error information 
        else:
             answer_txt = input(self.question)

            # Let's try to convert input to numeric
        try:
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')

            # If an error occurs tell the user to check 
        except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
                
        return result

if __name__ == "__main__":

    question = Question('Kuinka vanha olet? ')
    answer_and_error = question.ask_user_float(False)
    print (answer_and_error)