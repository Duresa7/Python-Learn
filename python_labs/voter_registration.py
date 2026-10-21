"""Collect and validate voter registration information for a class exercise."""

STATES = (
    "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD "
    "MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC "
    "SD TN TX UT VT VA WA WV WI WY"
).split()
US_COUNTRIES = (
    "us", "usa", "u.s.", "u.s.a.", "united states", "united states of america"
)


def ask(prompt):
    """Require an answer and allow cancellation at every prompt."""
    while True:
        answer = input(prompt).strip()
        if answer.lower() == "quit":
            print("Registration canceled.")
            raise SystemExit
        if answer:
            return answer
        print("This field is required. Please try again.")


def get_age():
    """Ask again until the user enters a whole-number age from 0 to 120."""
    while True:
        try:
            age = int(ask("Age: "))
        except ValueError:
            print("Enter your age as a whole number.")
            continue
        if 0 <= age <= 120:
            return age
        print("Enter an age from 0 to 120.")


def main():
    """Check eligibility, collect the remaining details, and show a summary."""
    print("Welcome to the Python Voter Registration Application.")
    print("Class exercise only; this does not submit a real voter registration.")
    print("Type quit at any prompt to cancel.\n")

    first_name = ask("First name: ")
    last_name = ask("Last name: ")
    age = get_age()

    if age < 18:
        print("You must be at least 18 years old to register in this application.")
        return

    country = ask("Country of citizenship (for example, USA): ")
    if country.lower() not in US_COUNTRIES:
        print("You must be a U.S. citizen to register in this application.")
        return

    state = ask("State of residence (two letters): ").upper()
    while state not in STATES:
        print("Enter a valid two-letter U.S. state abbreviation, such as MD.")
        state = ask("State of residence (two letters): ").upper()

    zipcode = ask("ZIP code (five digits): ")
    while not (len(zipcode) == 5 and zipcode.isascii() and zipcode.isdigit()):
        print("Enter a five-digit ZIP code, such as 02108.")
        zipcode = ask("ZIP code (five digits): ")

    print("\nCongratulations! You completed the practice registration.")
    print(f"Name: {first_name} {last_name}")
    print(f"Age: {age}")
    print("Country of citizenship: United States")
    print(f"State: {state}")
    print(f"ZIP code: {zipcode}")


if __name__ == "__main__":
    main()
