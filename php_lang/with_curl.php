<?php
$data = [
    'username' => 'testuser',
    'email' => 'testuser@test.com',
    'password' => 'testpassword'
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://3.145.97.83:3333/user/create');
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if ($http_code == 200) {
    $json_response = json_decode($response, true);
    if ($json_response['success'] && isset($json_response['data']['user_id'], $json_response['data']['username'], $json_response['data']['email'])) {
        echo "Test case passed: new user registered successfully.\n";
    } else {
        echo "Test case failed: invalid response.\n";
    }
} else {
    echo "Test case failed: HTTP request failed with status code $http_code.\n";
}

curl_close($ch);
?>