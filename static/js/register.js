document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');
  
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      const username = document.getElementById('username').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirmPassword').value;
  
      // Client-side validation
      if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
      }

      const data = {
        username: username,
        email: email,
        password: password
      };
  
      try {
        const response = await fetch('/api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        });
        if (response.ok) {
          const result = await response.json();
          alert('Registration successful');
          // Redirect or update the UI as needed
        } else {
          const errorData = await response.json();
          alert(`Registration failed: ${errorData.message}`);
        }
      } catch (error) {
        //console.error('Error:', error);
        alert('An error occurred. Please try again later.');
      }
    });
  });
  