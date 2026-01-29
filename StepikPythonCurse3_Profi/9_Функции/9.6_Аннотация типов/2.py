def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    students_name = grades['name']
    max_scores = max(grades['grades'])
    d = {'name': students_name, 'top_grade': max_scores}
    return d
