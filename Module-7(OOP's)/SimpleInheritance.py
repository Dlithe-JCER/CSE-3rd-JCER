# SECTION -B
# # Simple Inheritance/Single Inheritance Example in Python
# class ChatGPT3_5: 
#     version = "3.5"
#     year=2022
#     @staticmethod
#     def chat():
#         return "Hello! I am ChatGPT version 3.5"
#     @staticmethod
#     def gptInfo():
#         return f"ChatGPT version {ChatGPT3_5.version} released in {ChatGPT3_5.year}"
# class ChatGPT4(ChatGPT3_5):
#     version = "4.0"
#     year=2024
#     @staticmethod
#     def gptInfo():
#         return f"ChatGPT version {ChatGPT4.version} released in {ChatGPT4.year}"
# c2=ChatGPT4()
# print(c2.chat())  



# SECTION -A
# Simple Inheritance/Single Inheritance Example in Python
class ChatGPT3_5:
    version='3.5'
    year=2022
    @staticmethod
    def chat():
        return "Hello! I am ChatGPT version 3.5"
    @staticmethod
    def displayInfo():
        return f"ChatGPT version {ChatGPT3_5.version} released in {ChatGPT3_5.year}"
class ChatGPT4(ChatGPT3_5):
    version='4.0'
    year=2024
    @staticmethod
    def displayInfo():
        return f"ChatGPT version {ChatGPT4.version} released in {ChatGPT4.year}"
c1=ChatGPT4()
print(c1.chat())