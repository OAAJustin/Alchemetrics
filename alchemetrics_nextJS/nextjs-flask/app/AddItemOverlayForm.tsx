// src/OverlayForm.tsx
import React from 'react';
import { useState } from 'react';

interface AddItemOverlayFormProps {
  show: boolean;
  onClose: () => void;
}

const AddItemOverlayForm: React.FC<AddItemOverlayFormProps> = ({ show, onClose}) => {
  if (!show) return null;
  const [response, setResponse] = useState<string | null>(null)

  const handleClick = async () => {
    const res = await fetch('http://localhost:8080/add-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    const data = await res.json()
    setResponse(data.message)
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
        <h2 className="text-2xl mb-4 text-gray-700">Add New Item</h2>
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
            />
          </div>

          <div className="flex items-center justify-between">
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button"
              onClick={handleClick}
            >
              Submit
            </button>
          </div>

        </form>
      </div>
    </div>
  );
};

export default AddItemOverlayForm;
