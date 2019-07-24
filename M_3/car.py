class Car:

    def __init__(self, regno , no_gears):            
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print(f"car with regno : {self.regno} already started......")
        else:
            print(f"car with regno : {self.regno} started......")
            self.is_started = True
    
    def stop(self):
        if self.is_started:
            print(f"car with regno : {self.regno} stopped......")
            self.is_started = False
        else:
             print(f"car with regno : {self.regno} already stopped......")
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f"car with regno : {self.regno} changed gear......")
            else:
                print(f"car with regno : {self.regno} already in top gear......")
        else:
            print(f"car with regno : {self.regno} already stoped so you can't change the gear...")

    def showInfo(self):
        print(f"{self.regno}, status - {self.is_started}, gear - {self.no_gears}, gear status - {self.c_gear}")