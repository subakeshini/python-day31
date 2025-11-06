# 1. Available courses
available_courses = {"Python", "Data Science", "Web Development", "AI & ML", "Cybersecurity"}

# 2. Student's enrolled courses
student_courses = set()

# 3. Enroll in a course
def enroll_course(course_name):
    if course_name in available_courses:
        student_courses.add(course_name)
        print(f"✅ Enrolled in '{course_name}'")
    else:
        print(f"❌ Course '{course_name}' not found!")

# 4. Remove a course
def remove_course(course_name):
    if course_name in student_courses:
        student_courses.remove(course_name)
        print(f"🗑️ Removed '{course_name}' from enrollment")
    else:
        print(f"⚠️ You are not enrolled in '{course_name}'")

# 5. Display final enrolled courses
def display_enrolled_courses():
    if student_courses:
        print("\n📘 Final Enrolled Courses:")
        for course in student_courses:
            print(f"- {course}")
    else:
        print("\n📭 No courses enrolled.")

# Sample Execution
enroll_course("Python")
enroll_course("AI & ML")
enroll_course("Blockchain")  # Invalid
remove_course("Python")
enroll_course("Cybersecurity")
display_enrolled_courses()
