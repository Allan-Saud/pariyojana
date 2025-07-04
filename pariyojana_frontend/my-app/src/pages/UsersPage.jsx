import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { FaEye, FaEllipsisV, FaPlus, FaSearch } from 'react-icons/fa';
import { Menu, MenuItem } from '@mui/material';
import UserFormModal from "../components/UserFormModal";
import 'bootstrap/dist/css/bootstrap.min.css';

const UsersPage = () => {
    const [users, setUsers] = useState([]);
    const [currentUser, setCurrentUser] = useState(null);
    const [selectedUser, setSelectedUser] = useState(null);
    const [modalOpen, setModalOpen] = useState(false);
    const [editMode, setEditMode] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [viewMode, setViewMode] = useState(false);
    const [anchorEl, setAnchorEl] = useState(null); // For menu positioning
    const [menuUser, setMenuUser] = useState(null); // User for menu actions

    const navigate = useNavigate();

    const fetchUsers = async () => {
        try {
            const token = localStorage.getItem('access_token');
            if (!token) {
                navigate('/login');
                return;
            }

            const response = await axios.get('/api/users/', {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            setUsers(response.data);
        } catch (error) {
            console.error('Error fetching users:', error);
            if (error.response?.status === 401) {
                localStorage.removeItem('access_token');
                navigate('/login');
            }
        }
    };

    // Handle menu open
    const handleMenuClick = (event, user) => {
        setAnchorEl(event.currentTarget);
        setMenuUser(user);
    };

    // Handle menu close
    const handleMenuClose = () => {
        setAnchorEl(null);
        setMenuUser(null);
    };

    // Toggle user active status
    const toggleUserStatus = async (userId, newStatus) => {
        try {
            const token = localStorage.getItem('access_token');
            await axios.patch(`/api/users/${userId}/`, 
                { is_active: newStatus },
                { headers: { 'Authorization': `Bearer ${token}` } }
            );
            fetchUsers(); // Refresh the list
        } catch (error) {
            console.error('Error updating user status:', error);
        }
    };

    // Delete user
    const deleteUser = async (userId) => {
        try {
            const token = localStorage.getItem('access_token');
            await axios.delete(`/api/users/${userId}/`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            fetchUsers(); // Refresh the list
        } catch (error) {
            console.error('Error deleting user:', error);
        }
    };

    // Reset password
    const resetPassword = async (userId) => {
        try {
            const token = localStorage.getItem('access_token');
            await axios.post(`/api/users/${userId}/reset-password/`, {}, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            alert('Password reset successfully!');
        } catch (error) {
            console.error('Error resetting password:', error);
            alert('Error resetting password');
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    const filteredUsers = users.filter(user =>
        user.full_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.email.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className="container-fluid py-4">
            <div className="card shadow">
                <div className="card-header bg-white py-3">
                    <div className="row align-items-center">
                        <div className="col-md-6">
                            <h5 className="mb-0">प्रयोगकर्ता सुची</h5>
                        </div>
                        <div className="col-md-6 d-flex justify-content-end">
                            <div className="input-group me-3" style={{ maxWidth: '300px' }}>
                                <span className="input-group-text">
                                    <FaSearch />
                                </span>
                                <input
                                    type="text"
                                    className="form-control"
                                    placeholder="खोज्नुहोस्..."
                                    value={searchTerm}
                                    onChange={(e) => setSearchTerm(e.target.value)}
                                />
                            </div>
                            <button
                                className="btn btn-primary"
                                onClick={() => {
                                    setEditMode(false);
                                    setViewMode(false);
                                    setSelectedUser(null);
                                    setModalOpen(true);
                                }}
                            >
                                <FaPlus className="me-2" />
                                प्रयोगकर्ता थप्नुहोस्
                            </button>
                        </div>
                    </div>
                </div>

                <div className="card-body">
                    <div className="table-responsive">
                        <table className="table table-hover">
                            <thead>
                                <tr>
                                    <th>क्र.स.</th>
                                    <th>नाम</th>
                                    <th>इमेल</th>
                                    <th>भूमिका</th>
                                    <th>फोन</th>
                                    <th>वडा नं.</th>
                                    <th>स्थिति</th>
                                    <th>अन्य</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredUsers.map((user, index) => (
                                    <tr key={user.id}>
                                        <td>{index + 1}</td>
                                        <td>{user.full_name}</td>
                                        <td>{user.email}</td>
                                        <td>
                                            <span className={`badge ${user.role === 'admin' ? 'bg-primary' :
                                                user.role.includes('engineer') ? 'bg-primary' : 'bg-danger'
                                                }`}>
                                                {user.role}
                                            </span>
                                        </td>
                                        <td>{user.phone}</td>
                                        <td>{user.ward_no}</td>
                                        <td>
                                            <span className={`badge ${user.is_active ? 'bg-success' : 'bg-danger'}`}>
                                                {user.is_active ? 'Active' : 'Inactive'}
                                            </span>
                                        </td>
                                        <td>
                                            <div className="d-flex gap-2">
                                                <button
                                                    className="btn btn-sm btn-outline-primary"
                                                    onClick={() => {
                                                        setEditMode(false);
                                                        setViewMode(true);
                                                        setSelectedUser(user);
                                                        setModalOpen(true);
                                                    }}
                                                >
                                                    <FaEye />
                                                </button>
                                                <button
                                                    className="btn btn-sm btn-outline-secondary"
                                                    onClick={(e) => handleMenuClick(e, user)}
                                                >
                                                    <FaEllipsisV />
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>

                        {filteredUsers.length === 0 && (
                            <div className="text-center py-5 text-muted">
                                <p>कुनै प्रयोगकर्ता फेला परेन</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* User Form Modal */}
            <UserFormModal
                open={modalOpen}
                onClose={() => setModalOpen(false)}
                editMode={editMode}
                viewOnly={!editMode && selectedUser !== null}
                user={selectedUser}
                onSuccess={fetchUsers}
            />

            {/* Action Menu */}
            <Menu
                anchorEl={anchorEl}
                open={Boolean(anchorEl)}
                onClose={handleMenuClose}
            >
                <MenuItem onClick={() => {
                    setSelectedUser(menuUser);
                    setEditMode(true);
                    setViewMode(false);
                    setModalOpen(true);
                    handleMenuClose();
                }}>
                    सम्पादन गर्नुहोस् (Edit)
                </MenuItem>
                
                <MenuItem onClick={() => {
                    if (window.confirm(`Reset password for ${menuUser.full_name}?`)) {
                        resetPassword(menuUser.id);
                    }
                    handleMenuClose();
                }}>
                    पासवर्ड रिसेट गर्नुहोस् (Reset Password)
                </MenuItem>
                
                <MenuItem onClick={() => {
                    if (window.confirm(`${menuUser.is_active ? 'Deactivate' : 'Activate'} ${menuUser.full_name}?`)) {
                        toggleUserStatus(menuUser.id, !menuUser.is_active);
                    }
                    handleMenuClose();
                }}>
                    {menuUser?.is_active ? 'निष्क्रिय गर्नुहोस् (Deactivate)' : 'सक्रिय गर्नुहोस् (Activate)'}
                </MenuItem>
                
                <MenuItem onClick={() => {
                    if (window.confirm(`Delete user ${menuUser.full_name}? This cannot be undone.`)) {
                        deleteUser(menuUser.id);
                    }
                    handleMenuClose();
                }}>
                    मेटाउनुहोस् (Delete)
                </MenuItem>
            </Menu>
        </div>
    );
};

export default UsersPage;

