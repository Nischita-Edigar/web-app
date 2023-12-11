<?php
// Retrieve form data
$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];

// Create the email message
$message = "Name: $name\n";
$message .= "Email: $email\n";
$message .= "Phone: $phone\n";

// Set up the email parameters
$to = 'admissions@iqschool.in'; // Replace with your email address
$subject = 'Form Submission';
$headers = 'From: ' . $email . '\r\n' .
    'Reply-To: ' . $email . '\r\n' .
    'X-Mailer: PHP/' . phpversion();

// Send the email
$mail_sent = mail($to, $subject, $message, $headers);

// Check if the email was sent successfully
if ($mail_sent) {
    // Generate and download the PDF file
    $pdfContent = "Name: $name\nEmail: $email\nPhone: $phone";
    $pdfFilename = './images/Full Stack Java Brocher.pdf';
    header('Content-Type: application/pdf');
    header('Content-Disposition: attachment; filename="' . $pdfFilename . '"');
    echo $pdfContent;
} else {
    echo 'An error occurred while sending the form data.';
}
?>
