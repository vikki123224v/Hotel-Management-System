from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.utils import login_required
from app.models import Room, Booking
from app.services import notification_service
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.get_by_user(session['user_id'])
    return render_template('customer/dashboard.html', bookings=bookings)

@main_bp.route('/rooms')
@login_required
def rooms():
    all_rooms = list(Room.get_all())
    return render_template('customer/rooms.html', rooms=all_rooms)

@main_bp.route('/book/<int:room_id>', methods=['POST'])
@login_required
def book_room(room_id):
    check_in = request.form.get('check_in')
    check_out = request.form.get('check_out')
    
    if not check_in or not check_out:
        flash('Check-in and check-out dates are required.', 'danger')
        return redirect(url_for('main.rooms'))
        
    try:
        booking_id = Booking.create(session['user_id'], room_id, check_in, check_out)
        Room.update_status(room_id, 'booked')
        
        # Publish event for microservice conceptual demonstration
        event_data = {
            'booking_id': booking_id,
            'user': session['username'],
            'room_id': room_id,
            'check_in': check_in,
            'check_out': check_out
        }
        notification_service.publish("BOOKING_CREATED", event_data)
        
        flash('Room booked successfully! A confirmation notification has been triggered to the pub/sub queue.', 'success')
    except Exception as e:
        flash(f'Error booking room. It may be unavailable. ({str(e)})', 'danger')
        
    return redirect(url_for('main.dashboard'))
