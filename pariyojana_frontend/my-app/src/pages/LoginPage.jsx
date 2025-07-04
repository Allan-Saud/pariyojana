import React, { useState } from 'react';
import { loginUser } from '../services/authService';
import { useNavigate } from 'react-router-dom';
import logo from '../assets/logo.jpg';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await loginUser(email, password);
      localStorage.setItem('access_token', res.data.access);
      localStorage.setItem('refresh_token', res.data.refresh);
      
      navigate('/'); 
    } catch (err) {
      setError('Invalid email or password');
    }
  };

  return (
    <div className="login-container" style={styles.container}>
      <img src={logo} alt="Organization Logo" style={styles.logo} />
      <form onSubmit={handleLogin} style={styles.form}>
        <h2>Login</h2>
        {error && <p style={styles.error}>{error}</p>}
        <input
          type="email"
          placeholder="Email"
          value={email}
          required
          onChange={(e) => setEmail(e.target.value)}
          style={styles.input}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          required
          onChange={(e) => setPassword(e.target.value)}
          style={styles.input}
        />
        <button type="submit" style={styles.button}>Login</button>
        <p onClick={() => navigate('/forgot-password')} style={styles.link}>
          Forgot Password?
        </p>
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
  error: {
    color: 'red',
  },
};

export default LoginPage;


