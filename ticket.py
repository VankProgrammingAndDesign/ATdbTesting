class Ticket:
  def __init__(self,ticketInfo):
    self.ticketNum = ticketInfo["Ticket Number"]
    self.deviceSN = ticketInfo['Installed Asset Serial Number']
    self.status = ticketInfo["Status"]
    self.school = ticketInfo["Client"]
    self.model = ticketInfo["Title"]
    self.notes = ticketInfo["Description"]
    self.parts = ticketInfo["partsList"]

  #
  def printTicket(self):
    print("Ticket Number: "+ self.ticketNum)
    print("Status:  "+ self.status)
    print("School:  "+ self.school)
    print("Model: "+ self.model)
    print("Notes: "+ self.notes)
    print("Serial Number: "+ self.deviceSN)
    #print(self.parts)
