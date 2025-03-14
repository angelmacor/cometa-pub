// app/services/apiRoutes.ts
export const API_MAIN = process.env.NEXT_PUBLIC_API_MAIN;

export const API_ROUTES = {
  
  ORDER: `${API_MAIN}/order`,
  STOCK: `${API_MAIN}/stock`,
  PAY: `${API_MAIN}/order/pay`,
  RESET: `${API_MAIN}/order/reset`,
  BEERS: `${API_MAIN}/stock/beers`,
  
};