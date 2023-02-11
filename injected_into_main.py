# -----------------------------------------
# injected_into_main.py
def injected_into_main():
    print("In injected_into_main")
    with open("/tmp/aa", "a") as ff:
        ff.write("test in injected_into_main\n")


# injected_into_main()
# -----------------------------------------
