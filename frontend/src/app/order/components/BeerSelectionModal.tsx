import { useState } from "react";
import { Beer, OrderAdd, OrderItemDetail } from "@/types/order";
import { useBeers } from "@/hooks/useBeers";
import { useOrder } from "@/hooks/useOrder";
import Modal from "@/components/UI/Modal";
import { api } from "@/services/api";

interface BeerSelectionModalProps {
  isOpen: boolean;
  onClose: () => void;
  onAdd: (items: OrderItemDetail[]) => void;
}

export default function BeerSelectionModal({ isOpen, onClose, onAdd }: BeerSelectionModalProps) {
  const { beers, loading, error } = useBeers();
  const { refresh: refreshOrder } = useOrder();
  const [selectedItems, setSelectedItems] = useState<OrderAdd[]>([]);
  const [submitting, setSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);
  const handleQuantityChange = (beer: Beer, increment: number) => {
    setSubmitError(null);
    setSelectedItems((prev) => {
      // If incrementing and there's a different beer selected, replace it
      if (increment > 0 && prev.length > 0 && prev[0].nameId !== beer.nameId) {
        return [{ nameId: beer.nameId, name: beer.name, price: beer.price, quantity: 1 }];
      }

      const existing = prev.find((item) => item.nameId === beer.nameId);
      if (existing) {
        const newQuantity = existing.quantity + increment;
        if (newQuantity <= 0) {
          return [];
        }
        return [{ ...existing, quantity: newQuantity }];
      }

      if (increment <= 0) return prev;
      return [{ nameId: beer.nameId, name: beer.name, price: beer.price, quantity: 1 }];
    });
  };

  const getItemQuantity = (beerId: string) => {
    const item = selectedItems.find((item) => item.nameId === beerId);
    return item?.quantity || 0;
  };

  const handleConfirm = async () => {

    if (selectedItems.length === 0) return;
    
    setSubmitting(true);
    setSubmitError(null);

    try {
      // Send only the first selected item to match the API format
      const firstItem = selectedItems[0];
      const orderData = {
        name: firstItem.name,
        quantity: firstItem.quantity
      };

      const response = await api.createOrder(orderData);

      if (response.success && response.data) {
        // Update the items with the response data
        const { rounds } = response.data;
        if (rounds) {
          onAdd(rounds);
          await refreshOrder(); // Refresh the order after successful creation
        }
        onClose();
      } else {
        const errorMessage = response.error?.detail || response.message || "Failed to create order";
        setSubmitError(errorMessage);
      }
    } catch (err) {
      // Handle network or unexpected errors
      const error = err as any;
      const errorMessage = error?.response?.data?.detail || error?.message || "An error occurred while creating the order";
      setSubmitError(errorMessage);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Select Beers">
      {loading && <p>Loading...</p>}

      {!loading && (
        <div className="space-y-4">
          <select 
            className="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            onChange={(e) => {
              const beer = beers.find(b => b.nameId === e.target.value);
              if (beer) {
                handleQuantityChange(beer, 1);
              }
            }}
            value={selectedItems.length > 0 ? selectedItems[0].nameId : ""}

          >
            <option value="" disabled>Select a beer</option>
            {beers.map((beer) => (
              <option key={beer.nameId} value={beer.nameId}>
                {beer.name} - ${beer.price.toFixed(2)}
              </option>
            ))}
          </select>

          {selectedItems.length > 0 && (
            <div className="mt-6 space-y-4">
              <div className="space-y-3">
                {selectedItems.map((item) => (
                  <div 
                    key={item.nameId} 
                    className="flex items-center justify-between bg-white p-4 rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-shadow"
                  >
                    <div className="flex flex-col">
                      <span className="font-medium text-gray-900"> 🪁 {item.name}</span>
                      <span className="text-gray-600">${item.price.toFixed(2)}</span>
                    </div>
                    <div className="flex items-center space-x-3">
                      <button
                        onClick={() => handleQuantityChange({ nameId: item.nameId, name: item.name, price: item.price } as Beer, -1)}
                        className="w-8 h-8 flex items-center justify-center bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                        disabled={submitting}
                      >
                        -
                      </button>
                      <span className="w-8 text-center text-gray-700 font-medium">{item.quantity}</span>
                      <button
                        onClick={() => handleQuantityChange({ nameId: item.nameId, name: item.name, price: item.price } as Beer, 1)}
                        className="w-8 h-8 flex items-center justify-center bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                        disabled={submitting}
                      >
                        +
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
          {error && <p className="flex text-red-500">{error}</p>}
          {submitError && <p className="flex text-red-500">{submitError}</p>}
          <button 
            onClick={handleConfirm} 
            className="w-full mt-2 bg-green-600 text-white py-2 rounded-lg hover:bg-green-700 disabled:bg-gray-400"
            disabled={submitting || selectedItems.length === 0}
          >
            {submitting ? "Send Order..." : "Confirm Selection"}
          </button>
        </div>
      )}

    </Modal>
  );
}
