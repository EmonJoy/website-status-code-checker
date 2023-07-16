import requests
import pyfiglet
""""
Testing in 2sites ==>
1. active site = https://www.teamtigerforce.com/
2. inactive or block site = http://www.chureyshiya.ga/

"""
print(pyfiglet.figlet_format("TTF_website status checker", font="digital"))
def main(url):
    try:
        get_req = requests.get(url).status_code
        if get_req == 200:
            print(f"This site is working properly\nsite's staus code is: {get_req}")
    except:
        print("Looks like this site isn't working properly or\nthe site is disabled")

url = input("Enter url: ")
if __name__ == '__main__':
    main(url)
    print("code by MR. Morningstar")
