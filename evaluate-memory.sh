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
        test_files=("01_default_mem.py" "03_memory_optimized.py")
 
        # Loop through each test file
        for test_file in "${test_files[@]}"; do
            # Check if the file exists then do something with it
            if [ -f "$test_case/$tool/$test_file" ]; then
                # Run the script and collect the peak values in a list
                peak_values=0
                for i in {1..10}
                do
                    result=$(python3 ./"$test_case"/"$tool"/"$test_file" 2>&1)
                    if [ -z ${result+x} ] || [ "$result" == "" ]; then
                        :
                    else
                        # Extract the peak memory value from the result
                        peak=$(echo "$result" | grep -Po 'peak=\d+.\d+' | cut -d'=' -f 2)
                        
                        # Check if peak != 0
                        if [ -z ${peak+x} ]; then
                            :
                        else
                            # Sum of peak and peak_values
                            peak_values=$(echo "$peak_values + $peak" | bc -l)
                        fi
                    fi
                done
                # Calculate the average of peak values
                average=$(echo "$peak_values / 10" | bc -l)

                # Print the result in a table format
                printf "| %-10s | %-20s | %-20s | %-15s |\n" "$test_case" "$tool" "$test_file" "$average kB"
            fi
        done
    done
done