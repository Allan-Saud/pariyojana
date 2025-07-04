import React, { useState } from 'react';
import { loginUser } from '../services/authService';
import { useNavigate } from 'react-router-dom';
import logo from '../assets/logo.jpg'; // your full photo here

const LoginPage = () => {
  const [email, setEmail] = useState(localStorage.getItem('saved_email') || '');
  const [password, setPassword] = useState(localStorage.getItem('saved_password') || '');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [rememberMe, setRememberMe] = useState(false);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await loginUser(email, password);
      localStorage.setItem('access_token', res.data.access);
      localStorage.setItem('refresh_token', res.data.refresh);

      if (rememberMe) {
        localStorage.setItem('saved_email', email);
        localStorage.setItem('saved_password', password);
      } else {
        localStorage.removeItem('saved_email');
        localStorage.removeItem('saved_password');
      }

      navigate('/');
    } catch (err) {
      setError('Invalid email or password');
    }
  };

  return (
    <div style={styles.container}>
      {/* Left side with image */}
      <div style={styles.imageContainer}>
        <img src={logo} alt="Organization Visual" style={styles.image} />
      </div>

      {/* Right side with login form */}
      <div style={styles.formContainer}>
        <form onSubmit={handleLogin} style={styles.form}>
          <h2 style={styles.title}>Login</h2>
          {error && <p style={styles.error}>{error}</p>}
          <input
            type="email"
            placeholder="Email"
            value={email}
            required
            onChange={(e) => setEmail(e.target.value)}
            style={styles.input}
          />
          <div style={styles.passwordContainer}>
            <input
              type={showPassword ? 'text' : 'password'}
              placeholder="Password"
              value={password}
              required
              onChange={(e) => setPassword(e.target.value)}
              style={styles.input}
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              style={styles.togglePassword}
            >
              {showPassword ? 'Hide' : 'Show'}
            </button>
          </div>
          <div style={styles.rememberRow}>
            <label style={styles.rememberLabel}>
              <input
                type="checkbox"
                checked={rememberMe}
                onChange={() => setRememberMe(!rememberMe)}
              />
              Remember Me
            </label>
            <span onClick={() => navigate('/forgot-password')} style={styles.link}>
              Forgot Password?
            </span>
          </div>
          <button type="submit" style={styles.button}>Login</button>
        </form>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    height: '100vh',
    width: '100vw',
    overflow: 'hidden',
    fontFamily: 'sans-serif',
  },
//   imageContainer: {
//     flex: 6,
//     backgroundColor: '#e3f2fd',
//   },
//   image: {
//     width: '100%',
//     height: '100%',
//     objectFit: 'cover',
//   },
imageContainer: {
  flex: 6,
  position: 'relative',
  height: '100%',
  width: '100%',
  overflow: 'hidden',
},
image: {
  position: 'absolute',
  top: 0,
  left: 0,
  height: '100%',
  width: '100%',
  objectFit: 'cover',
},

  formContainer: {
    flex: 4,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: '#fff',
    boxShadow: 'inset 2px 0 8px rgba(0,0,0,0.05)',
  },
  form: {
    width: '80%',
    maxWidth: 400,
    display: 'flex',
    flexDirection: 'column',
    gap: 15,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#1976d2',
    textAlign: 'center',
  },
  input: {
    padding: '12px 14px',
    fontSize: 16,
    borderRadius: 6,
    border: '1px solid #ccc',
    outlineColor: '#1976d2',
    width: '100%',
  },
  passwordContainer: {
    position: 'relative',
  },
  togglePassword: {
    position: 'absolute',
    right: 10,
    top: '50%',
    transform: 'translateY(-50%)',
    background: 'transparent',
    border: 'none',
    color: '#1976d2',
    fontWeight: 'bold',
    cursor: 'pointer',
  },
  rememberRow: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    fontSize: 14,
  },
  rememberLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: 5,
  },
  button: {
    padding: 12,
    fontSize: 16,
    background: '#1976d2',
    color: '#fff',
    border: 'none',
    borderRadius: 6,
    cursor: 'pointer',
    transition: 'background 0.3s',
  },
  link: {
    color: '#1976d2',
    cursor: 'pointer',
    textDecoration: 'underline',
  },
  error: {
    color: 'red',
    fontSize: 14,
    textAlign: 'center',
  },
};

export default LoginPage;
