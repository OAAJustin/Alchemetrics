import React, { useState, useEffect } from 'react';
import ModifyItemOverlayForm from './ModifyItemOverlayForm';
import { json } from 'stream/consumers';
import DataTableCSS from './DataTable.module.css';

interface TableData {
    uid: number;
    artist: string;
    title: string;
    medium: string;
    size: number;
    qty: number;
    price: number;
  }
  
  interface SelectedRowData {
    uid: number;
    artist: string;
    title: string;
    medium: string;
    size: number;
    qty: number;
    price: number;
  }

  const rowStyle: React.CSSProperties = {
    cursor: 'pointer',
  };

  const ArchiveTable: React.FC = () => {
    const [selectedRowData, setSelectedRowData] = useState<SelectedRowData | null>(null);
    const [showForm, setShowForm] = useState(false);
    const [data, setData] = useState<TableData[]>([]);
    const [refresh, setRefresh] = useState(false);

    const updateArchiveData = async () => {
        const res = await fetch('http://localhost:8080/get-archive-data', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        const sqlData = await res.json();
        setData(JSON.parse(await sqlData));
    }

    const handleRowClick = (rowData: TableData) => {
      setSelectedRowData(rowData);
      setShowForm(!showForm);
    };

    const toggleForm = () => {
      setShowForm(!showForm);
    };

    const refreshTable = () => {
      setRefresh(!refresh);
    }

    useEffect(() => {
      updateArchiveData();
      
    }, [refresh]);
  
    return (
      <div>
        <table className={DataTableCSS.table}>
    <thead>
      <tr>
        <th>UID</th>
        <th>Artist</th>
        <th>Title</th>
        <th>Medium</th>
        <th>Size</th>
        <th>Qty</th>
        <th>Price</th>
      </tr>
    </thead>
    <tbody>
      {data.map(item => (
            <tr key={item.uid} onClick={() => handleRowClick(item)} style={rowStyle}>
            <td>{item.uid}</td>
            <td>{item.artist}</td>
            <td>{item.title}</td>
            <td>{item.medium}</td>
            <td>{item.size}</td>
            <td>{item.qty}</td>
            <td>{item.price}</td>
          </tr>
          ))}
    </tbody>
        </table>
        <ModifyItemOverlayForm 
        show={showForm}
        onClose={toggleForm}
        uid={selectedRowData?.uid}
        artist={selectedRowData?.artist}
        title={selectedRowData?.title}
        medium={selectedRowData?.medium}
        size={selectedRowData?.size}
        qty={selectedRowData?.qty}
        price={selectedRowData?.price}
        refresh={refresh}
        updateTable={refreshTable}/>
      </div>
    );
    
  };

  
  
  export default ArchiveTable;