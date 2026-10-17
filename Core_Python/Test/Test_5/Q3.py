Data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000]  
]

Data.sort(key=lambda emp: emp[2])

print(Data)