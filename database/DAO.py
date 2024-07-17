from database.DB_connect import DBConnect
from model.genes import Gene


class DAO():
    @staticmethod
    def getGenesE():
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT GeneID, Chromosome 
                    FROM genes g
                    WHERE Essential = 'Essential' 
                    ORDER BY GeneID ASC
                    """
            cursor.execute(query)

            results = cursor.fetchall()
            cursor.close()
            cnx.close()
        return results



    @staticmethod
    def getInteractions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT 
            GeneID1, 
            GeneID2, 
            Expression_Corr
        FROM 
            interactions
        WHERE 
            GeneID1 != GeneID2 """
            cursor.execute(query)

            results = cursor.fetchall()
            cursor.close()
            cnx.close()
        return results






