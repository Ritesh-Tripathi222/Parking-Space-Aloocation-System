class ParkingLot:
    def __init__(self, slots):
        #Created DS for storing slot Status of slot, Vechile Number,Driver Age
        self.no_of_slots = slots
        self.flag = [0]*slots
        self.vechileNumber = [""]*slots
        self.driverAge = [0]*slots

    #Main Function to execute the task
    def execute_parking_ticket(self, file_line): 
        for i in range(1,file_line):
          query=inputList[i].split(" ")
          #Used if-elif-else ladder to identify commands and execute tasks accordingly
          if query[0].lower() == "park":
              self.Park(query)
          elif query[0].lower() == "slot_numbers_for_driver_of_age":
              self.Slot_numbers_for_driver_of_age(query)
          elif query[0].lower() == "slot_number_for_car_with_number":
              self.Slot_number_for_car_with_number(query)  
          elif query[0].lower() == "leave":
              self.Leave(query)
          elif query[0].lower()=="vehicle_registration_number_for_driver_of_age":
              self.Vehicle_registration_number_for_driver_of_age  (query)
          else:
              print("Invalid Command")


    #Park function to park arriving vehicle at closest slot from entrance
    def Park(self, query):
        slot=self.searchClosest(self.flag, self.no_of_slots)
        if slot != -1:
            self.flag[slot] = 1
            self.vechileNumber[slot] = query[1]
            self.driverAge[slot] = int(query[3])
            print("Car with vehicle registration number \"" + self.vechileNumber[slot] + "\" has been parked at slot number ",(slot+1))
        else:
            print("Parking is full")


    #Function to print all slot numbers for drivers who match the given age 
    def Slot_numbers_for_driver_of_age(self, query):
        age=int(query[1])
        ageSlot = self.listAsPerAge(self.flag,self.driverAge, age)
        if len(ageSlot) != 0:
            for i in range(len(ageSlot)-1):
                print(ageSlot[i],end=",")
                print(ageSlot[len(ageSlot)-1])
        else:
            print()

    #Function to print slot number of given v-number
    def Slot_number_for_car_with_number(self, query):
        vNumber = query[1]
        slotNumber = self.findSlot(self.vechileNumber,vNumber)
        if slotNumber != -1:
            print(slotNumber)
        else:
            print("Vechile not found")  

    #Function to print leaving car details and mark slot as empty
    def Leave(self, query):
        leavingSlot = int(query[1])-1
        status=self.leavingCar(self.flag, leavingSlot)
        if status == True:
            print("Slot number ",(leavingSlot+1)," vacated, the car with vehicle registration number \""+ self.vechileNumber[leavingSlot]+"\" left the space, the driver of the car was of age ",self.driverAge[leavingSlot])
        else:
            print("Slot already vacant")

    #Function to print list of V-registration numbers for given driver age    
    def Vehicle_registration_number_for_driver_of_age(self, query):
        age = int(query[1])
        vechileList = self.listAsPerVechileNumber(self.vechileNumber, age,self.driverAge, self.flag)
        if len(vechileList) != 0:
            for i in range(len(vechileList)-1):
              print(vechileList[i],end=",")
            print(vechileList[len(vechileList)-1])
        else:
            print()

    #Function to find closest possible slot for parking
    def searchClosest(self, flag,n):
      result =-1
      for i in range(n):
        if flag[i] == 0:
          result = i
          break
      return result

    #Function to create list of slots as per given driver age
    def listAsPerAge(self, flag,driverAge,age):
        li = []
        for i in range(0,6):
            if flag[i] == 1 and driverAge[i] == age:
              li.append(i+1)
        return li

    #Function to find slot of given v-number 
    def findSlot(self, vechileNumber,vNumber):
        find =-1
        for i in range(len(vechileNumber)):
            if vechileNumber[i] == vNumber:
              find = i+1
              return (find)

    #Function to empty slot of leaving car
    def leavingCar(self, flag,slot):
        if flag[slot] == 1:
            flag[slot] = 0
            return True
        return False

    #Function to create list of v-number as per given driver age
    def listAsPerVechileNumber(self, vechileNumber,age,driverAge,flag):
        li=[]
        for i in range(len(driverAge)):
            if flag[i] == 1 and driverAge[i] == age:
             li.append(vechileNumber[i])
        return li

if __name__=='__main__':
    inputText = open("input.txt","r")
    inputData = inputText.read()
    inputList = inputData.split("\n") 
    #Input split into seperate commands and stored in list
    inputText.close()
    file_lines = len(inputList)

    extract_slots = inputList[0].split(" ")
    slots = int(extract_slots[1]) 
    print('Created parking of ', slots ,' slots')
    ticket_obj=ParkingLot(slots)
    ticket_obj.execute_parking_ticket(file_lines)
