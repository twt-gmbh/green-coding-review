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
        test_files=("01_default.py" "02_runtime_optimized.py")
 
        # Loop through each test file
        for test_file in "${test_files[@]}"; do
            # Check if the file exists then do something with it
            if [ -f "$test_case/$tool/$test_file" ]; then
                # Run the perf command
                result=$(sudo perf stat -e power/energy-pkg/ -a -r 10 python3 -X perf ./"$test_case"/"$tool"/"$test_file" 2>&1)
                
                # Extract the elapsed time value ignoring the deviation
                time_taken=$(echo "$result" | grep -Po '\d+.\d+ \+- \d+.\d+ seconds time elapsed' | cut -d' ' -f 1)

                # Print the result in a table format
                printf "| %-10s | %-20s | %-20s | %-20s |\n" "$test_case" "$tool" "$test_file" "$time_taken seconds"
            fi
        done
    done
done