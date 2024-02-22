Based on the provided `main.py` script and the insights from `FUNCTIONS.py`, here's a structured documentation outline for your project, ready to be included in a `README.md` file:

---


# Kendall Tau distance calculator and Kendall Tau distance calculator extended over lists of occurrences of letters in files of different languages.

# Project: This project allows you to perform data cleaning, obtain statistics in the form of lists ranked by occurrences of letters of the alphabet, calculate Kendall's Tau distance, and extended Kendall's Tau distance, statistics, and statistical tests on these results.

## Overview

The project consists of several scripts, each handling different aspects of the data processing and analysis pipeline:
- **Data Cleaning and Summary Statistics**: Cleans provided `.txt` files and converts them into summarized statistics.
- **Matrix Calculation**: Generates matrices for Kendall Tau and Extended Kendall Tau calculations based on summarized data.
- **Statistical Analysis**: Calculates and aggregates statistics from the generated matrices.

## Dependencies


This project requires the following Python libraries:

- `itertools`: For efficient looping.
- `re`: For regular expression matching.
- `ast`: For safely evaluating strings containing Python expressions.
- `collections`: For high-performance container datatypes.
- `numpy`: For scientific computing with Python.
- `openpyxl`: For reading and writing Excel files.
- `scipy`: For scientific and technical computing.
- `os`: For interacting with the operating system.
- `pandas`: For data manipulation and analysis.

You can install most of these dependencies using pip (note: some of these come with Python standard library):


## Getting Started

1. **Data Preparation**: Place your `.txt` files in designated folders named after their respective categories (e.g., 'ES', 'PT', 'IN', etc.).


2. **Execution Steps**:
    - Run the `process_folder` function for each folder containing `.txt` files to clean data and calculate preliminary statistics.
    - Use the `aggregate` function to compile and summarize statistics across all folders.
    - Execute the `matrix` function to fill Excel matrices for KT and EKT data analysis. 
    - Copy data from outputkt.xlsx and outputekt.xlsx to previously formated outputkt_form.xlsx and outputekt_form.xlsx 
    - Perform statistical calculations using the `calculate_statistics` function for in-depth analysis.


## Usage

The `main.py` script orchestrates the project's workflow. Adjust the folder names and paths as necessary before execution.
Original data used in submited paper was provided in folders. Additional spreadsheets in Excel format can be found in the project's Root.


## Contributing

Contributions to improve the project are welcome. Please ensure to follow the project's coding standards and submit pull requests for any enhancements.

## License

This project is released into the public domain and is free of licenses. It can be used, modified, and distributed without any restrictions. For more details, please refer to the [Creative Commons CC0 declaration](https://creativecommons.org/share-your-work/public-domain/cc0/).


