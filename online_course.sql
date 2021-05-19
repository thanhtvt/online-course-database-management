DROP DATABASE IF EXISTS online_course;

CREATE DATABASE IF NOT EXISTS online_course;

USE online_course;

/* Table structure for table learner */
CREATE TABLE IF NOT EXISTS learner(
	learner_id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    learner_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) DEFAULT NULL,
    date_of_birth DATE DEFAULT NULL,
    employment_status VARCHAR(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
/* Data for the table learner */
INSERT INTO learner(learner_name, gender, date_of_birth, employment_status) VALUES
('Jonny Jack', 'Male', '2001/10/02', NULL),
('Ivy Handley', 'Female', '1992/08/10', 'Employed full time'),
('Jack Wilson', 'Male', '1998/07/12', 'Self-employed'),
('George Jarvis', 'Male', '1990/12/26', 'Employed full time'),
('Kylo Hebert', 'Female', '2000/04/10', 'Employed part time'),
('Rees Holland', NULL, '1999/03/21', NULL),
('Emily Hunt', 'Female', NULL, 'Unemployed'),
('Alex Ferguson', 'Male', '1973/12/31', 'Employed full time');

/* Table structure for table course */
CREATE TABLE IF NOT EXISTS course(
	course_id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    topic VARCHAR(50) NOT NULL,
    syllabus VARCHAR(5000) NOT NULL,
    price FLOAT(8) NOT NULL,
    course_description VARCHAR(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table learner */
INSERT INTO course(course_name, topic, syllabus, price, course_description) VALUES
('Machine Learning', 'Data Science', 'Week 1: Linear Regression with One Variable, Linear Algebra Review. Week 2: Linear Regression with Multiple Variables, Octave/Matlab Tutorial. Week 3: Logistic Regression, Regularization. Week 4: Neural Networks: Representation', 78.99, 'Skills you will gain: Logistic regression, artificial neural network, ML algorithms, machine learning'),
('Introduction to Marketing', 'Marketing', 'Week 1: BRANDING: Marketing Strategy and Brand Positioning. Week 2: CUSTOMER CENTRICITY: The Limits of Product-Centric Thinking & The Opportunities and Challenges of Customer Centricity. Week 3: GO TO MARKET STRATEGIES: Communications Strategy & Fundamentals of Pricing. Week 4: BRANDING: Effective Brand Communications Strategies and Repositioning Strategies', 56.99, 'Skills you will gain: Position, Marketing, Marketing Strategy, Customer Satisfaction'),
('Introduction to Psychology', 'Psychology', 'Week 1: Foundations. Week 2: Development and Language. Week 3: Cognition. Week 4: Self and others. Week 5: Variation. Week 6: The good life', 0.0, 'Skill you will gain: reasoning, problem solving, abstract thinking, analytical thinking, critical thinking'),
('Introduction to Research for Essay Writing', 'Music and Art', 'Week 1: Introduction to Research. Week 2: Doing Research and Planning the Paper. Week 3: Language for Research Writing. Week 4: More on Citing Sources and Formatting', 84.99, NULL);

/* Table structure for table university */
CREATE TABLE IF NOT EXISTS university(
	uni_id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    uni_name VARCHAR(50) NOT NULL,
    website MEDIUMTEXT,
    uni_description VARCHAR(3000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table university */
INSERT INTO university(uni_name, website, uni_description) VALUES
('Stanford', 'https://www.stanford.edu/', 'Stanford University is an American private research university located in Stanford'),
('University of Pennsylvania ', 'https://www.upenn.edu/', 'The University of Pennsylvania is a private university. A member of the Ivy League, Penn is the fourth-oldest institution of higher education in the United States, and considers itself to be the first university in the United States with both undergraduate and graduate studies'),
('Yale University', 'https://www.yale.edu/', ' Based in New Haven, Connecticut, Yale brings people and ideas together for positive impact around the globe. A research university that focuses on students and encourages learning as an essential way of life, Yale is a place for connection, creativity, and innovation among cultures and across disciplines'),
('University of California, Irvine', 'https://uci.edu/', 'UCI’s unyielding commitment to rigorous academics, cutting-edge research, and leadership and character development makes the campus a driving force for innovation and discovery that serves our local, national and global communities in many ways');

/* Table structure for table instructor */
CREATE TABLE IF NOT EXISTS instructor(
	instructor_id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    uni_id SMALLINT NOT NULL,
    instructor_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) DEFAULT NULL,
    date_of_birth DATE DEFAULT NULL,
    major VARCHAR(50) NOT NULL,
    CONSTRAINT fk_university_instructor FOREIGN KEY (uni_id) REFERENCES university (uni_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table instructor */
INSERT INTO instructor(uni_id, instructor_name, gender, date_of_birth, major) VALUES
(1, 'Andrew Ng', 'Male', '1976/04/18', 'Computer Science'),
(2, 'Barbara E. Kahn', 'Female', NULL, 'Marketing'),
(2, 'Peter Fader', 'Male', NULL, 'Marketing'),
(2, 'Jagmohan Raju', 'Male', NULL, 'Marketing'),
(3, 'Paul Bloom', 'Male', '1963/12/24', 'Psychology and Cognitive Science'),
(4, 'Tamy Chapman', 'Female', NULL, 'Language'),
(4, 'Helen Nam', 'Female', NULL, 'Philosophy');

/* Table structure for table certificate */
CREATE TABLE IF NOT EXISTS certificate(
	course_id SMALLINT PRIMARY KEY,
    cert_name VARCHAR(100) NOT NULL,
    CONSTRAINT fk_course_certificate FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table certificate */
INSERT INTO certificate(course_id, cert_name) VALUES
(1, 'Machine Learning: Certification of Completion'),
(2, 'Introduction to Marketing: Certification of Completion'),
(3, 'Introduction to Psychology: Certification of Completion'),
(4, 'Introduction to Research for Essay Writing: Certification of Completion');

/* Table structure for table section */
CREATE TABLE IF NOT EXISTS section(
	sec_number TINYINT NOT NULL,
    course_id SMALLINT NOT NULL, 
    sec_hour TINYINT NOT NULL,
    PRIMARY KEY (sec_number, course_id),
    CONSTRAINT fk_course_section FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table section */
INSERT INTO section(sec_number, course_id, sec_hour) VALUES
(1, 1, 4),
(2, 1, 8),
(3, 1, 7),
(4, 1, 5),
(1, 2, 2),
(2, 2, 2),
(3, 2, 3),
(4, 2, 2),
(1, 3, 4),
(2, 3, 3),
(3, 3, 2),
(4, 3, 3),
(5, 3, 2),
(6, 3, 1),
(1, 4, 5),
(2, 4, 5),
(3, 4, 4),
(4, 4, 5);

/* Table structure for table cert_achieve */
CREATE TABLE IF NOT EXISTS cert_achieve(
	learner_id SMALLINT NOT NULL,
    course_id SMALLINT NOT NULL,
    provide_date DATE NOT NULL,
    expire_date DATE NOT NULL,
    PRIMARY KEY (learner_id, course_id),
    CONSTRAINT fk_learner_cert_achieve FOREIGN KEY (learner_id) REFERENCES learner (learner_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_course_cert_achieve FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table cert_achieve */
INSERT INTO cert_achieve(learner_id, course_id, provide_date, expire_date) VALUES
(1, 1, '2021/04/21', '9999/12/31'),
(1, 3, '2020/11/18', '9999/12/31'),
(2, 4, '2020/12/09', '9999/12/31'),
(4, 2, '2019/09/04', '9999/12/31'),
(5, 2, '2021/01/30', '9999/12/31'),
(8, 1, '2018/05/28', '9999/12/31');

/* Table structure for table take_course */
CREATE TABLE IF NOT EXISTS take_course(
	learner_id SMALLINT NOT NULL,
    sec_number TINYINT NOT NULL,
    course_id SMALLINT NOT NULL,
    grade TINYINT DEFAULT NULL,
    PRIMARY KEY (learner_id, sec_number, course_id),
    CONSTRAINT fk_learner_take_course FOREIGN KEY (learner_id) REFERENCES learner (learner_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_section_take_course FOREIGN KEY (sec_number) REFERENCES section (sec_number) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_course_take_course FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table take_course */
INSERT INTO take_course(learner_id, sec_number, course_id, grade) VALUES
(1, 1, 1, 10),
(1, 2, 1, 10),
(1, 3, 1, 9),
(1, 4, 1, 10),
(1, 1, 3, 8),
(1, 2, 3, 8),
(1, 3, 3, 9),
(1, 4, 3, 10),
(1, 5, 3, 8),
(1, 6, 3, 9),
(2, 1, 4, 10),
(2, 2, 4, 10),
(2, 3, 4, 8),
(2, 4, 4, 9),
(3, 1, 2, 7),
(3, 2, 2, 10),
(3, 3, 2, 8),
(3, 4, 2, NULL),
(4, 1, 2, 9),
(4, 2, 2, 8),
(4, 3, 2, 8),
(4, 4, 2, 10),
(4, 1, 1, 7),
(4, 2, 1, 8),
(4, 3, 1, NULL),
(4, 4, 1, 9),
(5, 1, 2, 8),
(5, 2, 2, 9),
(5, 3, 2, 10),
(5, 4, 2, 6),
(6, 1, 3, 7),
(6, 2, 3, 10),
(6, 3, 3, 10),
(6, 4, 3, 7),
(6, 5, 3, 8),
(6, 6, 3, 7),
(7, 1, 4, 9),
(7, 2, 4, NULL),
(7, 3, 4, NULL),
(7, 4, 4, NULL),
(8, 1, 1, 9),
(8, 2, 1, 8),
(8, 3, 1, 9),
(8, 4, 1, 10);

/* Table structure for table hold_course */
CREATE TABLE IF NOT EXISTS hold_course(
	instructor_id SMALLINT NOT NULL PRIMARY KEY,
    uni_id SMALLINT NOT NULL,
    course_id SMALLINT NOT NULL,
    CONSTRAINT fk_university_hold_course FOREIGN KEY (uni_id) REFERENCES university (uni_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_instructor_hold_course FOREIGN KEY (instructor_id) REFERENCES instructor (instructor_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_course_hold_course FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/* Data for the table hold_course */
INSERT INTO hold_course(instructor_id, uni_id, course_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 2, 2),
(4, 2, 2),
(5, 3, 3),
(6, 4, 4),
(7, 4, 4);
