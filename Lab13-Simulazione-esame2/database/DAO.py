from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(s.`datetime`) as y
                from new_ufo_sightings.sighting s """

        cursor.execute(query)

        for row in cursor:
            result.append(row["y"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getForme():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct s.shape as forma
                    from new_ufo_sightings.sighting s """

        cursor.execute(query)

        for row in cursor:
            result.append(row["forma"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getState():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
                   from new_ufo_sightings.state s  """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArco(stato1,stato2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select state1, state2
                    from new_ufo_sightings.neighbor n , new_ufo_sightings.state s1 , new_ufo_sightings.state s2 
                    where s1.id = %s and s1.id = n.state1 and s2.id = %s and s2.id = n.state2 """

        cursor.execute(query,(stato1,stato2))

        for row in cursor:
            result.append((row["state1"], row["state2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(shape,year, stato1, stato2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as peso
                    from new_ufo_sightings.sighting s
                    where s.shape = %s and year(s.`datetime`)= %s and (s.state =%s or s.state = %s) """

        cursor.execute(query, (shape,year, stato1, stato2,))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result
