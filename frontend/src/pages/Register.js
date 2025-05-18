import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import '../App.css'; // Assure-toi que le CSS est importé

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: '',
  });
  const [errors, setErrors] = useState({});
  const [apiError, setApiError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.username.trim()) {
      newErrors.username = 'Le nom d\'utilisateur est requis';
    } else if (formData.username.length < 3) {
      newErrors.username = 'Le nom doit contenir au moins 3 caractères';
    }

    if (!formData.email.includes('@')) {
      newErrors.email = 'Email invalide';
    }

    if (formData.password.length < 6) {
      newErrors.password = 'Le mot de passe doit contenir au moins 6 caractères';
    }

    if (formData.password !== formData.password2) {
      newErrors.password2 = 'Les mots de passe ne correspondent pas';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setApiError('');

    if (!validateForm()) return;

    try {
      const response = await api.post('users/register/', {
        username: formData.username,
        email: formData.email,
        password: formData.password,
      });

      // Si inscription réussie, redirige vers la page de connexion
      if (response.status === 201) {
        navigate('/login');
      }
    } catch (err) {
      if (err.response) {
        // Gestion des erreurs du backend
        if (err.response.data.username) {
          setErrors({ ...errors, username: err.response.data.username[0] });
        }
        if (err.response.data.email) {
          setErrors({ ...errors, email: err.response.data.email[0] });
        }
        setApiError(err.response.data.detail || 'Erreur lors de l\'inscription');
      } else {
        setApiError('Erreur de connexion au serveur');
      }
    }
  };

  return (
    <div className="auth-container">
      <h2>Créer un compte</h2>
      {apiError && <div className="error-message">{apiError}</div>}

      <form onSubmit={handleSubmit} noValidate>
        <div className="form-group">
          <label htmlFor="username">Nom d'utilisateur</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            className={errors.username ? 'input-error' : ''}
          />
          {errors.username && <span className="error-text">{errors.username}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className={errors.email ? 'input-error' : ''}
          />
          {errors.email && <span className="error-text">{errors.email}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="password">Mot de passe</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className={errors.password ? 'input-error' : ''}
          />
          {errors.password && <span className="error-text">{errors.password}</span>}
        </div>

        <div className="form-group">
          <label htmlFor="password2">Confirmer le mot de passe</label>
          <input
            type="password"
            id="password2"
            name="password2"
            value={formData.password2}
            onChange={handleChange}
            className={errors.password2 ? 'input-error' : ''}
          />
          {errors.password2 && <span className="error-text">{errors.password2}</span>}
        </div>

        <button type="submit" className="auth-button">
          S'inscrire
        </button>
      </form>

      <div className="auth-footer">
        Déjà inscrit? <a href="/login">Connectez-vous</a>
      </div>
    </div>
  );
};

export default Register;