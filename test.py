#!/usr/bin/env python3
"""
Test file for the calculate_pi_to_5th_digit function
"""

import sys
from main import calculate_pi_to_5th_digit


def test_pi_calculation():
    """Test that pi is calculated correctly to 5 decimal places"""
    result = calculate_pi_to_5th_digit()
    expected = 3.14159
    
    print(f"Calculated pi: {result}")
    print(f"Expected pi:   {expected}")
    
    # Test that the result matches expected value
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ Test passed: Pi calculated correctly to 5 decimal places!")
    
    # Additional checks
    assert isinstance(result, float), "Result should be a float"
    print("✓ Test passed: Result is a float type!")
    
    # Check that it's within reasonable bounds
    assert 3.14 < result < 3.15, "Pi should be between 3.14 and 3.15"
    print("✓ Test passed: Pi is within reasonable bounds!")
    
    return True


def test_pi_precision():
    """Test that the calculation has exactly 5 decimal places"""
    result = calculate_pi_to_5th_digit()
    
    # Convert to string and check decimal places
    result_str = str(result)
    if '.' in result_str:
        decimal_places = len(result_str.split('.')[1])
        print(f"Number of decimal places: {decimal_places}")
        assert decimal_places <= 5, f"Should have at most 5 decimal places, got {decimal_places}"
        print("✓ Test passed: Precision is correct!")
    
    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("Testing Pi Calculation Function")
    print("=" * 60)
    print()
    
    try:
        test_pi_calculation()
        print()
        test_pi_precision()
        print()
        print("=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print()
        print("=" * 60)
        print(f"Test failed: {e}")
        print("=" * 60)
        return 1
    except Exception as e:
        print()
        print("=" * 60)
        print(f"Unexpected error: {e}")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
