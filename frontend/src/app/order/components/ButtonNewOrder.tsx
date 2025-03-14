import { useTranslation } from "@/hooks/useTranslation";
import { api } from "@/services/api";

interface ButtonNewOrderProps {
  onReset: () => void;
  onRefresh: () => void;
}

export default function ButtonNewOrder({ onReset, onRefresh }: ButtonNewOrderProps) {
  const { t } = useTranslation();

  const handleClick = async () => {
    try {
      await api.resetOrder();
      onReset();
      onRefresh();
    } catch (error) {
      console.error('Error resetting order:', error);
    }
  };

  return (
    <button color="white"
      onClick={handleClick}
      className="px-6 py-2 bg-white text-indigo-800 font-medium rounded-lg hover:bg-indigo-600 hover:text-white transition-colors"
    >
      {t("new_order")}
    </button>
  );
}
