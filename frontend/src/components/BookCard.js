import React from 'react';

const BookCard = ({ book }) => {
  return (
    <div className="book-card">
      <h3>{book.title}</h3>
      <p>Auteur : {book.author}</p>
      <p>Disponible : {book.available ? 'Oui' : 'Non'}</p>
    </div>
  );
};

export default BookCard;
