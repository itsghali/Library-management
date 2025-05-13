import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from '../services/api';

const BookDetails = () => {
  const { id } = useParams(); // ID du livre depuis l'URL
  const [book, setBook] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchBookDetails();
  }, []);

  const fetchBookDetails = async () => {
    try {
      const response = await axios.get(`/books/${id}/`);
      setBook(response.data);
    } catch (error) {
      console.error('Erreur lors de la récupération du livre:', error);
    }
  };

  const handleBorrow = async () => {
    try {
      await axios.post('/borrow/', { book: id });
      setMessage('✅ Livre emprunté avec succès.');
    } catch (error) {
      console.error('Erreur lors de l\'emprunt:', error);
      setMessage('❌ Erreur lors de l\'emprunt.');
    }
  };

  const handleReserve = async () => {
    try {
      await axios.post('/reservations/', { book: id });
      setMessage('✅ Livre réservé avec succès.');
    } catch (error) {
      console.error('Erreur lors de la réservation:', error);
      setMessage('❌ Erreur lors de la réservation.');
    }
  };

  if (!book) return <p>Chargement...</p>;

  return (
    <div>
      <h1>{book.title}</h1>
      <p><strong>Auteur :</strong> {book.author}</p>
      <p><strong>Genre :</strong> {book.genre}</p>
      <p><strong>Description :</strong> {book.description}</p>
      <p><strong>Disponible :</strong> {book.available ? 'Oui' : 'Non'}</p>

      <div style={{ marginTop: '1rem' }}>
        <button onClick={handleBorrow}>📖 Emprunter</button>{' '}
        <button onClick={handleReserve}>🔖 Réserver</button>
      </div>

      {message && (
        <p style={{ marginTop: '1rem', fontWeight: 'bold' }}>{message}</p>
      )}
    </div>
  );
};

export default BookDetails;
