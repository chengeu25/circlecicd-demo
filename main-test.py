from main import add

def testAdd():
    assert add(2, 3) == 5
    print("Add Function works correctly")
    
if __name__ == "__main__":
    testAdd()