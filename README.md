## Overview

The Points Management API allows users to manage points for different payers. Users can add points, spend points, and check their balance. This API is built using Django REST Framework.

## Features

- **Add Points**: Add a new transaction with the payer, points, and timestamp.
- **Spend Points**: Spend points starting with the earliest transaction.
- **Check Balance**: Retrieve the current balance of points for each payer.

## API Endpoints

### 1. Add Points
- **Endpoint**: `points/add`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "payer": "PAYER_NAME",
      "points": POINTS_AMOUNT,
      "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
  }
  ```

- **Example**:
  ```json
  {
      "payer": "DANNON",
      "points": 300,
      "timestamp": "2022-10-31T10:00:00Z"
  }
  ```

- **Response**:
  - **200 OK**: Transaction added successfully.
  - **400 Bad Request**: Not enough points for this payer (if trying to add negative points that exceed the balance).

### 2. Spend Points
- **Endpoint**: `points/spend`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "points": POINTS_AMOUNT
  }
  ```

- **Example**:
  ```json
  {
      "points": 500
  }
  ```

- **Response**:
  - **200 OK**: Points spent successfully with details of deductions.
  - **400 Bad Request**: Not enough points to spend.

### 3. Get Balance
- **Endpoint**: `points/balance`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns the current balance for each payer.
  
- **Example Response**:
  ```json
  {
      "DANNON": 300,
      "UNILEVER": 200,
      "MILLER COORS": 10000
  }
  ```

## Setup Instructions

### Prerequisites

- Download and install latest version of Python from the official website: python.org
- Download Postman from the official website: postman.com/downloads/

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   Mac:
   ```bash
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the migrations to set up the database:
   ```bash
   python3 manage.py migrate
   ```

5. Start the development server:
   ```bash
   python3 manage.py runserver
   ```

## Testing with Postman

You can use Postman to test the API endpoints. Here’s how:

### Step 1: Open Postman

1. Launch Postman application.

### Step 2: Testing Add Points

1. Set the method to `POST`.
2. Enter the URL: `http://localhost:8000/points/add`
3. Go to the **Body** tab.
4. Select **raw** and choose **JSON** from the dropdown.
5. Enter the request body in JSON format.
6. Click **Send**.

### Step 3: Testing Spend Points

1. Set the method to `POST`.
2. Enter the URL: `http://localhost:8000/points/spend`
3. Go to the **Body** tab.
4. Select **raw** and choose **JSON** from the dropdown.
5. Enter the request body in JSON format (specify the points to spend).
6. Click **Send**.

### Step 4: Testing Get Balance

1. Set the method to `GET`.
2. Enter the URL: `http://localhost:8000/points/balance`
3. Click **Send**.

## Clearing the Database for Retesting
If you want to clear your database to start fresh for retesting, you can follow these steps:

1. First exit out of the development server by:
- Pressing `Ctrl + C` on your keyboard. This will terminate the server process.

2. Clear the database
    ```bash
      python3 manage.py flush
    ```
- This command will remove all data from the database while keeping the database schema intact.
- You will be prompted to confirm this action by typing "yes".

## Exiting the Server and Virtual Environment,
To stop the development server running on your terminal, simply:
- Press `Ctrl + C` on your keyboard. This will terminate the server process.

To deactivate the virtual environment, run:
```bash
deactivate
```
This command will return you to your system's default environment.

### Notes

- Make sure your server is running before making requests.