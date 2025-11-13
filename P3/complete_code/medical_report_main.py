# -*- coding: utf-8 -*-


def main():
    # Requesting the name
    name = input("What's your name? ")
    if name == "":
        print("Don't tell me you don't have a name")
    else:
        print("Hello " + name)

    # Requesting the age
    age_text = input("How old are you? ")
    age = int(age_text)
    if age >= 18:
        print("I see you are an adult")
    else:
        print("I see you are underage")

    # Requesting height and weight to calculate BMI
    height_text = input("How tall are you (in meters)? ")
    height = float(height_text)
    
    weight_text = input("How much do you weigh (in kg)? ")
    weight = float(weight_text)
    
    # Calculating BMI
    bmi = weight / (height * height)
    bmi_text = str(bmi)
    print("Your bmi is: " + bmi_text)

    # Asking if the user is a smoker
    smoker_text = input(
        "Write 'Y' if you are a smoker, enter any other value if you are not: "
    )
    smoker = smoker_text == "Y" or smoker_text == "y"

    if smoker:
        print("I see you are a smoker")
    else:
        print("I see you are not a smoker")

    print(
        "We are going to measure your heart rate at rest and after exercising, with this we will measure your heart rate range."
    )

    # Asking for heart rate at rest and after effort
    heart_beat_resting_text = input(
        "What is your resting heart rate? (in beats per minute) "
    )
    heart_beat_resting = int(heart_beat_resting_text)

    heart_beat_effort_text = input(
        "What is your heart rate after performing the first exercise? (in beats per minute) "
    )
    heart_beat_effort = int(heart_beat_effort_text)
    heart_beat_range = heart_beat_effort - heart_beat_resting
    print(f"Your heart rate range is: {heart_beat_range} beats per minute")

    # Measuring heart rate range again after another effort
    print(
        "We are going to measure your heart rate again after another effort, and check it again with your resting heart rate."
    )
    heart_beat_effort_text = input(
        "What is your heart rate after performing the second exercise? (in beats per minute) "
    )
    heart_beat_effort = int(heart_beat_effort_text)

    # Recalculating heart rate range (otherwise, it would be the same as before)
    heart_beat_range = heart_beat_effort - heart_beat_resting

    print(
        f"Your new heart rate range is: {heart_beat_range} beats per minute"
    )


if __name__ == "__main__":
    main()
