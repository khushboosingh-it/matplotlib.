import matplotlib.pyplot as plt

x = ["day1","day2","day3","day4"]
y = [30,45,50,65]
plt.plot( x,y ,label="marks")
plt.xlabel("days")
plt.ylabel("increses of marks")
plt.title("marks progress")
plt.legend()
plt.show()
