'use client'
import './globals.css'
import React, { Component, useState } from 'react';
import AddItemOverlayForm from '../app/AddItemOverlayForm';
import Table from '../app/DataTable';
import ArchiveTable from '@/app/ArchiveDataTable';
import Header from '../app/Header';
import { AppProps } from 'next/app';

const Archive: React.FC = () => {
  const [showForm, setShowForm] = useState(false);

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Header />
      <div style={{marginTop: '50px'}}>
        <ArchiveTable />
    </div>
    </main>
  )
}

export default Archive;