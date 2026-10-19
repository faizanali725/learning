
# ---------------- Reusable Input Helper Functions ----------------


def get_int_input(prompt, min_value=None):
    """Keep asking until the user enters a valid integer within range."""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a whole number.")





def get_float_input(prompt, min_value=None):
    """Keep asking until the user enters a valid number within range."""
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a valid number.")




def get_confirmation(prompt):
    """Return True for yes and False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter yes or no.")



def get_valid_doctor_id(prompt, doctors):
    """Return a doctor ID that exists in the doctors dictionary."""
    if not doctors:
        print("No doctors available. Please add a doctor first.")
        return None

    while True:
        doctor_id = get_int_input(prompt)
        if doctor_id in doctors:
            return doctor_id
        print("Doctor ID not found! Please enter an existing doctor ID.")




def get_available_room_number(prompt, patients, current_patient_id=None):
    """Return a room number not assigned to another patient."""
    while True:
        room_number = get_int_input(prompt)
        occupied = any(
            patient.room_number == room_number
            and patient.patient_id != current_patient_id
            for patient in patients.values()
        )
        if not occupied:
            return room_number
        print("This room is already occupied. Please choose another room.")




def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")



def get_valid_email(prompt):
    while True:
        email = get_non_empty_input(prompt)

        if "@" in email and "." in email.split("@")[-1]:
            return email

        print("Invalid email! Please enter a valid email address.")



from datetime import datetime


def get_valid_date(prompt):
    while True:
        date_input = get_non_empty_input(prompt)

        try:
            valid_date = datetime.strptime(date_input, "%d-%m-%Y")
            return valid_date.strftime("%d-%m-%Y")

        except ValueError:
            print("Invalid date! Please enter date in DD-MM-YYYY format.")



def get_valid_gender(prompt):
    while True:
        gender = get_non_empty_input(
            f"{prompt} (M = Male, F = Female): "
        ).lower()

        if gender in ("m", "male"):
            return "Male"

        elif gender in ("f", "female"):
            return "Female"

        print("Invalid gender! Please enter M/Male or F/Female.")
