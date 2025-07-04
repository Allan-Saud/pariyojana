// // UserIndex.jsx
// import React, { useEffect, useState, navigate} from 'react';
// import axios from 'axios';
// import { FaEye, FaEllipsisV } from 'react-icons/fa';
// import { Menu, MenuItem } from '@mui/material';
// import UserFormModal from "../components/UserFormModal"

// const roles = [
//   'admin',
//   'planning section',
//   'ward/office seceratery',
//   'engineer',
//   'ward engineer',
//   'user committee',
//   'Data Entry',
//   'Department chief'
// ];

// const UsersPage = () => {
//   const [users, setUsers] = useState([]);
//   const [anchorEl, setAnchorEl] = useState(null);
//   const [selectedUser, setSelectedUser] = useState(null);
//   const [modalOpen, setModalOpen] = useState(false);
//   const [editMode, setEditMode] = useState(false);

// useEffect(() => {
//   console.log("Current token:", localStorage.getItem('accessToken')); // or your storage
//   fetchUsers();
// }, []);

//  const fetchUsers = async () => {
//   try {
//     // Match the key used in storage ('access_token')
//     const token = localStorage.getItem('access_token');
    
//     if (!token) {
//       console.error("No token found");
//       navigate('/login');
//       return;
//     }

//     const response = await axios.get('http://localhost:8000/api/users/', {
//       headers: {
//         'Authorization': `Bearer ${token}`
//       }
//     });
    
//     setUsers(response.data);
//   } catch (error) {
//     console.error("Error:", error.response?.data);
//     if (error.response?.status === 401) {
//       localStorage.removeItem('access_token'); // Clear invalid token
//       navigate('/');
//     }
//   }
// };

//   const handleMenuOpen = (event, user) => {
//     setAnchorEl(event.currentTarget);
//     setSelectedUser(user);
//   };

//   const handleMenuClose = () => {
//     setAnchorEl(null);
//     setSelectedUser(null);
//   };

//   const handleEdit = () => {
//     setEditMode(true);
//     setModalOpen(true);
//     handleMenuClose();
//   };

//   return (
//     <div className="p-4">
//       <div className="flex justify-between items-center mb-4">
//         <h1 className="text-xl font-bold">प्रयोगकर्ता सुची</h1>
//         <button
//           className="bg-blue-600 text-white px-4 py-2 rounded"
//           onClick={() => {
//             setEditMode(false);
//             setModalOpen(true);
//           }}
//         >
//           प्रयोगकर्ता थप्नुहोस्
//         </button>
//       </div>

//       <div className="overflow-x-auto bg-white shadow rounded">
//         <table className="w-full table-auto">
//           <thead className="bg-gray-100">
//             <tr>
//               <th className="p-2 border">क्र.स.</th>
//               <th className="p-2 border">प्रयोगकर्ताको नाम</th>
//               <th className="p-2 border">इमेल</th>
//               <th className="p-2 border">भूमिका</th>
//               <th className="p-2 border">फोन नम्बर</th>
//               <th className="p-2 border">वडा नंं.</th>
//               <th className="p-2 border">स्थिति</th>
//               <th className="p-2 border">अन्य</th>
//             </tr>
//           </thead>
//           <tbody>
//             {users.map((user, index) => (
//               <tr key={user.id} className="hover:bg-gray-50">
//                 <td className="p-2 border text-center">{index + 1}</td>
//                 <td className="p-2 border">{user.full_name}</td>
//                 <td className="p-2 border">{user.email}</td>
//                 <td className="p-2 border">{user.role}</td>
//                 <td className="p-2 border">{user.phone}</td>
//                 <td className="p-2 border">{user.ward_no}</td>
//                 <td className="p-2 border">{user.is_active ? 'Active' : 'Inactive'}</td>
//                 <td className="p-2 border text-center relative">
//                   <FaEye className="inline mr-2 text-blue-600 cursor-pointer" />
//                   <FaEllipsisV
//                     className="inline text-gray-700 cursor-pointer"
//                     onClick={(e) => handleMenuOpen(e, user)}
//                   />
//                 </td>
//               </tr>
//             ))}
//           </tbody>
//         </table>
//       </div>

//       <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={handleMenuClose}>
//         <MenuItem onClick={handleEdit}>Edit</MenuItem>
//         <MenuItem>Reset Password</MenuItem>
//         <MenuItem>Deactivate</MenuItem>
//         <MenuItem>Delete</MenuItem>
//       </Menu>

//       {modalOpen && (
//         <UserFormModal
//           open={modalOpen}
//           onClose={() => setModalOpen(false)}
//           editMode={editMode}
//           user={selectedUser}
//           onSuccess={fetchUsers}
//         />
//       )}
//     </div>
//   );
// };

// export default UsersPage;


import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { FaEye, FaEllipsisV, FaPlus, FaSearch } from 'react-icons/fa';
import { Menu, MenuItem } from '@mui/material';
import UserFormModal from "../components/UserFormModal";
import 'bootstrap/dist/css/bootstrap.min.css';

const UsersPage = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [editMode, setEditMode] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const token = localStorage.getItem('access_token');
      if (!token) {
        navigate('/login');
        return;
      }

      const response = await axios.get('http://localhost:8000/api/users/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      setUsers(response.data);
    } catch (error) {
      if (error.response?.status === 401) {
        localStorage.removeItem('access_token');
        navigate('/login');
      }
    }
  };

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
                  <th>क्रिया</th>
                </tr>
              </thead>
              <tbody>
                {filteredUsers.map((user, index) => (
                  <tr key={user.id}>
                    <td>{index + 1}</td>
                    <td>{user.full_name}</td>
                    <td>{user.email}</td>
                    <td>
                      <span className={`badge ${
                        user.role === 'admin' ? 'bg-purple' : 
                        user.role.includes('engineer') ? 'bg-blue' : 'bg-green'
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
                        <button className="btn btn-sm btn-outline-primary">
                          <FaEye />
                        </button>
                        <button 
                          className="btn btn-sm btn-outline-secondary"
                          onClick={(e) => {
                            setSelectedUser(user);
                            // Add your menu toggle logic here
                          }}
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
      {modalOpen && (
        <UserFormModal
          open={modalOpen}
          onClose={() => setModalOpen(false)}
          editMode={editMode}
          user={selectedUser}
          onSuccess={fetchUsers}
        />
      )}
    </div>
  );
};

export default UsersPage;
