# Password Strength and Crack Time Estimator

## Overview

This project provides two Python scripts to analyze the strength of your passwords. These tools help you understand how secure your passwords are by calculating their entropy and estimating the time it would take to crack them using common hacking techniques.

## Features

- **Password Strength Analysis**: Evaluates the strength of a password and categorizes it as "Very Weak," "Weak," "Reasonable," "Strong," or "Very Strong."
- **Password Entropy Calculation**: Calculates the entropy of a password in bits, which is a measure of its randomness and unpredictability.
- **Crack Time Estimation**: Estimates the time it would take to crack a password using both CPU-based and GPU-based attacks.
- **User-Friendly**: Simple command-line interface that prompts for a password and provides a detailed analysis.

## Scripts

This repository contains two main scripts:

### 1. `password_Strength_checker.py`

This script focuses on calculating the entropy of a password and providing a strength rating. It's a great tool for quickly assessing how strong a password is without the crack time estimation.

### 2. `password_crack_time_checker.py`

This script provides a more in-depth analysis. In addition to calculating entropy and providing a strength rating, it also estimates the time it would take to crack the password using two different scenarios:

- **CPU-based attack**: Simulates a slower cracking speed (100 million guesses per second).
- **GPU-based attack**: Simulates a much faster cracking speed (1 trillion guesses per second).

## How to Use

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/password-analyzer.git
    cd password-analyzer
    ```

2.  **Run the scripts**:

    To check the strength of a password, run:
    ```bash
    python3 password_Strength_checker.py
    ```

    To get a more detailed analysis, including the estimated crack time, run:
    ```bash
    python3 password_crack_time_checker.py
    ```

3.  **Enter your password**:

    When prompted, enter the password you want to analyze and press Enter. The script will then display the analysis.

## Understanding the Output

- **Password Length**: The number of characters in your password.
- **Entropy (bits)**: A measure of the password's randomness. Higher entropy means a more secure password.
- **Strength Rating**: A qualitative assessment of the password's strength based on its entropy.
- **Estimated Crack Time**: The approximate time it would take to guess your password. This is provided for both slower (CPU) and faster (GPU) attacks to give you a better sense of your password's resilience.

## Author

By Abhrant Singh.
