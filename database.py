import sqlite3

# Define named constants
DATABASE_NAME = "HospitalDB.db"
PATIENT_TABLE_NAME = "PATIENT"
CONTACT_NO_TABLE_NAME = "CONTACT_NO"
EMPLOYEE_TABLE_NAME = "employee"
TREATMENT_TABLE_NAME = "TREATMENT"
MEDICINE_TABLE_NAME = "MEDICINE"
ROOM_TABLE_NAME = "ROOM"
APPOINTMENT_TABLE_NAME = "appointment"
MAX_NAME_LENGTH = 20
MAX_EMAIL_LENGTH = 50
MAX_ADDRESS_LENGTH = 100
MAX_DESIGNATION_LENGTH = 20
MAX_EXPERIENCE_LENGTH = 100
MAX_TREATMENT_LENGTH = 100
MAX_MEDICINE_LENGTH = 100
MAX_ROOM_TYPE_LENGTH = 10
MAX_DESCRIPTION_LENGTH = 100

# Establish a connection to the database
conn = sqlite3.connect(DATABASE_NAME)
print("DATABASE CONNECTION SUCCESSFUL")

# Drop existing tables if they exist
conn.execute(f"Drop table if EXISTS {PATIENT_TABLE_NAME}")
conn.execute(f"""Create table {PATIENT_TABLE_NAME}
           (PATIENT_ID int primary key,
            NAME VARCHAR({MAX_NAME_LENGTH}) not null,
            SEX varchar(10) not null,
            BLOOD_GROUP varchar(5) not null,
            DOB date not null,
            ADDRESS varchar({MAX_ADDRESS_LENGTH}) not null,
            CONSULT_TEAM varchar(50) not null,
            EMAIL varchar({MAX_EMAIL_LENGTH}) not null
            )""")
print(f"{PATIENT_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Create CONTACT_NO table
conn.execute(f"Drop table if EXISTS {CONTACT_NO_TABLE_NAME}")
conn.execute(f"""CREATE TABLE {CONTACT_NO_TABLE_NAME}
           (PATIENT_ID int PRIMARY KEY,
            CONTACTNO int not null,
            ALT_CONTACT int,
            FOREIGN KEY(PATIENT_ID) REFERENCES {PATIENT_TABLE_NAME}(PATIENT_ID))
           """)
print(f"{CONTACT_NO_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Create employee table
conn.execute(f"Drop table if EXISTS {EMPLOYEE_TABLE_NAME}")
conn.execute(f"""create table {EMPLOYEE_TABLE_NAME}
           (EMP_ID varchar(10) primary key,
           EMP_NAME varchar({MAX_NAME_LENGTH})not null,
            SEX varchar(10) not null,
            AGE int not null,
            DESIG varchar({MAX_DESIGNATION_LENGTH}) not null,
            SAL int not null,
            EXP varchar({MAX_EXPERIENCE_LENGTH}) not null,
            EMAIL varchar({MAX_EMAIL_LENGTH}) not null,
           PHONE int)""")
print(f"{EMPLOYEE_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Create TREATMENT table
conn.execute(f"Drop table if EXISTS {TREATMENT_TABLE_NAME}")
conn.execute(f"""CREATE TABLE {TREATMENT_TABLE_NAME}
           (PATIENT_ID int primary key,
            TREATMENT varchar({MAX_TREATMENT_LENGTH}) not null,
            TREATMENT_CODE varchar(30) not null,
            T_COST int not null,
           FOREIGN KEY(PATIENT_ID) REFERENCES {PATIENT_TABLE_NAME}(PATIENT_ID));
            """)
print(f"{TREATMENT_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Create MEDICINE table
conn.execute(f"Drop table if EXISTS {MEDICINE_TABLE_NAME}")
conn.execute(f"""CREATE TABLE {MEDICINE_TABLE_NAME}
           (PATIENT_ID int primary key,
            MEDICINE_NAME varchar({MAX_MEDICINE_LENGTH}) not null,
            M_COST int not null,
            M_QTY int not null,
            FOREIGN KEY(PATIENT_ID) REFERENCES {PATIENT_TABLE_NAME}(PATIENT_ID));
            """)
print(f"{MEDICINE_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Create ROOM table
conn.execute(f"Drop table if EXISTS {ROOM_TABLE_NAME}")
conn.execute(f"""Create table {ROOM_TABLE_NAME}
         (PATIENT_ID int not NULL ,
           ROOM_NO varchar(20) PRIMARY KEY ,
          ROOM_TYPE varchar({MAX_ROOM_TYPE_LENGTH}) not null,
           RATE int not null,
           DATE_ADMITTED date,
            DATE_DISCHARGED date NULL,
           FOREIGN KEY(PATIENT_ID) REFERENCES {PATIENT_TABLE_NAME}(PATIENT_ID)
            );
           """)
print(f"{ROOM_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Create APPOINTMENT table
conn.execute(f"Drop table if EXISTS {APPOINTMENT_TABLE_NAME}")
conn.execute(f"""create table {APPOINTMENT_TABLE_NAME}
            (
             PATIENT_ID int not null,
             EMP_ID varchar(10) not null,
             AP_NO varchar(10) primary key,
             AP_TIME time,
             AP_DATE date,
             description varchar({MAX_DESCRIPTION_LENGTH}),
             FOREIGN KEY(PATIENT_ID) references {PATIENT_TABLE_NAME}(PATIENT_ID),
             FOREIGN KEY(EMP_ID) references {EMPLOYEE_TABLE_NAME}(EMP_ID));""")
print(f"{APPOINTMENT_TABLE_NAME} TABLE CREATED SUCCESSFULLY")

# Commit changes and close the connection
conn.commit()
conn.close()