from SpreadSheetController import SpreadSheetController

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetController()
    while True:
        spreadsheetcontroller.showMenu()
        try:
            spreadsheetcontroller.insertCommand()
        except Exception as Error:
            print(Error.message)
        
