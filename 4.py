def meteo_measurements(file):
    meteo = open(file,'r')
    measurements = len(meteo.readlines())
    print("number of measurements:", measurements)

meteo_measurements("meteo.txt")

# def temperature(file):
#     x = []
#     meteo1 = open(file, 'r')
#     lines = len(meteo1.readlines())
#     for i in lines:
#         z = meteo1.readline(i)
#         splitting = z.split(" ")
#         return splitting[-2]
#
# print(temperature("meteo.txt")
#                 ?????????????????

