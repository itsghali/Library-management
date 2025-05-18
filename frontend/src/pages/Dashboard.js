import { useEffect, useState } from 'react';
import axios from '../services/api';

const Dashboard = () => {
  const [borrows, setBorrows] = useState([]);
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchUserData();
  }, []);

  const fetchUserData = async () => {
    try {
      const borrowRes = await axios.get('http://localhost:8000/api/borrows/');
      console.log('Raw borrow data:', borrowRes.data); // Debug log
      
      const reservationRes = await axios.get('http://localhost:8000/api/reservations/');
      console.log('Raw reservation data:', reservationRes.data); // Debug log

      setBorrows(borrowRes.data);
      setReservations(reservationRes.data);
    } catch (err) {
      console.error('Erreur lors de la récupération des données:', err);
      setError("Impossible de récupérer les données de l'utilisateur.");
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <p>Chargement...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;


  return (
    <div>
      <h2>📖 Mes Emprunts</h2>
      {borrows.length > 0 ? (
        <ul>
          {borrows.map((item) => (
            <li key={item.id} style={{ 
            padding: '1rem',
          }}>
              <strong>Livre: {item.book}</strong>
              <p><strong>Utilisateur</strong>: {item.user}</p>
              <p><strong>Date d'emprunt</strong>: {new Date(item.borrow_date).toLocaleDateString()}</p>
              <p><strong>Date de retour</strong>: {new Date(item.return_date).toLocaleDateString()}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Aucun emprunt en cours.</p>
      )}

      <h2 style={{ marginTop: '2rem' }}>🔖 Mes Réservations</h2>
      {reservations.length > 0 ? (
        <ul>
          {reservations.map((item) => (
            <li key={item.id} style={{ 
            padding: '1rem',
          }}>
              <strong>Livre : {item.book_title}</strong>
              <p><strong>Utilisateur</strong> : {item.user_name}</p>
              <p><strong>Réservé le</strong>: {new Date(item.reserved_at).toLocaleDateString()}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Aucune réservation en cours.</p>
      )}
    </div>
  );
};

export default Dashboard;