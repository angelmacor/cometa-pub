import { useState } from "react";
import BeerSelectionModal from "./BeerSelectionModal";
import { OrderItemDetail } from "@/types/order";
import { useTranslation } from "@/hooks/useTranslation";

interface AddRoundButtonProps {
  onAddRound: (items: OrderItemDetail[]) => void;
}

export default function AddRoundButton({ onAddRound }: AddRoundButtonProps) {
  const [isOpen, setIsOpen] = useState(false);
  const { t } = useTranslation(); 

  return (
    <>
      <button
        onClick={() => setIsOpen(true)}
        className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700"
      >
        {t('add_round')}
      </button>

      {isOpen && (
        <BeerSelectionModal
          isOpen={isOpen}
          onClose={() => setIsOpen(false)}
          onAdd={onAddRound}
        />
      )}
    </>
  );
}
