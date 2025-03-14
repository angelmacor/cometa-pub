import { useTranslation } from "@/hooks/useTranslation";
import { payOrder } from "@/services/api";
import { useState } from "react";

interface PayButtonProps {
  onPaymentSuccess: () => void;
}

export default function PayButton({ onPaymentSuccess }: PayButtonProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const { t } = useTranslation(); 


  const handlePayment = async () => {
    setLoading(true);
    setError(null); // Reset error before making the payment
    try {
      await payOrder();
      onPaymentSuccess();
    } catch (error) {
      setError('Payment failed. Please try again.');
      console.error('Payment failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full">
      {error && <p className="text-red-500">{error}</p>}
      <button 
        onClick={handlePayment}
        className={`w-full ${loading ? 'bg-gray-500 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700'} text-white font-medium py-3 rounded-lg transition-colors`}
        disabled={loading}
      >
        {loading ? t('processing') : t('pay')}

        </button>
    </div>
  );
}
