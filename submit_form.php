<<<<<<< HEAD
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Your email address
    $recipient = "allesandroya@gmail.com";

    // Form field values
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Email subject
    $subject = "New Message from $name";

    // Email body
    $body = "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Message: $message";

    // Email headers
    $headers = "From: $name <$email>";

    // Send the email
    if (mail($recipient, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Message could not be sent.";
    }
}
?>
=======
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Your email address
    $recipient = "allesandroya@gmail.com";

    // Form field values
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Email subject
    $subject = "New Message from $name";

    // Email body
    $body = "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Message: $message";

    // Email headers
    $headers = "From: $name <$email>";

    // Send the email
    if (mail($recipient, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Message could not be sent.";
    }
}
?>
>>>>>>> d5dcbcf (Publish portfolio (initial without heavy GIFs))
