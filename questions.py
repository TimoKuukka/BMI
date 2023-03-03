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
        """Asks a question and converts the answer to a boolean value

        Args:
            true_value (str): value to use as True
            false_value (str): value to use as False
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as integer, error message, error code, detailed error
        """

        # If loop argument is True use while loop until user inputs correct
        prompt = f'{self.question}, vastaa {true_value}/{false_value}: '
        if loop == True:

            while True:
                answer_txt = input(prompt)
                answer_txt = answer_txt.lower()

                if answer_txt == true_value.lower():
                     answer = True
                     result = (answer, 'OK', 0, 'Conversion successful')
                     break
                elif answer_txt == false_value.lower():
                     answer = False
                     result = (answer, 'OK', 0, 'Conversion successful')
                     break
                else:
                    print('Virhe syötetyssä arvossa, sallitut arvot', true_value, false_value)
                    result = ('N/A', 'Error', 1, 'unable to convert to boolean')
           
        # Else ask once and return zero value and error information 
        else:
            answer_txt = input(prompt)
            answer_txt = answer_txt.lower()

            if answer_txt == true_value.lower():
                    answer = True
                    result = (answer, 'OK', 0, 'Conversion successful')
            elif answer_txt == false_value.lower():
                    answer = False
                    result = (answer, 'OK', 0, 'Conversion successful')
            else:
                print('Virhe syötetyssä arvossa, sallitut arvot', true_value, false_value)
                result = ('N/A', 'Error', 1, 'unable to convert to boolean')
                
        return result

if __name__ == "__main__":

    question = Question('Kuinka paljon painat (kg)? ')
    answer_and_error = question.ask_user_float(False)
    print (answer_and_error)

    question2 = Question('Kuinka vanha olet? ')
    answer_and_error = question2.ask_user_integer(True)
    print(answer_and_error)

    question3 = Question('Haluatko lähteä viikonlopun viettoon? ')
    answer_and_error = question3.ask_user_boolean('Y', 'N', True)
    print(answer_and_error)