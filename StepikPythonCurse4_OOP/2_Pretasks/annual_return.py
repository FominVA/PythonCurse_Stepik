def annual_return(start, percent, years):
    while years > 0:
        yield start*(100+percent)/100
        years -= 1
