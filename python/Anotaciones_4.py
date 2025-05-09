from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    if employee_id in employee_ids:
        return employee_id
    return None