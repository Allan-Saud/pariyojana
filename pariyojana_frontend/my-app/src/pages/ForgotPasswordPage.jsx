import React, { useState } from 'react';
import { forgotPassword } from '../services/authService';
import { useNavigate } from 'react-router-dom';
import logo from '../assets/logo.jpg';

const ForgotPasswordPage = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await forgotPassword(email);
      setMessage('A new password has been sent to your email.');
    } catch (err) {
      setMessage('User with this email does not exist.');
    }
  };

  return (
    <div style={styles.container}>
      <img src={logo} alt="Organization Logo" style={styles.logo} />
      <form onSubmit={handleSubmit} style={styles.form}>
        <h2>Forgot Password</h2>
        {message && <p style={styles.message}>{message}</p>}
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          required
          onChange={(e) => setEmail(e.target.value)}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>Send Reset Link</button>
        <p onClick={() => navigate('/login')} style={styles.link}>Back to Login</p>
      </form>
    </div>
  );
};

const styles = {
  container: {
    maxWidth: 400,
    margin: 'auto',
    padding: 20,
    textAlign: 'center',
  },
  logo: {
    width: 100,
    marginBottom: 20,
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: 10,
  },
  input: {
    padding: 10,
    fontSize: 16,
  },
  button: {
    padding: 10,
    fontSize: 16,
    background: '#1976d2',
    color: '#fff',
    border: 'none',
  },
  link: {
    marginTop: 10,
    color: '#1976d2',
    cursor: 'pointer',
  },
  message: {
    color: 'green',
  },
};

export default ForgotPasswordPage;
