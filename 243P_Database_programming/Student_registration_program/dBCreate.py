DB_NAME = 'courseRegisteration'
TABLES = {}
TABLES['students'] = (
                    "CREATE TABLE IF NOT EXISTS `students` ("
                     "  `student_id` int(6) NOT NULL AUTO_INCREMENT,"
                     "  `last_name` varchar(16) NOT NULL,"
                      " `first_name` varchar(14) NOT NULL,"
                      " `gender` enum('M','F') NOT NULL,"
                      " `birth_date` date NOT NULL,"
                      " `enrollment_date` date NOT NULL,"
                      " PRIMARY KEY (`student_id`)"
                      ") ENGINE=InnoDB")

TABLES['courses'] = (
                    "CREATE TABLE IF NOT EXISTS `courses`("
                    "   `course_id` int(4) NOT NULL AUTO_INCREMENT,"
                    "   `course_name` varchar(40) NOT NULL,"
                    "   `days` set('Mon','Tue','Wed','Thu','Fri') NOT NULL,"
                    "   `start_time` time NOT NULL,"
                    "   `end_time` time NOT NULL,"
                    "   `course_type` enum('L','P','D') NOT NULL,"
                    "   `department_name` varchar(10) NOT NULL,"
                    "   PRIMARY KEY (`course_id`)"
                    ")  ENGINE=InnoDB")
TABLES['course_registration'] = (
                    "CREATE TABLE IF NOT EXISTS `course_registration` ("
                    "   `reg_index int(4) NOT NULL AUTO_INCREMENT,"
                    "   `student_id` int(6) NOT NULL,"
                    "   `course_id` int(4) NOT NULL,"
                    "   PRIMARY KEY (`reg_index`)"
                    ") ENGINE=InnoDB")

#TABLES['employees'] = (
#    "CREATE TABLE `employees` ("
#    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `birth_date` date NOT NULL,"
#    "  `first_name` varchar(14) NOT NULL,"
#    "  `last_name` varchar(16) NOT NULL,"
#    "  `gender` enum('M','F') NOT NULL,"
#    "  `hire_date` date NOT NULL,"
#    "  PRIMARY KEY (`emp_no`)"
#    ") ENGINE=InnoDB")
