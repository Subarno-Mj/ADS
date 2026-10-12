class Searching:

    my_list = [10, 15, 16, 78, 96, 45, 89, 100, 125, 112, 114, 145]

    #Linear search finction 
    def Linear_Search(self,target):
        print("This is linear searching....")

        # Take target value from the user
        user_input = int(input("Enter number to search: "))

        # Search for the target value
        for i in range(len(self.my_list)):
            if self.my_list[i] == user_input:
                print(f"Match found at index {i}")
                break
        else:
            print("Sorry, match not found!")

    #Binary search function
    def Binary_search(self, target):
        #sort the list
        self.my_list=sorted(self.my_list)
        low = 0
        high = len(self.my_list) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.my_list[mid] == target:
                return mid
            elif self.my_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1




# Create an object and call Linear_Search() or Binary_Search()
ob = Searching()
#ob.Linear_Search()
result_index=ob.Binary_search(15)

if result_index==-1:
    print("Match not found..")
else:
    print("Match found at index",result_index)