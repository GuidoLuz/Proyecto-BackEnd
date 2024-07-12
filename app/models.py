from app.database import get_db

class Paquete:
    #CONSTRUCTOR
    def __init__(self, id_paquete=None, ciudad=None, dias=None, precio=None, banner=None):
        self.id_paquete = id_paquete
        self.ciudad = ciudad
        self.dias = dias
        self.precio = precio
        self.banner = banner
        
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM paquetes")
        rows = cursor.fetchall()
        paquetes= []
        for row in rows:
            new_paquete = Paquete(row[0], ciudad=row[1], dias=row[2], precio=row[3], banner=row[4])
            paquetes.append(new_paquete)
        cursor.close()
        return paquetes
    

    @staticmethod
    def get_by_id(paquete_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM paquetes WHERE id_paquete = %s", (paquete_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Paquete(id_paquete=row[0], ciudad=row[1], dias=row[2], precio=row[3], banner=row[4])
        return None


    def save(self):
        # Logica para INSERT/UPDATE en base de datos
        db = get_db()
        cursor = db.cursor()
        if self.id_paquete:
            cursor.execute(""" UPDATE paquetes SET ciudad= %s,dias= %s,precio= %s,banner= %s 
            WHERE id_paquete = %s""", (self.ciudad,self.dias,self.precio,self.banner,self.id_paquete))
        else:
            cursor.execute("""INSERT INTO paquetes (ciudad,dias,precio,banner) VALUES(%s,%s,%s,%s)""",
                            (self.ciudad,self.dias,self.precio,self.banner))
            self.id_paquete = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM paquetes WHERE id_paquete = %s", (self.id_paquete,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_paquete': self.id_paquete,
            'ciudad': self.ciudad,
            'dias': self.dias,
            'precio': self.precio,
            'banner': self.banner
        }
    