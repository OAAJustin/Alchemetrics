// src/OverlayForm.tsx
import React from 'react';

interface ModifyItemOverlayFormProps {
  show: boolean;
  onClose: () => void;
  uid: number | undefined;
  artist: string | undefined;
  title: string | undefined;
  medium: string | undefined;
  size: number | undefined;
  qty: number | undefined;
  price: number | undefined;
}

const ModifyItemOverlayForm: React.FC<ModifyItemOverlayFormProps> = ({ show, onClose, uid, artist, title, medium, size, qty, price }) => {
  if (!show) return null;

  const data = { 
    UID: uid,
    Artist: artist,
    Title: title,
    Medium: medium,
    Size: size,
    Qty: qty,
    Price: price
  };

  const handleSubmit = async () => {
    const res = await fetch('http://localhost:8080/modify-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    const flaskData = await res.json()
    // setResponse(flaskData.message)
    onClose()
  }

  const handleDelete = async () => {
    const res = await fetch('http://localhost:8080/delete-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    const flaskData = await res.json()
    // setResponse(flaskData.message)
    onClose()
  }

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
      <div className="bg-white p-8 rounded shadow-lg w-full max-w-md relative">
        <button
          className="absolute top-4 right-4 text-gray-600"
          onClick={onClose}
        >
          &times;
        </button>
        <h2 className="text-2xl mb-4 text-gray-700">Modify Item</h2>
        <form>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="artist">
              Artist
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="artist"
              type="text"
              placeholder="Artist"
              value={artist}
              onChange={(e) => artist = e.target.value}
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="title">
              Title
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="title"
              type="text"
              placeholder="Title"
              value={title}
              onChange={(e) => title = e.target.value}
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="medium">
              Medium
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="medium"
              type="text"
              placeholder="Medium"
              value={medium}
              onChange={(e) => medium = e.target.value}
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="size">
              Size
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="size"
              type="number"
              placeholder="Size"
              value={size}
              onChange={(e) => size = e.target.valueAsNumber}
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="qty">
              Quantity
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="qty"
              type="number"
              placeholder="Quantity"
              value={qty}
              onChange={(e) => qty = e.target.valueAsNumber}
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="price">
              Price
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="price"
              type="number"
              placeholder="Price"
              value={price}
              onChange={(e) => price = e.target.valueAsNumber}
            />
          </div>

          <div className="flex items-center justify-between">
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button"
              onClick={handleSubmit}
            >
              Submit
            </button>

            <button
              className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button"
              onClick={handleDelete}
            >
              Delete
            </button>
          </div>

          

        </form>
      </div>
    </div>
  );
};

export default ModifyItemOverlayForm;
