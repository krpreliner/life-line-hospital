const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({ extended: true }));


// API Route: Contact Form Submission
app.post('/api/contact', (req, res) => {
    const { name, phone, email, message } = req.body;
    
    // In a real application, you would save this to a database or send an email.
    console.log('\n--- New Contact Message Received ---');
    console.log(`Name: ${name}`);
    console.log(`Phone: ${phone}`);
    console.log(`Email: ${email}`);
    console.log(`Message: ${message}`);
    console.log('------------------------------------\n');

    res.status(200).json({ success: true, message: 'Message sent successfully! We will get back to you soon.' });
});

// API Route: Appointment Booking
app.post('/api/appointment', (req, res) => {
    const { patientName, phone, department, date } = req.body;
    
    // In a real application, you would save this to a database.
    console.log('\n--- New Appointment Booking ---');
    console.log(`Patient Name: ${patientName}`);
    console.log(`Phone: ${phone}`);
    console.log(`Department: ${department}`);
    console.log(`Date: ${date}`);
    console.log('-------------------------------\n');

    res.status(200).json({ success: true, message: 'Appointment booked successfully!' });
});

// Fallback route removed for Express 5 compatibility

// Start the server only if running locally
if (require.main === module) {
    app.listen(PORT, () => {
        console.log(`\n========================================================`);
        console.log(`🚀 Server is running on http://localhost:${PORT}`);
        console.log(`========================================================\n`);
    });
}

// Export the app for Vercel
module.exports = app;
