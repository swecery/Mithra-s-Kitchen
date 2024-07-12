document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('reservationForm');
  
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      const date = document.getElementById('date').value;
      const time = document.getElementById('time').value;
      const guests = document.getElementById('guests').value;
  
      const data = {
        date: date,
        time: time,
        guests: guests
      };
  
      try {
        const response = await fetch('https://example.com/api/reserve/', { // Örnek bir API endpoint
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });
  
        if (response.ok) {
          const result = await response.json();
          alert('Reservation successful');
          // Redirect or update the UI as needed
        } else {
          const errorData = await response.json();
          console.error('Error response from server:', errorData);
          alert(`Reservation failed: ${errorData.message}`);
        }
      } catch (error) {
        console.error('Network or other error:', error);
        alert('An error occurred. Please try again later.');
      }
    });
  });
  