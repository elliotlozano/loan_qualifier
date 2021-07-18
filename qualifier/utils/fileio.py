# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(output_path):
    
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.

    Returns:
        exports qualifying loans to csv file
    """
    
    #making a header for the CSV file
    header = ["Institution", "Max Loan", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    #using a with-open function to write data from for-loop into new CSV file
    with open(output_path, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for row in csvwriter:
            csvwriter.writerow(row)