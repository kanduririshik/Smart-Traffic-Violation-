import mysql.connector

# DATABASE CONNECTION

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rishik@2842",
    database="traffic_violation_system"
)

cursor = db.cursor()

# FUNCTION 1 - SHOW DRIVERS

def show_drivers():

    query = "SELECT * FROM drivers"

    cursor.execute(query)

    result = cursor.fetchall()

    print("\n--- DRIVERS DATA ---\n")

    for row in result:
        print(row)

# FUNCTION 2 - SHOW VIOLATIONS

def show_violations():

    query = """
    SELECT v.violation_id,
           ve.vehicle_number,
           v.violation_type,
           v.fine_amount,
           v.location

    FROM violations v

    JOIN vehicles ve
    ON v.vehicle_id = ve.vehicle_id
    """

    cursor.execute(query)

    result = cursor.fetchall()

    print("\n--- VIOLATIONS DATA ---\n")

    for row in result:
        print(row)

# FUNCTION 3 - ADD VIOLATION

def add_violation():

    vehicle_id = int(input("Enter Vehicle ID: "))
    officer_id = int(input("Enter Officer ID: "))
    violation_type = input("Enter Violation Type: ")
    location = input("Enter Location: ")
    fine_amount = int(input("Enter Fine Amount: "))
    violation_date = input("Enter Date (YYYY-MM-DD): ")

    query = """
    INSERT INTO violations
    (vehicle_id, officer_id, violation_type, location, fine_amount, violation_date)

    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        vehicle_id,
        officer_id,
        violation_type,
        location,
        fine_amount,
        violation_date
    )

    cursor.execute(query, values)

    db.commit()

    print("\nViolation Added Successfully!\n")

# FUNCTION 4 - SEARCH VEHICLE

def search_vehicle():

    vehicle_number = input("Enter Vehicle Number: ")

    query = """
    SELECT d.driver_name,
           ve.vehicle_number,
           v.violation_type,
           v.fine_amount

    FROM violations v

    JOIN vehicles ve
    ON v.vehicle_id = ve.vehicle_id

    JOIN drivers d
    ON ve.owner_id = d.driver_id

    WHERE ve.vehicle_number = %s
    """

    cursor.execute(query, (vehicle_number,))

    result = cursor.fetchall()

    print("\n--- SEARCH RESULTS ---\n")

    for row in result:
        print(row)


# FUNCTION 5 - ANALYTICS

def analytics():

    print("\n====== ANALYTICS MENU ======\n")

    print("1. Total Fine Collection")
    print("2. Highest Fine")
    print("3. City-wise Violations")
    print("4. Repeat Offenders")

    choice = input("\nEnter Choice: ")

    # TOTAL FINE

    if choice == '1':

        query = """
        SELECT SUM(fine_amount)
        FROM violations
        """

        cursor.execute(query)

        result = cursor.fetchone()

        print("\nTotal Fine Collected:", result[0])

    # HIGHEST FINE

    elif choice == '2':

        query = """
        SELECT MAX(fine_amount)
        FROM violations
        """

        cursor.execute(query)

        result = cursor.fetchone()

        print("\nHighest Fine:", result[0])

    # CITY-WISE VIOLATIONS

    elif choice == '3':

        query = """
        SELECT location, COUNT(*)

        FROM violations

        GROUP BY location
        """

        cursor.execute(query)

        result = cursor.fetchall()

        print("\n--- CITY-WISE VIOLATIONS ---\n")

        for row in result:
            print(row)

    # REPEAT OFFENDERS

    elif choice == '4':

        query = """
        SELECT ve.vehicle_number,
               COUNT(*) AS total_cases

        FROM violations v

        JOIN vehicles ve
        ON v.vehicle_id = ve.vehicle_id

        GROUP BY ve.vehicle_number

        HAVING COUNT(*) > 1
        """

        cursor.execute(query)

        result = cursor.fetchall()

        print("\n--- REPEAT OFFENDERS ---\n")

        for row in result:
            print(row)

    else:
        print("\nInvalid Choice!")
def show_payments():

    query = """
    SELECT *
    FROM payments
    """

    cursor.execute(query)

    result = cursor.fetchall()

    print("\n--- PAYMENTS DATA ---\n")

    for row in result:
        print(row)  
def show_cameras():

    query = """
    SELECT *
    FROM cctv_cameras
    """

    cursor.execute(query)

    result = cursor.fetchall()

    print("\n--- CCTV CAMERAS ---\n")

    for row in result:
        print(row)
def show_accidents():

    query = """
    SELECT *
    FROM accident_reports
    """

    cursor.execute(query)

    result = cursor.fetchall()

    print("\n--- ACCIDENT REPORTS ---\n")

    for row in result:
        print(row)
# MAIN MENU

while True:

    print("\n====== SMART TRAFFIC SYSTEM ======\n")

    print("1. Show Drivers")
    print("2. Show Violations")
    print("3. Add Violation")
    print("4. Search Vehicle")
    print("5. Analytics")
    print("6. Show Payments")
    print("7. Show CCTV Cameras")
    print("8. Show Accident Reports")
    print("9. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == '1':
        show_drivers()

    elif choice == '2':
        show_violations()

    elif choice == '3':
        add_violation()

    elif choice == '4':
        search_vehicle()

    elif choice == '5':
        qanalytics()

    elif choice == '6':
        show_payments()

    elif choice == '7':
        show_cameras()

    elif choice == '8':
        show_accidents()

    elif choice == '9':
        print("\nExiting System...")
    break