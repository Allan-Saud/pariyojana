// // src/components/UserFormModal.jsx
// import React, { useState, useEffect } from 'react';

// const roles = [
//     'admin',
//     'planning section',
//     'ward/office seceratery',
//     'engineer',
//     'ward engineer',
//     'user committee',
//     'Data Entry',
//     'Department chief',
// ];

// const UserFormModal = ({ open, onClose, editMode, user, onSuccess, viewOnly = false  }) => {
//     const [formData, setFormData] = useState({
//         full_name: '',
//         last_name: '',
//         email: '',
//         phone: '',
//         role: '',
//         ward_no: '',
//         position: '',
//         mahashakha: '',
//         shakha: '',
//         ra_pr_stah: '',
//     });

//     // useEffect(() => {
//     //     if (editMode && user) {
//     //         setFormData({
//     //             full_name: user.full_name || '',
//     //             last_name: user.last_name || '',
//     //             email: user.email || '',
//     //             phone: user.phone || '',
//     //             role: user.role || '',
//     //             ward_no: user.ward_no || '',
//     //             position: user.position || '',
//     //             mahashakha: user.mahashakha || '',
//     //             shakha: user.shakha || '',
//     //             ra_pr_stah: user.ra_pr_stah || '',
//     //         });
//     //     } else {
//     //         setFormData({
//     //             full_name: '',
//     //             last_name: '',
//     //             email: '',
//     //             phone: '',
//     //             role: '',
//     //             ward_no: '',
//     //             position: '',
//     //             mahashakha: '',
//     //             shakha: '',
//     //             ra_pr_stah: '',
//     //         });
//     //     }
//     // }, [editMode, user]);

//     useEffect(() => {
//     if (user) {
//         setFormData({
//             full_name: user.full_name || '',
//             last_name: user.last_name || '',
//             email: user.email || '',
//             phone: user.phone || '',
//             role: user.role || '',
//             ward_no: user.ward_no || '',
//             position: user.position || '',
//             mahashakha: user.mahashakha || '',
//             shakha: user.shakha || '',
//             ra_pr_stah: user.ra_pr_stah || '',
//         });
//     } else {
//         setFormData({
//             full_name: '',
//             last_name: '',
//             email: '',
//             phone: '',
//             role: '',
//             ward_no: '',
//             position: '',
//             mahashakha: '',
//             shakha: '',
//             ra_pr_stah: '',
//         });
//     }
// }, [user]);

//     const handleChange = (e) => {
//         const { name, value } = e.target;
//         setFormData((prev) => ({ ...prev, [name]: value }));
//     };

//     const handleSubmit = async (e) => {
//         e.preventDefault();

//         try {
//             let url = '/api/users/';
//             let method = 'post';

//             if (editMode && user?.id) {
//                 url += `${user.id}/`;
//                 method = 'put';
//             }

//             const token = localStorage.getItem('access_token');

//             const response = await fetch(url, {
//                 method,
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'Authorization': `Bearer ${token}`,
//                 },
//                 body: JSON.stringify(formData),
//             });

//             if (!response.ok) {
//                 const errorData = await response.json();
//                 alert('Error: ' + JSON.stringify(errorData));
//                 return;
//             }

//             onSuccess(); // refresh list
//             onClose();
//         } catch (error) {
//             alert('Submission error: ' + error.message);
//         }
//     };

//     if (!open) return null;

//     return (
//         <div
//             style={{
//                 position: 'fixed',
//                 inset: 0,
//                 background: 'rgba(0,0,0,0.4)',
//                 display: 'flex',
//                 justifyContent: 'center',
//                 alignItems: 'center',
//                 zIndex: 999,
//             }}
//             onClick={onClose}
//         >
//             <div
//                 onClick={(e) => e.stopPropagation()}
//                 style={{
//                     background: '#fff',
//                     padding: 20,
//                     borderRadius: 8,
//                     width: '500px',
//                     maxHeight: '90vh',
//                     overflowY: 'auto',
//                     boxShadow: '0 0 10px rgba(0,0,0,0.3)',
//                 }}
//             >
//                 <h2 style={{ marginBottom: 15 }}>{editMode ? 'प्रयोगकर्ता सम्पादन' : 'नयाँ प्रयोगकर्ता थप्नुहोस्'}</h2>
//                 <form onSubmit={handleSubmit}>

//                     <label>
//                         नाम *
//                         <input
//                             type="text"
//                             name="full_name"
//                             value={formData.full_name}
//                             onChange={handleChange}
//                             required
//                             disabled={viewOnly}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         थर
//                         <input
//                             type="text"
//                             name="last_name"
//                             value={formData.last_name}
//                             onChange={handleChange}
//                             disabled={viewOnly}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         इमेल *
//                         <input
//                             type="email"
//                             name="email"
//                             value={formData.email}
//                             onChange={handleChange}
//                             required
//                             disabled={viewOnly}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         फोन नम्बर *
//                         <input
//                             type="text"
//                             name="phone"
//                             value={formData.phone}
//                             onChange={handleChange}
//                             required
//                             disabled={viewOnly}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         प्रयोगकर्ता भूमिका *
//                         <select
//                             name="role"
//                             value={formData.role}
//                             onChange={handleChange}
//                             required
//                             disabled={viewOnly}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         >
//                             <option value="">-- भूमिका छान्नुहोस् --</option>
//                             {roles.map((role) => (
//                                 <option key={role} value={role}>
//                                     {role}
//                                 </option>
//                             ))}
//                         </select>
//                     </label>

//                     <label>
//                         वडा नंं. *
//                         <input
//                             type="number"
//                             name="ward_no"
//                             value={formData.ward_no}
//                             onChange={handleChange}
//                             required
//                             disabled={viewOnly}
//                             min={1}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         पद
//                         <input
//                             type="text"
//                             name="position"
//                             value={formData.position}
//                             disabled={viewOnly}
//                             onChange={handleChange}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         महाशाखा
//                         <input
//                             type="text"
//                             name="mahashakha"
//                             value={formData.mahashakha}
//                             disabled={viewOnly}
//                             onChange={handleChange}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         शाखा
//                         <input
//                             type="text"
//                             name="shakha"
//                             value={formData.shakha}
//                             disabled={viewOnly}
//                             onChange={handleChange}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>

//                     <label>
//                         रा. प्र. स्तह
//                         <input
//                             type="text"
//                             name="ra_pr_stah"
//                             value={formData.ra_pr_stah}
//                             disabled={viewOnly}
//                             onChange={handleChange}
//                             style={{ width: '100%', padding: 8, marginBottom: 12 }}
//                         />
//                     </label>
// {/* 
//                     <div style={{ textAlign: 'right', marginTop: 20 }}>
//                         <button
//                             type="button"
//                             onClick={onClose}
//                             style={{ marginRight: 10, padding: '8px 16px', background: '#ccc', borderRadius: 4 }}
//                         >
//                             Cancel
//                         </button>
//                         <button
//                             type="submit"
//                             style={{ padding: '8px 16px', background: '#2c3e50', color: 'white', borderRadius: 4 }}
//                         >
//                             {editMode ? 'Update' : 'Add'}
//                         </button>
//                     </div> */}

//                     <div style={{ textAlign: 'right', marginTop: 20 }}>
//   <button
//     type="button"
//     onClick={onClose}
//     style={{ marginRight: 10, padding: '8px 16px', background: '#ccc', borderRadius: 4 }}
//   >
//     Cancel
//   </button>

//   {!viewOnly && (
//     <button
//       type="submit"
//       style={{ padding: '8px 16px', background: '#2c3e50', color: 'white', borderRadius: 4 }}
//     >
//       {editMode ? 'Update' : 'Add'}
//     </button>
//   )}
// </div>

//                 </form>
//             </div>
//         </div>
//     );
// };

// export default UserFormModal;


import React, { useState, useEffect } from 'react';

const roles = [
  'admin',
  'planning section',
  'ward/office seceratery',
  'engineer',
  'ward engineer',
  'user committee',
  'Data Entry',
  'Department chief',
];

const UserFormModal = ({ open, onClose, editMode, user, onSuccess, viewOnly = false }) => {
  const [formData, setFormData] = useState({
    full_name: '',
    last_name: '',
    email: '',
    phone: '',
    role: '',
    ward_no: '',
    position: '',
    mahashakha: '',
    shakha: '',
    ra_pr_stah: '',
  });

  useEffect(() => {
    if (user) {
      setFormData({
        full_name: user.full_name || '',
        last_name: user.last_name || '',
        email: user.email || '',
        phone: user.phone || '',
        role: user.role || '',
        ward_no: user.ward_no || '',
        position: user.position || '',
        mahashakha: user.mahashakha || '',
        shakha: user.shakha || '',
        ra_pr_stah: user.ra_pr_stah || '',
      });
    } else {
      setFormData({
        full_name: '',
        last_name: '',
        email: '',
        phone: '',
        role: '',
        ward_no: '',
        position: '',
        mahashakha: '',
        shakha: '',
        ra_pr_stah: '',
      });
    }
  }, [user]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      let url = '/api/users/';
      let method = 'post';

      if (editMode && user?.id) {
        url += `${user.id}/`;
        method = 'put';
      }

      const token = localStorage.getItem('access_token');

      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        alert('Error: ' + JSON.stringify(errorData));
        return;
      }

      onSuccess();
      onClose();
    } catch (error) {
      alert('Submission error: ' + error.message);
    }
  };

  if (!open) return null;

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        background: 'rgba(0,0,0,0.4)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 999,
      }}
      onClick={onClose}
    >
      <div
        onClick={(e) => e.stopPropagation()}
        style={{
          background: '#fff',
          padding: 20,
          borderRadius: 8,
          width: '500px',
          maxHeight: '90vh',
          overflowY: 'auto',
          boxShadow: '0 0 10px rgba(0,0,0,0.3)',
        }}
      >
        <h2 style={{ marginBottom: 15 }}>
          {viewOnly ? 'प्रयोगकर्ता विवरण' : editMode ? 'प्रयोगकर्ता सम्पादन' : 'नयाँ प्रयोगकर्ता थप्नुहोस्'}
        </h2>

        <form onSubmit={handleSubmit}>
          {[
            { label: 'नाम *', name: 'full_name', required: true },
            { label: 'थर', name: 'last_name' },
            { label: 'इमेल *', name: 'email', type: 'email', required: true },
            { label: 'फोन नम्बर *', name: 'phone', required: true },
            { label: 'पद', name: 'position' },
            { label: 'महाशाखा', name: 'mahashakha' },
            { label: 'शाखा', name: 'shakha' },
            { label: 'रा. प्र. स्तह', name: 'ra_pr_stah' },
          ].map(({ label, name, required, type = 'text' }) => (
            <label key={name}>
              {label}
              <input
                type={type}
                name={name}
                value={formData[name]}
                onChange={handleChange}
                required={required}
                disabled={viewOnly}
                style={{ width: '100%', padding: 8, marginBottom: 12 }}
              />
            </label>
          ))}

          <label>
            प्रयोगकर्ता भूमिका *
            <select
              name="role"
              value={formData.role}
              onChange={handleChange}
              required
              disabled={viewOnly}
              style={{ width: '100%', padding: 8, marginBottom: 12 }}
            >
              <option value="">-- भूमिका छान्नुहोस् --</option>
              {roles.map((role) => (
                <option key={role} value={role}>
                  {role}
                </option>
              ))}
            </select>
          </label>

          <label>
            वडा नंं. *
            <input
              type="number"
              name="ward_no"
              value={formData.ward_no}
              onChange={handleChange}
              required
              min={1}
              disabled={viewOnly}
              style={{ width: '100%', padding: 8, marginBottom: 12 }}
            />
          </label>

          <div style={{ textAlign: 'right', marginTop: 20 }}>
            <button
              type="button"
              onClick={onClose}
              style={{ marginRight: 10, padding: '8px 16px', background: '#ccc', borderRadius: 4 }}
            >
              Cancel
            </button>

            {!viewOnly && (
              <button
                type="submit"
                style={{ padding: '8px 16px', background: '#2c3e50', color: 'white', borderRadius: 4 }}
              >
                {editMode ? 'Update' : 'Add'}
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};

export default UserFormModal;
