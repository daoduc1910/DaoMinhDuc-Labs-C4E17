import pyexcel

data = [
    {
        "Name": "Huyen",
        "Age": 23
    },
    {
        "Name": "Quan",
        "Age": 123
    },
    {
        "Name": "Tan",
        "Age": 43
    },
]

pyexcel.save_as(records = data, dest_file_name = "test.xlsx")
