import React, { useEffect, useState } from 'react';
import axios from '../services/api';

const AdminDashboard = () => {
  const [books, setBooks] = useState([]);
  const [form, setForm] = useState({ title: '', author: '', genre: '', description: '' });
  const [editId, setEditId] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const res = await axios.get('/books/');
      setBooks(res.data);
    } catch (error) {
      console.error('Erreur lors du chargement des livres', error);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editId) {
        await axios.put(`/books/${editId}/`, form);
        setMessage('📘 Livre modifié avec succès.');
      } else {
        await axios.post('/books/', form);
        setMessage('📕 Livre ajouté avec succès.');
      }
      setForm({ title: '', author: '', genre: '', description: '' });
      setEditId(null);
      fetchBooks();
    } catch (err) {
      console.error('Erreur lors de l\'ajout/modification du livre', err);
      setMessage('❌ Une erreur est survenue.');
    }
  };

  const handleEdit = (book) => {
    setForm({
      title: book.title,
      author: book.author,
      genre: book.genre,
      description: book.description,
    });
    setEditId(book.id);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Supprimer ce livre ?')) return;
    try {
      await axios.delete(`/books/${id}/`);
      setMessage('🗑️ Livre supprimé.');
      fetchBooks();
    } catch (err) {
      console.error('Erreur lors de la suppression', err);
      setMessage('❌ Erreur lors de la suppression.');
    }
  };

  return (
    <div>
      <h2>📚 Tableau de bord Administrateur</h2>

      <form onSubmit={handleSubmit} style={{ marginBottom: '2rem' }}>
        <h3>{editId ? 'Modifier le livre' : 'Ajouter un nouveau livre'}</h3>
        <input
          type="text"
          name="title"
          placeholder="Titre"
          value={form.title}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="author"
          placeholder="Auteur"
          value={form.author}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="genre"
          placeholder="Genre"
          value={form.genre}
          onChange={handleChange}
        />
        <textarea
          name="description"
          placeholder="Description"
          value={form.description}
          onChange={handleChange}
        />
        <button type="submit">{editId ? 'Modifier' : 'Ajouter'}</button>
      </form>

      {message && <p><strong>{message}</strong></p>}

      <h3>📖 Liste des livres</h3>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            <strong>{book.title}</strong> – {book.author}
            <div>
              <button onClick={() => handleEdit(book)}>✏️ Modifier</button>{' '}
              <button onClick={() => handleDelete(book.id)}>🗑️ Supprimer</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminDashboard;
