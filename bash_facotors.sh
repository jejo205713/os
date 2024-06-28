#!/bin/bash

# Function to find factors of a number
find_factors() {
    num=$1
    echo "Factors of $num are:"
    for (( i=1; i<=num; i++ ))
    do
        if (( num % i == 0 ))
        then
            echo $i
        fi
    done
}

# Read number from user
read -p "Enter a number: " number

# Find and print factors
find_factors $number
