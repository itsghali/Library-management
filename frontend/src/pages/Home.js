import React, { useEffect, useState } from 'react';
import axios from '../services/api';
import BookCard from '../components/BookCard';

const Home = () => {
  const [books, setBooks] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await axios.get('/books/');
      setBooks(response.data);
      setFiltered(response.data);
    } catch (error) {
      console.error('Erreur lors de la récupération des livres:', error);
    }
  };

  const handleSearch = (e) => {
    const keyword = e.target.value;
    setSearch(keyword);
    const filteredBooks = books.filter((book) =>
      book.title.toLowerCase().includes(keyword.toLowerCase())
    );
    setFiltered(filteredBooks);
  };

  return (
    <div>
      <h1>📚 Liste des livres</h1>

      <input
        type="text"
        placeholder="Rechercher un livre par titre..."
        value={search}
        onChange={handleSearch}
        style={{
          padding: '0.5rem',
          width: '100%',
          margin: '1rem 0',
          borderRadius: '5px',
          border: '1px solid #ccc'
        }}
      />

      {filtered.length > 0 ? (
        filtered.map((book) => (
          <BookCard key={book.id} book={book} />
        ))
      ) : (
        <p>Aucun livre trouvé.</p>
      )}
    </div>
  );
};

export default Home;
