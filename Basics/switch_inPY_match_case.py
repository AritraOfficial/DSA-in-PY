# class Solution():
#     def whichWeekDay(self, day):
#         match (day):
#             case 1:
#                 print("Monday")
#             case 2:
#                 print("Tuesday")
#             case 3:
#                 print("Wednesday")
#             case 4:
#                 print("Thrusday")
#             case 5:
#                 print("Friday")
#             case 6:
#                 print("Saterday")
#             case 7:
#                 print("Sunday")
#             case _:
#                 print("Invalid")
#
# d = Solution()
# d.whichWeekDay(1)
class Solution:
    def whichWeekDay(self, day):
        switch = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        print(switch.get(day, "Invalid"))
d = Solution()
d.whichWeekDay(4)