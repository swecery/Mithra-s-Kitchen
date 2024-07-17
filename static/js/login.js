document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
  
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
  
      const data = {
        email: email,
        password: password
      };
  
      try {
        const response = await fetch('/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });
  
        if (response.ok) {
          const result = await response.json();
          alert('Login successful');
          // Redirect or update the UI as needed
          window.location.href = '/dashboard'; 
        } else {
          const errorData = await response.json();
          alert(`Login failed: ${errorData.message}`);
        }
      } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
      }
    });
  });
  