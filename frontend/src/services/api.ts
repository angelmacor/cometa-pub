import { Beer, OrderItemDetail } from "@/types/order";
import { get, post } from "./apiClient";
import { API_ROUTES } from './apiRoutes';
import { Order } from "@/types/order";
import { ApiResponse } from "@/types/api";

const handleApiResponse = <T>(response: ApiResponse<T>): T => {
  if (!response.success) {
    throw new Error(response.message || "API request failed");
  }
  return response.data as T;
};

export const getStock = async () => {
  const response = await get(`${API_ROUTES.STOCK}`);
  return handleApiResponse(response);
};

export const getOrder = async () => {
  const response = await get<Order>(`${API_ROUTES.ORDER}`);
  return handleApiResponse(response);
};

interface CreateOrderRequest {
  name: string;
  quantity: number;
}

export interface CreateOrderResponse {
  subtotal: string;
  discounts: string;
  rounds: OrderItemDetail[];
}

export const api = {
  async getBeers(): Promise<Beer[]> {
    const response = await get<Beer[]>(`${API_ROUTES.BEERS}`);
    return handleApiResponse(response);
  },
  
  async createOrder(orderData: CreateOrderRequest): Promise<ApiResponse<CreateOrderResponse>> {
    const response = await post<CreateOrderResponse>(`${API_ROUTES.ORDER}`, orderData);
    return response;
  },

  async resetOrder(): Promise<void> {
    const response = await post<void>(`${API_ROUTES.RESET}`, {});
    return handleApiResponse<void>(response);
  }
}

export const payOrder = async () => {
  const response = await post(`${API_ROUTES.PAY}`,{});
  return handleApiResponse(response);
};
