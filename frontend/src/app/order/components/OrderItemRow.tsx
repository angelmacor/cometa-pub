import { OrderItemDetail } from "@/types/order";
import { formatCurrency } from "@/utils/format";
import { useTranslation } from "@/hooks/useTranslation"; 

interface OrderItemRowProps {
  item: OrderItemDetail;
}

export default function OrderItemRow({ item }: OrderItemRowProps) {
  const { t } = useTranslation();

  return (
    <div className="flex items-center gap-4">
      <div className="flex-1">
        <h3 className="font-semibold text-gray-900 dark:text-white">🪁 {item.name} 🍻</h3>
        <div className="flex items-center gap-2">
          <p className="text-sm text-gray-500 dark:text-gray-400">
            {formatCurrency(item.price_per_unit)} {t("each")}
          </p>
          {item.discounts > 0 && (
            <span className="text-xs bg-emerald-500/10 text-emerald-500 px-2 py-0.5 rounded">
              {t("happy_hour")}
            </span>
          )}
        </div>
      </div>
      <span className="w-8 text-center text-gray-900 dark:text-white">{item.quantity}</span>
      <div className="w-20 text-right gap-2">
        {item.discounts > 0 ? (
          <>
            <p className="text-sm line-through text-gray-500 dark:text-gray-400">
              {formatCurrency(item.price_per_unit * item.quantity)}
            </p>
            <p className="font-semibold text-emerald-600 dark:text-emerald-400">
              {formatCurrency(item.total_price || (item.price_per_unit * item.quantity - item.discounts))}
            </p>
          </>
        ) : (
          <p className="font-semibold text-gray-900 dark:text-white">
            {formatCurrency(item.subtotal || item.total_price)}
          </p>
        )}
      </div>
    </div>
  );
}
