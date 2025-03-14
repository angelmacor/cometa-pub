"use client";

import { useTranslation } from "@/hooks/useTranslation";
import OrderSummary from "./components/OrderSummary";
import { useOrder } from "@/hooks/useOrder";

export default function OrdersPage() {
  const { t } = useTranslation(); 
  const { loading, error, orderRef } = useOrder();
  
  return (
    <div className="flex flex-col items-center mx-auto py-8 px-4">
      <h1 className="text-2xl font-bold text-center mb-6">{t("your_order")}</h1> 
      
      {loading && <p className="text-center">{t("loading_order")}</p>} 
      
      {error && <p className="text-red-500 text-center">{t("error_message")}</p>}
      
      {!loading && !error && !orderRef.current && (
        <p className="text-center">{t("no_order_available")}</p> 
      )}

      {orderRef.current && <OrderSummary order={orderRef.current} />}
    </div>
  );
}
