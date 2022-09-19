class Ticket:
  def __init__(self,ticketInfo):
    self.ticketNum = ticketInfo["Ticket Number"]
    self.deviceSN = ticketInfo['Installed Asset Serial Number']
    
    print(self.ticketNum + " Serial Number is:  "+ self.deviceSN)
