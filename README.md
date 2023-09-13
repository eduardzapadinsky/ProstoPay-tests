# Python Modules: `hashmap.py` and `users.py`

## `hashmap.py`

This module provides an efficient hash map with linear probing for collision handling. 
It supports key-value storage and updates, maintaining simplicity and robust testing.

- **Linear Probing:** Efficiently handles collisions.
- **Fixed-Size Array:** Simplifies implementation.
- **Efficient Hashing:** Evenly distributes keys.
- **Updates:** Properly updates existing keys.
- **Testing:** Comprehensive unit tests.
- **Simplicity:** Clear, concise, and maintainable code.
- **Default Size:** Size parameter (default: 10).

## `users.py`

This module defines a `UserDTO` data model and a `UserService` class for user management.

- **UserDTO:** Pydantic model with `id` and `name` attributes.
- **UserService:** Database interaction using SQLAlchemy's `AsyncSession`.

## Unittests for `hashmap.py` and `users.py`

Unit tests for the `hashmap.py` and `users.py` modules are provided to ensure the correctness and robustness of the implementations.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/eduardzapadinsky/ProstoPay-tests.git
   ```

2. Navigate to the project directory:

   ```shell
   cd ProstoPay-tests
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```
