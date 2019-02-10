# Write some code to flatten an array of arbitrarily nested arrays of integers into a flat array of integers 
# (e.g., [[1,2,['foo']],4] -> [1,2,'foo',4].
from typing import List
#Assuming valid input 
def flatten(toFlatten : List[int] = []):
    #Checking input is correct
    assert isinstance(toFlatten,list)
    flattened = []
    for element in toFlatten:
        if isinstance(element,list):
            # Flatten the element with a recursive call, then combine the two arrays
            flattened.extend(flatten(element))
        else:
            # No recursive call needed, can simply add the element
            flattened.append(element)
    return flattened
    
    
def base_tester(expected, toFlatten):
    actual = flatten(toFlatten)
    assert expected == actual

def test_easy_path():
    toFlatten = [[1,2,3],[4,5,6]]
    expected = [1,2,3,4,5,6]
    base_tester(expected,toFlatten)

def test_multiple_levels():
    toFlatten = [4,[1,2,[3,[4,[5]]]]]
    expected = [4,1,2,3,4,5]
    base_tester(expected,toFlatten)

def test_empty_arr():
    toFlatten = [[[[[]]]],[[[]]],[[],[]]]
    expected = []
    base_tester(expected,toFlatten)

def test_noop():
    toFlatten = [5,4,3,2,1]
    expected = [5,4,3,2,1]
    base_tester(expected,toFlatten)

def ensure_tests_throw():
    toFlatten = [1,2,3,4,5]
    expected = []
    base_tester(expected,toFlatten)

def main():
    print("Flattening arrays: test cases")
    test_easy_path()
    test_multiple_levels()
    test_empty_arr()
    test_noop()
    #Uncomment to see test failure
    #ensure_tests_throw()
    print("Tests pass!")


if __name__ == "__main__":
    main()
