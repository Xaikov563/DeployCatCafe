document.getElementById('contactForm').addEventListener('submit',function(event) {
    event.preventDefault(); 

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Send email using EmailJS
    emailjs.send("service_z5t0j9j", "template_f7o1vhh", {
        to_name: "Cafe",
        from_name: name,
        from_email: email,
        message: message
    })
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        alert('Email sent successfully!');
    }, function(error) {
        console.log('FAILED...', error);
        alert('Failed to send email. Please try again later.');
    });

    // Optionally, you can reset the form after submission
    document.getElementById('contactForm').reset();
});