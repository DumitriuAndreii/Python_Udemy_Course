# Dictionaries

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again",
#     "Loop":"The action of doing something over and over again"
# }
#
# print(programming_dictionary["Bug"])

# Ex1 - modifying values in dictionaries
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for student in student_scores:
#     if student_scores[student] >= 91 and student_scores[student] <=100:
#         student_grades[student] = "outstanding"
#     elif student_scores[student] >= 81 and student_scores[student] <=90:
#         student_grades[student] = "exceeds expectations"
#     elif student_scores[student] >= 71 and student_scores[student] <=80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)

# nesting list/dict in dict
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
#
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 12}
# }

# NESTING DICTS IN LISTS

# travel_log = [
#     {
#         "Country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total visits": 12
#     },
#     {
#         "Country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
#         "total_visits": 12
#     }
# ]

# Ex 2 - travel log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)