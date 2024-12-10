def convert_date(date):
    yyyy, mm, dd = date.split('-')
    return f'{dd}-{mm}-{yyyy}'

print(convert_date('2024-12-02'))