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
    {"id": 15, "name": "Oscar White", "age": 42, "role": "Director", "hireDate": "2016-05-11", "isActive": True, "salary": 125000, "department": "Management", "projectsCompleted": 22, "lastLogin": "2024-07-29T09:33:00.000Z", "accessLevel": "Admin"}
]

@app.route('/')
def index():
    # Get filter parameters
    filter_type = request.args.get('filter-type')
    column_name = request.args.get('column-name')
    filter_value = request.args.get('filter-value')
    filter_condition = request.args.get('filter-condition')

    filtered_data = data


    if filter_type and column_name:
        if filter_type == 'integer':
            try:
                filter_value = int(filter_value)
                if column_name == 'age':
                    if filter_condition == 'equals':
                        filtered_data = [item for item in filtered_data if item['age'] == filter_value]
                    elif filter_condition == 'lessThan':
                        filtered_data = [item for item in filtered_data if item['age'] < filter_value]
                    elif filter_condition == 'lessThanOrEqual':
                        filtered_data = [item for item in filtered_data if item['age'] <= filter_value]
                    elif filter_condition == 'greaterThan':
                        filtered_data = [item for item in filtered_data if item['age'] > filter_value]
                    elif filter_condition == 'greaterThanOrEqual':
                        filtered_data = [item for item in filtered_data if item['age'] >= filter_value]
                    elif filter_condition == 'range':
                        range_values = filter_value.split(',')
                        if len(range_values) == 2:
                            start, end = map(int, range_values)
                            filtered_data = [item for item in filtered_data if start <= item['age'] <= end]
                    elif filter_condition == 'notEqual':
                        filtered_data = [item for item in filtered_data if item['age'] != filter_value]
             

            except ValueError:
                pass

        elif filter_type == 'string':
            if column_name == 'name':
                if filter_condition == 'contains':
                    filtered_data = [item for item in filtered_data if filter_value in item['name']]
                elif filter_condition == 'notContains':
                    filtered_data = [item for item in filtered_data if filter_value not in item['name']]
                elif filter_condition == 'equals':
                    filtered_data = [item for item in filtered_data if item['name'] == filter_value]
                elif filter_condition == 'notEqual':
                    filtered_data = [item for item in filtered_data if item['name'] != filter_value]
                elif filter_condition == 'startsWith':
                    filtered_data = [item for item in filtered_data if item['name'].startswith(filter_value)]
                elif filter_condition == 'endsWith':
                    filtered_data = [item for item in filtered_data if item['name'].endswith(filter_value)]
                elif filter_condition == 'isNull':
                    filtered_data = [item for item in filtered_data if item['name'] is None]
                elif filter_condition == 'isNotNull':
                    filtered_data = [item for item in filtered_data if item['name'] is not None]
          

        elif filter_type == 'date':
            pass

        elif filter_type == 'boolean':
            if column_name == 'isActive':
                if filter_condition == 'equals':
                    filtered_data = [item for item in filtered_data if item['isActive'] == (filter_value.lower() == 'true')]
                elif filter_condition == 'isNull':
                    filtered_data = [item for item in filtered_data if item['isActive'] is None]
                elif filter_condition == 'isNotNull':
                    filtered_data = [item for item in filtered_data if item['isActive'] is not None]
         

    return render_template('index.html', data=filtered_data)

if __name__ == '__main__':
    app.run(debug=True)


   
   






