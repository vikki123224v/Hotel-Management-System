from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils import admin_required
from app.models import Room, Booking

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@admin_required
def dashboard():
    bookings = Booking.get_all()
    rooms = Room.get_all()
    return render_template('admin/dashboard.html', bookings=bookings, rooms=rooms)

@admin_bp.route('/rooms', methods=['GET', 'POST'])
@admin_required
def rooms():
    if request.method == 'POST':
        room_number = request.form.get('room_number')
        room_type = request.form.get('type')
        price = request.form.get('price')
        
        try:
            Room.create(room_number, room_type, price)
            flash('Room added successfully!', 'success')
        except Exception as e:
            flash(f'Error adding room: {str(e)}', 'danger')
            
        return redirect(url_for('admin.rooms'))
        
    all_rooms = Room.get_all()
    return render_template('admin/rooms.html', rooms=all_rooms)

@admin_bp.route('/rooms/<int:room_id>/status', methods=['POST'])
@admin_required
def update_room_status(room_id):
    status = request.form.get('status')
    Room.update_status(room_id, status)
    flash('Room status updated.', 'success')
    return redirect(url_for('admin.rooms'))

@admin_bp.route('/bookings/<int:booking_id>/status', methods=['POST'])
@admin_required
def update_booking_status(booking_id):
    status = request.form.get('status')
    Booking.update_status(booking_id, status)
    flash('Booking status updated.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/rooms/<int:room_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_room(room_id):
    room = Room.get_by_id(room_id)
    if not room:
        flash('Room not found.', 'danger')
        return redirect(url_for('admin.rooms'))

    if request.method == 'POST':
        room_number = request.form.get('room_number')
        room_type = request.form.get('type')
        price = request.form.get('price')
        try:
            Room.update(room_id, room_number, room_type, price)
            flash('Room updated successfully!', 'success')
        except Exception as e:
            flash(f'Error updating room: {str(e)}', 'danger')
        return redirect(url_for('admin.rooms'))

    return render_template('admin/edit_room.html', room=room)

@admin_bp.route('/rooms/<int:room_id>/delete', methods=['POST'])
@admin_required
def delete_room(room_id):
    try:
        Room.delete(room_id)
        flash('Room deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting room: {str(e)}', 'danger')
    return redirect(url_for('admin.rooms'))

@admin_bp.route('/bookings/<int:booking_id>/delete', methods=['POST'])
@admin_required
def delete_booking(booking_id):
    try:
        booking = Booking.get_by_id(booking_id)
        if booking:
            Room.update_status(booking['room_id'], 'available')
        Booking.delete(booking_id)
        flash('Booking deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting booking: {str(e)}', 'danger')
    return redirect(url_for('admin.dashboard'))
