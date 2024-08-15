'use client'
import './globals.css'
import React, { Component, useState } from 'react';
import AddItemOverlayForm from '../app/AddItemOverlayForm';
import Table from '../app/DataTable';
import Header from '../app/Header';
import { AppProps } from 'next/app';

const Index: React.FC = () => {
  const [showForm, setShowForm] = useState(false);

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Header />
      <div style={{marginTop: '50px'}}>
        <Table />
        
        <div id="modifications_container">
          <div className="App">
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              onClick={toggleForm}
            >
              Add New Item
            </button>
            <AddItemOverlayForm show={showForm} onClose={toggleForm} />
          </div>
        </div>
    </div>
    </main>
  )
}

export default Index;


