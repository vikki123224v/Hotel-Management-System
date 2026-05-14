document.addEventListener('DOMContentLoaded', () => {
    // Basic date validation for forms
    const forms = document.querySelectorAll('.check-form');
    
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const checkInInput = form.querySelector('input[name="check_in"]');
            const checkOutInput = form.querySelector('input[name="check_out"]');
            
            if(!checkInInput || !checkOutInput) return;

            const checkIn = new Date(checkInInput.value);
            const checkOut = new Date(checkOutInput.value);
            const today = new Date();
            today.setHours(0,0,0,0);
            
            if (checkIn < today) {
                e.preventDefault();
                alert('Check-in date cannot be in the past.');
            }
            
            if (checkOut <= checkIn) {
                e.preventDefault();
                alert('Check-out date must be after check-in date.');
            }
        });
    });

    // Automatically dismiss flash alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    if (alerts.length > 0) {
        setTimeout(() => {
            alerts.forEach(alert => {
                alert.style.transition = "opacity 0.5s ease";
                alert.style.opacity = "0";
                setTimeout(() => alert.remove(), 500);
            });
        }, 5000);
    }
});
