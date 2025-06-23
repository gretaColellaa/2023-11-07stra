from database.DB_connect import DBConnect
from model.teams import Team


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodes(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select  t.ID , t.teamCode , t.name, sum(s.salary) as salaries 
                    from teams t
                    join salaries s on s.teamID = t.ID 
                    where t.`year` = %s
                    group by t.`year` , t.ID , t.teamCode , t.name
        """

        cursor.execute(query, (anno, ))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select
                    distinct
                    t.
                    `year` as y
                    from teams t
                    where
                    t.
                    `year` > 1979
                            """

        cursor.execute(query,)

        for row in cursor:
            result.append(row['y'])

        cursor.close()
        conn.close()
        return result
