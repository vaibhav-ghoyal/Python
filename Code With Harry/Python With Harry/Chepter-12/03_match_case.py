
def http_status(status):

    match status:
        case 200:
            return "OK"

        case 404:
            return "Not Found"
        
        case 500:
            return "Internal Server Error"
        
        case _:
            return "Unknown Status.!"
        

print("200-OK\n404-Not Found\n500-Internal Server Error")

n = int(input("Enter Above Number:"))
print(http_status(n))