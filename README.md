# Greeting-Service-Kata

## Falcon Clean Architecture - Exercises

This code defines a `Greetings` class that includes the following functionality:

- **Initialization**: 
  - Initializes an empty dictionary `greetings_storage`.
  - Calls the `load_config` method when an instance of the class is created.

- **`load_config` Method**:
  - Loads environment variables starting with the prefix `GREET_`.
  - Adds these variables to the `greetings_storage` dictionary.
  - Prints "GREETING DASHBOARD!" followed by the current `greetings_storage`.

- **`user_info` Method**:
  - Takes `lang` and `user` arguments.
  - Assigns them to `language` and `user_name` attributes of the instance.
  - Calls the `greet` method.

- **`greet` Method**:
  - Checks if the `language` attribute is a key in the `greetings_storage` dictionary.
  - If it is, prints the corresponding greeting with the `user_name`.
  - If not, prints "Sorry, greeting not available in" followed by the `language`.

- **`store` Method**:
  - Takes a dictionary `greets` and assigns it to the `greetings_storage` attribute.
  - Prints the updated `greetings_storage`.

- **Instance Creation**:
  - An instance of the `Greetings` class is created and assigned to the variable `greetObj`.

## Twelve-Factor App Principles

This implementation adheres to the Twelve-Factor App principles by:

- Storing greetings in environment variables (config) under the `GREET_` prefix.
- Loading the config in the constructor to initialize the greetings storage.
- Treating the greetings storage as an attached resource.
- Keeping the `greet` method stateless by only using `language` and `user_name` properties.
- Not using any backing services.
- Not providing any admin processes.

## Running the Code

To run this code:

1. Set environment variables in the format `GREET_LANGUAGE="GREETING_MESSAGE"`.
2. Run the script with Python.

```bash
python your_script_name.py
