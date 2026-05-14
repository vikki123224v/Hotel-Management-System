from flask import Blueprint, jsonify, request
from app.models import Room, Booking

api_bp = Blueprint('api', __name__)

# ============ ROOMS CRUD ============

@api_bp.route('/rooms', methods=['GET'])
def get_rooms():
    """REST API - Read all rooms"""
    rooms = list(Room.get_all())
    return jsonify({"status": "success", "data": rooms, "count": len(rooms)})

@api_bp.route('/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    """REST API - Read single room"""
    room = Room.get_by_id(room_id)
    if not room:
        return jsonify({"status": "error", "message": "Room not found"}), 404
    return jsonify({"status": "success", "data": room})

@api_bp.route('/rooms', methods=['POST'])
def create_room():
    """REST API - Create a room"""
    data = request.get_json()
    if not data or not all(k in data for k in ('room_number', 'type', 'price')):
        return jsonify({"status": "error", "message": "Missing required fields: room_number, type, price"}), 400
    try:
        Room.create(data['room_number'], data['type'], data['price'])
        return jsonify({"status": "success", "message": "Room created"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    """REST API - Update a room"""
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    room = Room.get_by_id(room_id)
    if not room:
        return jsonify({"status": "error", "message": "Room not found"}), 404
    try:
        Room.update(
            room_id,
            data.get('room_number', room['room_number']),
            data.get('type', room['type']),
            data.get('price', room['price'])
        )
        if 'status' in data:
            Room.update_status(room_id, data['status'])
        return jsonify({"status": "success", "message": "Room updated"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@api_bp.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    """REST API - Delete a room"""
    room = Room.get_by_id(room_id)
    if not room:
        return jsonify({"status": "error", "message": "Room not found"}), 404
    try:
        Room.delete(room_id)
        return jsonify({"status": "success", "message": "Room deleted"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ============ BOOKINGS CRUD ============

@api_bp.route('/bookings', methods=['GET'])
def get_bookings():
    """REST API - Read all bookings"""
    bookings = list(Booking.get_all())
    return jsonify({"status": "success", "data": bookings, "count": len(bookings)})

@api_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """REST API - Read single booking"""
    booking = Booking.get_by_id(booking_id)
    if not booking:
        return jsonify({"status": "error", "message": "Booking not found"}), 404
    return jsonify({"status": "success", "data": booking})

@api_bp.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """REST API - Delete a booking"""
    booking = Booking.get_by_id(booking_id)
    if not booking:
        return jsonify({"status": "error", "message": "Booking not found"}), 404
    try:
        Room.update_status(booking['room_id'], 'available')
        Booking.delete(booking_id)
        return jsonify({"status": "success", "message": "Booking deleted"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ============ HEALTH CHECK ============

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Cloud native health check endpoint"""
    return jsonify({
        "status": "up",
        "service": "CloudNest-HMS",
        "version": "1.0.0"
    })
