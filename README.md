# Hi , Welcome to LotteryApp

# Instuctions to  run this app -

1. First need to install python3 ( https://www.python.org/downloads/ )
2. run: python --version // To verify python is working 
3. run: python -m pip --version // To verify pip  is working 
4. Download code from Git
5. run: cd LotteryApp
6. run: python -m pip install -r requirements.txt // To install requirements 
7. run: cd src 
8. run: python mainApp.py

# Instuctions to  run  Test cases -

1. Go back to root folder LotteryApp
2. python -m pytest 

# Folder Structure -
    
    LotteryApp
    |
    |_____src
    |      |  
    |      |___model\  
    |      |          \
    |      |             Has-a Relationship
    |      |           /                 
    |      |___service/
    |      |  
    |      |___util
    |       
    |____tests
    |       |  
    |       |___util
    |       |  
    |       |___service
    |         
    |
    |_______mainApp.py
