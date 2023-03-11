<?php

// do not forget about: 'composer require guzzlehttp/guzzle'

use GuzzleHttp\Client;

// Test case 1: Verify that a new user can be successfully registered with valid inputs
function test_register_new_user($client) {
    $response = $client->post('http://3.145.97.83:3333/user/create', [
        'form_params' => [
            'username' => 'testuser',
            'email' => 'testuser@example.com',
            'password' => 'testpassword'
        ]
    ]);
    $response_data = json_decode($response->getBody(), true);
    if ($response->getStatusCode() == 200 && $response_data['message'] == 'User registered successfully') {
        echo "Test case 1: Passed\n";
    } else {
        echo "Test case 1: Failed\n";
    }
}

// Test case 2: Verify that the API returns an appropriate error message and status code when a user tries to register with an already existing email or username
function test_register_existing_user($client) {
    $response = $client->post('http://3.145.97.83:3333/user/create', [
        'form_params' => [
            'username' => 'testuser',
            'email' => 'testuser@example.com',
            'password' => 'testpassword'
        ]
    ]);
    $response_data = json_decode($response->getBody(), true);
    if ($response->getStatusCode() == 400 && $response_data['message'] == 'Username or email already exists') {
        echo "Test case 2: Passed\n";
    } else {
        echo "Test case 2: Failed\n";
    }
}

// Test case 3: Verify that a GET request to retrieve all registered users returns the correct data
function test_get_all_users($client) {
    $response = $client->get('http://3.145.97.83:3333/user/get');
    $response_data = json_decode($response->getBody(), true);
    if ($response->getStatusCode() == 200 && count($response_data) > 0 && isset($response_data[0]['username']) && isset($response_data[0]['email'])) {
        echo "Test case 3: Passed\n";
    } else {
        echo "Test case 3: Failed\n";
    }
}

// Create a Guzzle HTTP client
$client = new Client();

// Call the test functions
test_register_new_user($client);
test_register_existing_user($client);
test_get_all_users($client);

?>