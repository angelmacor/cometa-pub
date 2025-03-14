import { Order, OrderItemDetail } from "@/types/order";
import PayButton from "./PayButton";
import { useEffect } from "react";
import AddRoundButton from "./AddRound";
import { formatCurrency } from "@/utils/format";
import { useOrder } from "@/hooks/useOrder";
import { api } from "@/services/api";
import ButtonNewOrder from "./ButtonNewOrder";
import OrderItemRow from "./OrderItemRow";
import { useTranslation } from "@/hooks/useTranslation";

interface OrderProps {
  order: Order;
}

export default function OrderSummary({ order }: OrderProps) {
  const { refresh: refreshOrder, orderRef, reset } = useOrder();
  const { t } = useTranslation(); 

  const total =
    (orderRef.current?.subtotal || 0.0) +
    (orderRef.current?.taxes || 0.0) -
    (orderRef.current?.discounts || 0.0);
  const textStyle = "text-base text-gray-500 dark:text-gray-400";
  const wasPaid = orderRef.current?.status === "paid";

  useEffect(() => {
    if (order) {
      orderRef.current = order;
    }
  }, [order]);

  const handleAddRound = async (newItems: OrderItemDetail[]) => {
    if (orderRef.current) {
      orderRef.current.rounds = [
        ...(orderRef.current.rounds || []),
        { items: newItems, created: new Date().toISOString() },
      ];
      await refreshOrder();
    }
  };

  if (!orderRef.current) return null;

  return (
    <div className="max-w-2xl w-full dark:bg-gray-800 rounded-xl shadow-lg p-6">
      <div className="flex justify-between items-center mb-6">
        <div className="flex items-center gap-x-1.5">
          <h2 className="text-2xl font-bold text-gray-200">{t("order")}</h2>
          <div
            className={`flex-none rounded-full ${
              wasPaid ? "bg-emerald-500/20" : "bg-red-500/20"
            } p-1`}
          >
            <div
              className={`size-1.5 rounded-full ${
                wasPaid ? "bg-emerald-500" : "bg-red-500"
              }`}
            />
          </div>
          <p
            className={`text-sm ${
              wasPaid ? "text-emerald-500" : "text-red-500"
            }`}
          >
            {wasPaid ? t("paid") : t("pending")}
          </p>
        </div>

        {!wasPaid ? (
          <div className="flex items-center gap-x-1.5">
            <AddRoundButton onAddRound={handleAddRound} />
          </div>
        ) : (
          <ButtonNewOrder onReset={reset} onRefresh={refreshOrder} />
        )}
      </div>
      <div className="space-y-4">
        {orderRef.current.rounds.map((round, roundIndex) => (
          <div
            key={roundIndex}
            className="bg-gray-100 dark:bg-gray-700 rounded-lg p-4"
          >
            <div className="flex justify-between items-center mb-3">
              <p className="text-sm font-medium text-gray-500 dark:text-gray-300">
                {t("round")} {roundIndex + 1}
              </p>
              <p className="text-sm text-gray-500 dark:text-gray-300">
                {round.created}
              </p>
            </div>
            <div className="space-y-3">
              {round.items.map((item, itemIndex) => (
                <OrderItemRow key={itemIndex} item={item} />
              ))}
            </div>
          </div>
        ))}

        {/* Resumen de Totales */}
        <div className="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
          <div className={`flex justify-between ${textStyle} mb-2`}>
            <p>{t("subtotal")}</p>
            <p>{formatCurrency(orderRef.current.subtotal)}</p>
          </div>
          <div className={`flex justify-between ${textStyle} mb-2`}>
            <p>{t("taxes")}</p>
            <p>{formatCurrency(orderRef.current.taxes)}</p>
          </div>
          {orderRef.current.discounts > 0 && (
            <div className={`flex justify-between ${textStyle} mb-2`}>
              <p>{t("discounts")}</p>
              <p>-{formatCurrency(orderRef.current.discounts)}</p>
            </div>
          )}
          <div className="flex justify-between text-lg font-bold text-gray-900 dark:text-white mb-6">
            <p>{t("total")}</p>
            <p>{formatCurrency(total)}</p>
          </div>

          {!wasPaid && orderRef.current.rounds.length>0 && (
            <div className="flex justify-center">
              <PayButton onPaymentSuccess={refreshOrder}/>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
