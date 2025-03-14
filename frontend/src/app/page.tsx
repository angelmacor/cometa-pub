import { useTranslation } from "@/hooks/useTranslation";

export const runtime = 'nodejs';

export default function Home() {
  const { t } = useTranslation();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-4">{t("welcome_to_cometa")}</h1> 
      <p className="text-lg text-gray-600">{t("order_your_favorite_beer")}</p> 
      <a
        href="/order"
        className="mt-6 px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700"
      >
        {t("go_to_order")}
      </a>
    </div>
  );
}
