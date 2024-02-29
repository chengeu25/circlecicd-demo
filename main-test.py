from main import add

def testAdd():
    assert add(5,5) == 10
    print("Add Function works correctly")
    
if __name__ == "__main__":
    testAdd()