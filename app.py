# from flask import Flask, render_template

# app = Flask(__name__)

# # Mock data
# mockData = [
#     {"id": 1, "name": "Alice Johnson", "age": 28, "role": "Engineer", "hireDate": "2022-01-15", "isActive": True, "salary": 85000, "department": "Development", "projectsCompleted": 5, "lastLogin": "2024-07-28T14:48:00.000Z", "accessLevel": "Admin"},
#     {"id": 2, "name": "Bob Smith", "age": 34, "role": "Manager", "hireDate": "2020-06-30", "isActive": False, "salary": 95000, "department": "Operations", "projectsCompleted": 10, "lastLogin": "2024-07-30T09:21:00.000Z", "accessLevel": "User"},
#     {"id": 3, "name": "Charlie Rose", "age": 22, "role": "Intern", "hireDate": "2023-03-01", "isActive": True, "salary": 45000, "department": "Development", "projectsCompleted": 1, "lastLogin": "2024-07-29T17:03:00.000Z", "accessLevel": "User"},
#     {"id": 4, "name": "David Green", "age": 40, "role": "Director", "hireDate": "2018-11-20", "isActive": True, "salary": 120000, "department": "Management", "projectsCompleted": 20, "lastLogin": "2024-07-27T12:35:00.000Z", "accessLevel": "Admin"},
#     {"id": 5, "name": "Eva White", "age": 30, "role": "Designer", "hireDate": "2021-05-15", "isActive": True, "salary": 70000, "department": "Design", "projectsCompleted": 8, "lastLogin": "2024-07-31T10:15:00.000Z", "accessLevel": "User"},
#     {"id": 6, "name": "Frank Black", "age": 29, "role": "Engineer", "hireDate": "2019-09-17", "isActive": True, "salary": 80000, "department": "Development", "projectsCompleted": 6, "lastLogin": "2024-07-25T11:45:00.000Z", "accessLevel": "User"},
#     {"id": 7, "name": "Grace Brown", "age": 26, "role": "Engineer", "hireDate": "2021-04-10", "isActive": False, "salary": 78000, "department": "Development", "projectsCompleted": 4, "lastLogin": "2024-07-20T09:00:00.000Z", "accessLevel": "User"},
#     {"id": 8, "name": "Hank Green", "age": 45, "role": "Senior Manager", "hireDate": "2017-03-25", "isActive": True, "salary": 110000, "department": "Operations", "projectsCompleted": 15, "lastLogin": "2024-07-29T13:22:00.000Z", "accessLevel": "Admin"},
#     {"id": 9, "name": "Ivy Blue", "age": 31, "role": "Designer", "hireDate": "2019-08-05", "isActive": True, "salary": 72000, "department": "Design", "projectsCompleted": 7, "lastLogin": "2024-07-28T08:48:00.000Z", "accessLevel": "User"},
#     {"id": 10, "name": "Jack White", "age": 37, "role": "Product Manager", "hireDate": "2020-02-20", "isActive": False, "salary": 95000, "department": "Product", "projectsCompleted": 12, "lastLogin": "2024-07-26T15:18:00.000Z", "accessLevel": "Admin"},
#     {"id": 11, "name": "Kara Black", "age": 33, "role": "Engineer", "hireDate": "2018-12-12", "isActive": True, "salary": 85000, "department": "Development", "projectsCompleted": 9, "lastLogin": "2024-07-29T12:00:00.000Z", "accessLevel": "User"},
#     {"id": 12, "name": "Leo Green", "age": 27, "role": "Designer", "hireDate": "2021-01-30", "isActive": True, "salary": 68000, "department": "Design", "projectsCompleted": 3, "lastLogin": "2024-07-28T16:15:00.000Z", "accessLevel": "User"},
#     {"id": 13, "name": "Mona Blue", "age": 36, "role": "Engineer", "hireDate": "2019-11-18", "isActive": True, "salary": 87000, "department": "Development", "projectsCompleted": 11, "lastLogin": "2024-07-30T14:50:00.000Z", "accessLevel": "User"},
#     {"id": 14, "name": "Nina Brown", "age": 25, "role": "Intern", "hireDate": "2023-04-14", "isActive": True, "salary": 42000, "department": "Development", "projectsCompleted": 2, "lastLogin": "2024-07-31T11:00:00.000Z", "accessLevel": "User"},
#     {"id": 15, "name": "Oscar White", "age": 42, "role": "Director", "hireDate": "2016-05-11", "isActive": True, "salary": 125000, "department": "Management", "projectsCompleted": 22, "lastLogin": "2024-07-29T09:33:00.000Z", "accessLevel": "Admin"}
# ]

# @app.route('/')
# def index():
#     return render_template('index.html', data=mockData)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Alice Johnson", "age": 28, "role": "Engineer", "hireDate": "2022-01-15", "isActive": True, "salary": 85000, "department": "Development", "projectsCompleted": 5, "lastLogin": "2024-07-28T14:48:00.000Z", "accessLevel": "Admin"},
    {"id": 2, "name": "Bob Smith", "age": 34, "role": "Manager", "hireDate": "2020-06-30", "isActive": False, "salary": 95000, "department": "Operations", "projectsCompleted": 10, "lastLogin": "2024-07-30T09:21:00.000Z", "accessLevel": "User"},
    {"id": 3, "name": "Charlie Rose", "age": 22, "role": "Intern", "hireDate": "2023-03-01", "isActive": True, "salary": 45000, "department": "Development", "projectsCompleted": 1, "lastLogin": "2024-07-29T17:03:00.000Z", "accessLevel": "User"},
    {"id": 4, "name": "David Green", "age": 40, "role": "Director", "hireDate": "2018-11-20", "isActive": True, "salary": 120000, "department": "Management", "projectsCompleted": 20, "lastLogin": "2024-07-27T12:35:00.000Z", "accessLevel": "Admin"},
    {"id": 5, "name": "Eva White", "age": 30, "role": "Designer", "hireDate": "2021-05-15", "isActive": True, "salary": 70000, "department": "Design", "projectsCompleted": 8, "lastLogin": "2024-07-31T10:15:00.000Z", "accessLevel": "User"},
    {"id": 6, "name": "Frank Black", "age": 29, "role": "Engineer", "hireDate": "2019-09-17", "isActive": True, "salary": 80000, "department": "Development", "projectsCompleted": 6, "lastLogin": "2024-07-25T11:45:00.000Z", "accessLevel": "User"},
    {"id": 7, "name": "Grace Brown", "age": 26, "role": "Engineer", "hireDate": "2021-04-10", "isActive": False, "salary": 78000, "department": "Development", "projectsCompleted": 4, "lastLogin": "2024-07-20T09:00:00.000Z", "accessLevel": "User"},
    {"id": 8, "name": "Hank Green", "age": 45, "role": "Senior Manager", "hireDate": "2017-03-25", "isActive": True, "salary": 110000, "department": "Operations", "projectsCompleted": 15, "lastLogin": "2024-07-29T13:22:00.000Z", "accessLevel": "Admin"},
    {"id": 9, "name": "Ivy Blue", "age": 31, "role": "Designer", "hireDate": "2019-08-05", "isActive": True, "salary": 72000, "department": "Design", "projectsCompleted": 7, "lastLogin": "2024-07-28T08:48:00.000Z", "accessLevel": "User"},
    {"id": 10, "name": "Jack White", "age": 37, "role": "Product Manager", "hireDate": "2020-02-20", "isActive": False, "salary": 95000, "department": "Product", "projectsCompleted": 12, "lastLogin": "2024-07-26T15:18:00.000Z", "accessLevel": "Admin"},
    {"id": 11, "name": "Kara Black", "age": 33, "role": "Engineer", "hireDate": "2018-12-12", "isActive": True, "salary": 85000, "department": "Development", "projectsCompleted": 9, "lastLogin": "2024-07-29T12:00:00.000Z", "accessLevel": "User"},
    {"id": 12, "name": "Leo Green", "age": 27, "role": "Designer", "hireDate": "2021-01-30", "isActive": True, "salary": 68000, "department": "Design", "projectsCompleted": 3, "lastLogin": "2024-07-28T16:15:00.000Z", "accessLevel": "User"},
    {"id": 13, "name": "Mona Blue", "age": 36, "role": "Engineer", "hireDate": "2019-11-18", "isActive": True, "salary": 87000, "department": "Development", "projectsCompleted": 11, "lastLogin": "2024-07-30T14:50:00.000Z", "accessLevel": "User"},
    {"id": 14, "name": "Nina Brown", "age": 25, "role": "Intern", "hireDate": "2023-04-14", "isActive": True, "salary": 42000, "department": "Development", "projectsCompleted": 2, "lastLogin": "2024-07-31T11:00:00.000Z", "accessLevel": "User"},
    {"id": 15, "name": "Oscar White", "age": 42, "role": "Director", "hireDate": "2016-05-11", "isActive": True, "salary": 125000, "department": "Management", "projectsCompleted": 22, "lastLogin": "2024-07-29T09:33:00.000Z", "accessLevel": "Admin"},
    {"id": 16, "name": "Oscar White", "age": 42, "role": "Director", "hireDate": "2016-05-11", "isActive": None, "salary": 125000, "department": "Management", "projectsCompleted": 22, "lastLogin": "2024-07-29T09:33:00.000Z", "accessLevel": "Admin"}
]



def sort_data(data, col_name, sort_order):
    if col_name not in data[0]:
        return data
    
    return sorted(data, key=lambda x: x[col_name], reverse=(sort_order == 'desc'))


def search_data(data, search_term):
    if not search_term:
        return data
    
    search_term = search_term.lower()
    return [item for item in data if any(search_term in str(value).lower() for value in item.values())]

@app.route('/')
def index():
    # Get filter parameters
    filter_type = request.args.get('filter-type')
    col_name = request.args.get('column-name')
    fil_val = request.args.get('filter-value')
    fil_cond = request.args.get('filter-condition')
    sort_by = request.args.get('sort-by')
    sort_col = request.args.get('column-name')
    search_term = request.args.get('search')

    fil_data = data

    if filter_type and col_name:
        if filter_type == 'integer':
            try:
                fil_val = int(fil_val)
                if col_name == 'age':
                    if fil_cond == 'equals':
                        fil_data = [item for item in fil_data if item['age'] == fil_val]
                    elif fil_cond == 'lessThan':
                        fil_data = [item for item in fil_data if item['age'] < fil_val]
                    elif fil_cond == 'lessThanOrEqual':
                        fil_data = [item for item in fil_data if item['age'] <= fil_val]
                    elif fil_cond == 'greaterThan':
                        fil_data = [item for item in fil_data if item['age'] > fil_val]
                    elif fil_cond == 'greaterThanOrEqual':
                        fil_data = [item for item in fil_data if item['age'] >= fil_val]
                    elif fil_cond == 'range':
                        range_values = fil_val.split(',')
                        if len(range_values) == 2:
                            start, end = map(int, range_values)
                            fil_data = [item for item in fil_data if start <= item['age'] <= end]
                    elif fil_cond == 'notEqual':
                        fil_data = [item for item in fil_data if item['age'] != fil_val]
                
                elif col_name == 'salary':
                    if fil_cond == 'equals':
                        fil_data = [item for item in fil_data if item['salary'] == fil_val]
                    elif fil_cond == 'lessThan':
                        fil_data = [item for item in fil_data if item['salary'] < fil_val]
                    elif fil_cond == 'lessThanOrEqual':
                        fil_data = [item for item in fil_data if item['salary'] <= fil_val]
                    elif fil_cond == 'greaterThan':
                        fil_data = [item for item in fil_data if item['salary'] > fil_val]
                    elif fil_cond == 'greaterThanOrEqual':
                        fil_data = [item for item in fil_data if item['salary'] >= fil_val]
                    elif fil_cond == 'range':
                        range_values = fil_val.split(',')
                        if len(range_values) == 2:
                            start, end = map(int, range_values)
                            fil_data = [item for item in fil_data if start <= item['salary'] <= end]
                    elif fil_cond == 'notEqual':
                        fil_data = [item for item in fil_data if item['salary'] != fil_val]
                
                elif col_name == 'projectsCompleted':
                    if fil_cond == 'equals':
                        fil_data = [item for item in fil_data if item['projectsCompleted'] == fil_val]
                    elif fil_cond == 'lessThan':
                        fil_data = [item for item in fil_data if item['projectsCompleted'] < fil_val]
                    elif fil_cond == 'lessThanOrEqual':
                        fil_data = [item for item in fil_data if item['projectsCompleted'] <= fil_val]
                    elif fil_cond == 'greaterThan':
                        fil_data = [item for item in fil_data if item['projectsCompleted'] > fil_val]
                    elif fil_cond == 'greaterThanOrEqual':
                        fil_data = [item for item in fil_data if item['projectsCompleted'] >= fil_val]
                    elif fil_cond == 'range':
                        range_values = fil_val.split(',')
                        if len(range_values) == 2:
                            start, end = map(int, range_values)
                            fil_data = [item for item in fil_data if start <= item['projectsCompleted'] <= end]
                    elif fil_cond == 'notEqual':
                        fil_data = [item for item in fil_data if item['projectsCompleted'] != fil_val]
                
                elif col_name == 'id':
                    if fil_cond == 'equals':
                        fil_data = [item for item in fil_data if item['id'] == fil_val]
                    elif fil_cond == 'lessThan':
                        fil_data = [item for item in fil_data if item['id'] < fil_val]
                    elif fil_cond == 'lessThanOrEqual':
                        fil_data = [item for item in fil_data if item['id'] <= fil_val]
                    elif fil_cond == 'greaterThan':
                        fil_data = [item for item in fil_data if item['id'] > fil_val]
                    elif fil_cond == 'greaterThanOrEqual':
                        fil_data = [item for item in fil_data if item['id'] >= fil_val]
                    elif fil_cond == 'range':
                        range_values = fil_val.split(',')
                        if len(range_values) == 2:
                            start, end = map(int, range_values)
                            fil_data = [item for item in fil_data if start <= item['id'] <= end]
                    elif fil_cond == 'notEqual':
                        fil_data = [item for item in fil_data if item['id'] != fil_val]

            except ValueError:
                pass

        elif filter_type == 'string':
            if col_name == 'name':
                if fil_cond == 'contains':
                    fil_data = [item for item in fil_data if fil_val in item['name']]
                elif fil_cond == 'notContains':
                    fil_data = [item for item in fil_data if fil_val not in item['name']]
                elif fil_cond == 'equals':
                    fil_data = [item for item in fil_data if item['name'] == fil_val]
                elif fil_cond == 'notEqual':
                    fil_data = [item for item in fil_data if item['name'] != fil_val]
                elif fil_cond == 'startsWith':
                    fil_data = [item for item in fil_data if item['name'].startswith(fil_val)]
                elif fil_cond == 'endsWith':
                    fil_data = [item for item in fil_data if item['name'].endswith(fil_val)]
                elif fil_cond == 'isNull':
                    fil_data = [item for item in fil_data if item['name'] is None]
                elif fil_cond == 'isNotNull':
                    fil_data = [item for item in fil_data if item['name'] is not None]
            
            elif col_name == 'role':
                if fil_cond == 'contains':
                    fil_data = [item for item in fil_data if fil_val in item['role']]
                elif fil_cond == 'notContains':
                    fil_data = [item for item in fil_data if fil_val not in item['role']]
                elif fil_cond == 'equals':
                    fil_data = [item for item in fil_data if item['role'] == fil_val]
                elif fil_cond == 'notEqual':
                    fil_data = [item for item in fil_data if item['role'] != fil_val]
                elif fil_cond == 'startsWith':
                    fil_data = [item for item in fil_data if item['role'].startswith(fil_val)]
                elif fil_cond == 'endsWith':
                    fil_data = [item for item in fil_data if item['role'].endswith(fil_val)]
                elif fil_cond == 'isNull':
                    fil_data = [item for item in fil_data if item['role'] is None]
                elif fil_cond == 'isNotNull':
                    fil_data = [item for item in fil_data if item['role'] is not None]
                
            elif col_name == 'department':
                if fil_cond == 'contains':
                    fil_data = [item for item in fil_data if fil_val in item['department']]
                elif fil_cond == 'notContains':
                    fil_data = [item for item in fil_data if fil_val not in item['department']]
                elif fil_cond == 'equals':
                    fil_data = [item for item in fil_data if item['department'] == fil_val]
                elif fil_cond == 'notEqual':
                    fil_data = [item for item in fil_data if item['department'] != fil_val]
                elif fil_cond == 'startsWith':
                    fil_data = [item for item in fil_data if item['department'].startswith(fil_val)]
                elif fil_cond == 'endsWith':
                    fil_data = [item for item in fil_data if item['department'].endswith(fil_val)]
                elif fil_cond == 'isNull':
                    fil_data = [item for item in fil_data if item['department'] is None]
                elif fil_cond == 'isNotNull':
                    fil_data = [item for item in fil_data if item['department'] is not None]
            
            elif col_name == 'accessLevel':
                if fil_cond == 'contains':
                    fil_data = [item for item in fil_data if fil_val in item['accessLevel']]
                elif fil_cond == 'notContains':
                    fil_data = [item for item in fil_data if fil_val not in item['accessLevel']]
                elif fil_cond == 'equals':
                    fil_data = [item for item in fil_data if item['accessLevel'] == fil_val]
                elif fil_cond == 'notEqual':
                    fil_data = [item for item in fil_data if item['accessLevel'] != fil_val]
                elif fil_cond == 'startsWith':
                    fil_data = [item for item in fil_data if item['accessLevel'].startswith(fil_val)]
                elif fil_cond == 'endsWith':
                    fil_data = [item for item in fil_data if item['accessLevel'].endswith(fil_val)]
                elif fil_cond == 'isNull':
                    fil_data = [item for item in fil_data if item['accessLevel'] is None]
                elif fil_cond == 'isNotNull':
                    fil_data = [item for item in fil_data if item['accessLevel'] is not None]

            elif col_name == 'lastLogin':
                if fil_cond == 'contains':
                    fil_data = [item for item in fil_data if fil_val in item['lastLogin']]
                elif fil_cond == 'notContains':
                    fil_data = [item for item in fil_data if fil_val not in item['lastLogin']]
                elif fil_cond == 'equals':
                    fil_data = [item for item in fil_data if item['lastLogin'] == fil_val]
                elif fil_cond == 'notEqual':
                    fil_data = [item for item in fil_data if item['lastLogin'] != fil_val]
                elif fil_cond == 'startsWith':
                    fil_data = [item for item in fil_data if item['lastLogin'].startswith(fil_val)]
                elif fil_cond == 'endsWith':
                    fil_data = [item for item in fil_data if item['lastLogin'].endswith(fil_val)]
                elif fil_cond == 'isNull':
                    fil_data = [item for item in fil_data if item['lastLogin'] is None]
                elif fil_cond == 'isNotNull':
                    fil_data = [item for item in fil_data if item['lastLogin'] is not None]

        elif filter_type == 'date':
            from datetime import datetime
            try:
                fil_val = datetime.strptime(fil_val, '%Y-%m-%d')
                if col_name == 'hireDate':
                    if fil_cond == 'equals':
                        fil_data = [item for item in fil_data if datetime.strptime(item['hireDate'], '%Y-%m-%d') == fil_val]
                    elif fil_cond == 'lessThan':
                        fil_data = [item for item in fil_data if datetime.strptime(item['hireDate'], '%Y-%m-%d') < fil_val]
                    elif fil_cond == 'lessThanOrEqual':
                        fil_data = [item for item in fil_data if datetime.strptime(item['hireDate'], '%Y-%m-%d') <= fil_val]
                    elif fil_cond == 'greaterThan':
                        fil_data = [item for item in fil_data if datetime.strptime(item['hireDate'], '%Y-%m-%d') > fil_val]
                    elif fil_cond == 'greaterThanOrEqual':
                        fil_data = [item for item in fil_data if datetime.strptime(item['hireDate'], '%Y-%m-%d') >= fil_val]
                    elif fil_cond == 'dateRange':
                        range_values = fil_val.split(',')
                        if len(range_values) == 2:
                            start, end = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in range_values]
                            fil_data = [item for item in fil_data if start <= datetime.strptime(item['hireDate'], '%Y-%m-%d') <= end]
                    elif fil_cond == 'notEqual':
                        fil_data = [item for item in fil_data if datetime.strptime(item['hireDate'], '%Y-%m-%d') != fil_val]
                    elif fil_cond == 'isNull':
                        fil_data = [item for item in fil_data if item['hireDate'] is None]
                    elif fil_cond == 'isNotNull':
                        fil_data = [item for item in fil_data if item['hireDate'] is not None]
            except ValueError:
                pass

        elif filter_type == 'boolean':
            if col_name == 'isActive':
                if fil_cond == 'equals':
                    fil_data = [item for item in fil_data if item['isActive'] == (fil_val.lower() == 'true')]
                elif fil_cond == 'isNull':
                    fil_data = [item for item in fil_data if item['isActive'] is None]
                elif fil_cond == 'isNotNull':
                    fil_data = [item for item in fil_data if item['isActive'] is not None]


     # Search data
    fil_data = search_data(fil_data, search_term)

    if sort_col:
        fil_data = sort_data(fil_data, sort_col, sort_by)
    return render_template('index.html', data=fil_data)

if __name__ == '__main__':
    app.run(debug=True)



   
   






