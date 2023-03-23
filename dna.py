import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database/.csv sequences/.txt")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1], "r") as database_file:
        database_reader = csv.reader(database_file)
        database = list(database_reader)
        # Extract the STRs from the first row of the database
        str_sequences = database[0][1:]
    
    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence_file:
        dna_sequence = sequence_file.readline().rstrip()

    # Find longest match of each STR in DNA sequence
    longest_str_counts = []
    for str_seq in str_sequences:
        longest_str_counts.append(str(longest_match(dna_sequence, str_seq)))

    # Check database for matching profiles
    for i, row in enumerate(database[1:]):
        if row[1:] == longest_str_counts:
            print(row[0])
            return
        else:
            print("No Match for", row[0])

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
