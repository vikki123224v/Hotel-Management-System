from app import mysql

class User:
    @staticmethod
    def create(username, password_hash, role='customer'):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
            (username, password_hash, role)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_by_username(username):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        return user

    @staticmethod
    def get_by_id(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user


class Room:
    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM rooms ORDER BY room_number")
        rooms = cursor.fetchall()
        cursor.close()
        return rooms
        
    @staticmethod
    def get_by_id(room_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM rooms WHERE id = %s", (room_id,))
        room = cursor.fetchone()
        cursor.close()
        return room

    @staticmethod
    def create(room_number, type, price):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO rooms (room_number, type, price) VALUES (%s, %s, %s)",
            (room_number, type, price)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update(room_id, room_number, room_type, price):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE rooms SET room_number = %s, type = %s, price = %s WHERE id = %s",
            (room_number, room_type, price, room_id)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_status(room_id, status):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE rooms SET status = %s WHERE id = %s", (status, room_id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(room_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM rooms WHERE id = %s", (room_id,))
        mysql.connection.commit()
        cursor.close()


class Booking:
    @staticmethod
    def create(user_id, room_id, check_in, check_out):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO bookings (user_id, room_id, check_in, check_out) VALUES (%s, %s, %s, %s)",
            (user_id, room_id, check_in, check_out)
        )
        booking_id = cursor.lastrowid
        mysql.connection.commit()
        cursor.close()
        return booking_id

    @staticmethod
    def get_by_user(user_id):
        cursor = mysql.connection.cursor()
        query = '''
            SELECT b.*, r.room_number, r.type, r.price 
            FROM bookings b 
            JOIN rooms r ON b.room_id = r.id 
            WHERE b.user_id = %s
            ORDER BY b.check_in DESC
        '''
        cursor.execute(query, (user_id,))
        bookings = cursor.fetchall()
        cursor.close()
        return bookings

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        query = '''
            SELECT b.*, u.username, r.room_number 
            FROM bookings b 
            JOIN users u ON b.user_id = u.id
            JOIN rooms r ON b.room_id = r.id
            ORDER BY b.created_at DESC
        '''
        cursor.execute(query)
        bookings = cursor.fetchall()
        cursor.close()
        return bookings

    @staticmethod
    def update_status(booking_id, status):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE bookings SET status = %s WHERE id = %s", (status, booking_id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_by_id(booking_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM bookings WHERE id = %s", (booking_id,))
        booking = cursor.fetchone()
        cursor.close()
        return booking

    @staticmethod
    def delete(booking_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        mysql.connection.commit()
        cursor.close()
