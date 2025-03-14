import { useEffect, useState, useRef } from "react";
import { getOrder } from "@/services/api";
import { Order } from "@/types/order";

interface ApiResponse {
  success: boolean;
  data?: Order;
  error?: string;
}

export const useOrder = (initialOrder?: Order) => {
  const [order, setOrder] = useState<Order | undefined>(initialOrder);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const orderRef = useRef<Order>(initialOrder);

  const fetchOrder = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await getOrder();
      setOrder(response);
      orderRef.current = response;
    } catch (err: any) {
      setError(err.message || "Failed to fetch orders");
      setOrder(undefined);
      orderRef.current = undefined;
    } finally {
      setLoading(false);
    }
  };

  const resetOrder = () => {
    setOrder(undefined);
    orderRef.current = undefined;
    setError(null);
  };

  useEffect(() => {
    fetchOrder();
  }, []);

  return { order, loading, error, refresh: fetchOrder, reset: resetOrder, orderRef };
};

