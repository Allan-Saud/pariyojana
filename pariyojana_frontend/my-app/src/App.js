import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import ForgotPasswordPage from './pages/ForgotPasswordPage';
import Sidebar from './components/Sidebar';
import DashboardPage from './pages/DashBoradPage';
import ProjectsPage from './pages/ProjectsPage';
import AuthPage from './pages/AuthPage';
import InventoryPage from './pages/InventoryPage';
import PlanningPage from './pages/PlanningPage';
import ReportsPage from './pages/ReportsPage';
import SettingsPage from './pages/SettingsPage';
import UsersPage from './pages/UsersPage';
import Layout from './components/Layout';

function App() {
  return (
    // <Router>
    //   <Routes>
        
    //     <Route path="/login" element={<LoginPage />} />
    //     <Route path="/forgot-password" element={<ForgotPasswordPage />} />
    //     <Route path="/" element={<DashboardPage />} />
    //     <Route path="/projects" element={<ProjectsPage />} />
    //     <Route path="/auth" element={<AuthPage />} />
    //     <Route path="/inventory" element={<InventoryPage />} />
    //     <Route path="/planning" element={<PlanningPage />} />
    //     <Route path="/reports" element={<ReportsPage />} />
    //     <Route path="/settings" element={<SettingsPage />} />
    //     <Route path="/users" element={<UsersPage />} />
    //   </Routes>
    // </Router>

    <Router>
      <Routes>
        {/* Public routes */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/forgot-password" element={<ForgotPasswordPage />} />

        {/* Protected routes with sidebar layout */}
        <Route path="/" element={<Layout />}>
          <Route index element={<DashboardPage />} />
          <Route path="projects" element={<ProjectsPage />} />
          <Route path="auth" element={<AuthPage />} />
          <Route path="inventory" element={<InventoryPage />} />
          <Route path="planning" element={<PlanningPage />} />
          <Route path="reports" element={<ReportsPage />} />
          <Route path="settings" element={<SettingsPage />} />
          <Route path="users" element={<UsersPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
