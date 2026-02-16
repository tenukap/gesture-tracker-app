#finger movement detection function 
def movement_fingers(CMC,MCP,IP,TIP):
   if IP.x >0.5 and  MCP.x >0.5 and CMC.x >0.5 and TIP.x > 0.5 :
          print("thumb is moving to the right")
   elif IP.x ==0.5 and MCP.x == 0.5 and  CMC.x == 0.5 and TIP.x == 0.5 :
        print("thumb is in the middle ") 
   else:
          print("thumb is moving to left")