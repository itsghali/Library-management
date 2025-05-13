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
      const [borrowRes, reservationRes] = await Promise.all([
        axios.get('/borrow/'),
        axios.get('/reservations/')
      ]);

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
            <li key={item.id}>
              <strong>{item.book.title}</strong> – Emprunté le {item.borrow_date}
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
            <li key={item.id}>
              <strong>{item.book.title}</strong> – Réservé le {item.reservation_date}
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
