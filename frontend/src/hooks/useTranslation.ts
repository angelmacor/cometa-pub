import es from "@/locales/es.json";

export function useTranslation() {
  const t = (key: string) => {
    return es[key as keyof typeof es] || key;
  };

  return { t };
}
