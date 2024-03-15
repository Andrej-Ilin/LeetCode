"""
"""
import pandas as pd

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype(
    {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'})


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    # emp = employee.loc[employee["managerId"].isin(employee["id"].tolist())]
    emp = employee.merge(employee, how='inner',  left_on='managerId', right_on='id')
    emp_earn = emp[emp.salary_x > emp.salary_y].name_x

    return pd.DataFrame({"Employee": emp_earn})  # employee["id"] == employee["managerId"],


print(find_employees(employee))
