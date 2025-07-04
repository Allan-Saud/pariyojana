import axios from 'axios';

const BASE_URL='http://localhost:8000/api/auth'

export const loginUser = async (email, password) => {
  return axios.post(`${BASE_URL}/login/`, { email, password });
};

export const forgotPassword = async (email) => {
  return axios.post(`${BASE_URL}/forgot-password/`, { email });
};

