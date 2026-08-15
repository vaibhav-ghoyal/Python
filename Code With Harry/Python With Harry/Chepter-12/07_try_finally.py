def main():

    try:
        a = int(input("Hey, Enter a Number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I Am Inside Finally") 

main()
    