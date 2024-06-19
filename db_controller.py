from db_config import mydb

def get_license_info(plate):

    mycursor = mydb.cursor()

    sql = "SELECT name FROM license_info WHERE plate = %s"

    mycursor.execute(sql, (plate, ))

    myresult = ""

    try:
        myresult = mycursor.fetchone()[0]
    except:
        myresult = "Not found"

    return myresult
#txt = get_license_info("38-P1056.94")
#print(txt)