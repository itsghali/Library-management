import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const isLoggedIn = !!localStorage.getItem("token");

  return (
    <nav>
      <Link to="/">Home</Link>
      {isLoggedIn ? (
        <>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/borrows/create/">Add borrow</Link>
          <Link to="/reservations/create/">Add reservation</Link>
          <Link to="/logout">Logout</Link>
        </>
      ) : (
        <>
          <Link to="/login/">Login</Link>
          <Link to="register/">Register</Link>
        </>
      )}
    </nav>
  );
};

export default Navbar;
