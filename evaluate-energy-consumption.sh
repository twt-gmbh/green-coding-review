#!/bin/bash
 
# Define the top-level test case directories
test_cases=("cookies" "median" "network" "search" "sort" "sum")
 
# Loop through each test case
for test_case in "${test_cases[@]}"; do
    # Get a list of tools in the test case directory
    tools=($(ls "$test_case"))
 
    # Loop through each tool
    for tool in "${tools[@]}"; do
        # Get a list of test files for the tool
        test_files=("01_default_optimized" "05_energy_optimized")
 
        # Loop through each test file
        for test_file in "${test_files[@]}"; do
            # Run the perf command
            result=$(sudo perf stat -e power/energy-pkg/ -a -r 1 python3 -X perf ./"$test_case"/"$tool"/"$test_file" 2>&1)
            # echo "$result"
            # Extract the energy consumption value (example line: "10.123 Joules power/energy-pkg/")
            energy_consumed=$(echo "$result" | grep -Po '(\d+.\d+) Joules power/energy-pkg/')
 
            # Print the result in a table format
            printf "| %-10s | %-20s | %-20s | %-10s |\n" "$test_case" "$tool" "$test_file" "$energy_consumed"
        done
    done
done