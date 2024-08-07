'use client'
import React, { Component, useState } from 'react';
import AddItemOverlayForm from './AddItemOverlayForm';
import Table from './DataTable';
import Header from './Header';
import { AppProps } from 'next/app';



export default function Home() {
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
          <button type="button" id="add" className="modification_button">+</button>
          <button type="button" id="delete" className="modification_button">-</button>
          <button type="button" id="update" className="modification_button">Update</button>

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


