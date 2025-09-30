from school_schedule.student import Student


def test_student_class_iniitialization():
    # Arrange
    name = "Bob"
    grade = "Junior"
    classes = ["History", "CS"]


    # Act

    bob = Student(name, grade, classes)

    # Assert
    
    assert bob.name == name
    assert bob.grade == grade
    assert bob.classes == classes


def test_add_class_allows_non_string_values():

    alice = Student("Alice", "Senior", ["History", "CS"])

    result = alice.add_class(123)

    assert result == ["History", "CS", 123]



def test_get_student_num_classes():
    # Arrange
    name = "Kate"
    grade = "Junior"
    classes = ["History", "CS"]

    kate = Student(name, grade, classes)

    # Act

    result = kate.get_num_classes()

    # Assert
    # Assert result is 2
    
    assert result == 2






