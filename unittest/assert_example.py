def examples():
    try:
        assert 1+1 ==3, "Error"
    except AssertionError as e:
        print(e)

examples()