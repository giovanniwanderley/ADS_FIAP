document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.getElementById('password');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
});

document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Login submitted!');
});

document.getElementById('register').addEventListener('click', function () {
    alert('Redirect to registration page.');
});

document.getElementById('forgotPassword').addEventListener('click', function () {
    alert('Redirect to password reset page.');
});

document.getElementById('googleLogin').addEventListener('click', function () {
    alert('Google login clicked.');
});

document.getElementById('facebookLogin').addEventListener('click', function () {
    alert('Facebook login clicked.');
});
    