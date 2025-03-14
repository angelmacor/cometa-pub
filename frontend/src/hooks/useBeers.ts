import { useEffect, useState } from "react";
import { api } from "@/services/api";
import { Beer } from "@/types/order";

export const useBeers = () => {
  const [beers, setBeers] = useState<Beer[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchBeers = async () => {
      try {
        const data = await api.getBeers();
        setBeers(data);
      } catch (err) {
        setError("Failed to fetch beers");
      } finally {
        setLoading(false);
      }
    };

    fetchBeers();
  }, []);

  return { beers, loading, error };
};
