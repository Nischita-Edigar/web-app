<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $phone = $_POST["phone"];
    $email = $_POST["email"];

    $to = "nischitav702@gmail.com"; // Replace with your email address
    $subject = "New Enquiry";
    $message = "Name: $name\nPhone: $phone\nEmail: $email";

    // Send email
    if (mail($to, $subject, $message)) {
        // If email is sent successfully, show the thank you message
        echo json_encode(["success" => true]);
    } else {
        // If there's an error sending email, provide an error response
        echo json_encode(["success" => false, "message" => "Error sending email"]);
    }
} else {
    // If the request is not a POST request, provide an error response
    echo json_encode(["success" => false, "message" => "Invalid request"]);
}
?>
